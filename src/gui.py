import sys,os
sys.path.append(os.path.dirname(__file__))  # 把 src 加入模块路径
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from main import main  # 导入你的批量转录函数


# 运行 main() 的线程类，避免 GUI 卡顿
class TranscribeThread(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, config):
        super().__init__()
        self.config = config

    def run(self):
        try:
            main(**self.config)
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))


class TranscribeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhisperX 批量转录工具")
        self.setGeometry(300, 300, 500, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 输入路径
        self.input_label = QLabel("输入视频文件夹路径：")
        self.input_path = QLineEdit("Video_to_translate")
        self.input_browse = QPushButton("浏览")
        self.input_browse.clicked.connect(self.browse_input)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_path)
        input_layout.addWidget(self.input_browse)

        # 输出路径
        self.output_label = QLabel("输出字幕文件夹路径：")
        self.output_path = QLineEdit("Generated_subtitles")
        self.output_browse = QPushButton("浏览")
        self.output_browse.clicked.connect(self.browse_output)
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(self.output_browse)

        # WhisperX 模型选择
        self.model_label = QLabel("WhisperX 模型：")
        self.model_choice = QComboBox()
        self.model_choice.addItems(["tiny", "base", "small", "medium", "large-v3"])
        self.model_choice.setCurrentText("medium")

        # 计算类型选择
        self.compute_label = QLabel("计算类型：")
        self.compute_choice = QComboBox()
        self.compute_choice.addItems(["int8","float16", "float32"])
        self.compute_choice.setCurrentText("float16")

        # 语言代码选择
        self.language_label = QLabel("对齐语言代码：")
        self.language_choice = QComboBox()
        self.language_choice.addItems(["en", "zh", "de", "fr", "es"])
        self.language_choice.setCurrentText("en")
        
        # LLM 模型选择（新增）
        self.llm_label = QLabel("LLM 模型：")
        self.llm_choice = QComboBox()
        self.llm_choice.addItems(["meta-llama-3.1-8b-instruct", "gemma-3-12b-it-qat"])
        self.llm_choice.setCurrentText("qwen-2")

        # 启动/取消按钮
        self.start_button = QPushButton("开始转录")
        self.start_button.clicked.connect(self.start_transcription)

        self.cancel_button = QPushButton("取消")
        self.cancel_button.clicked.connect(self.cancel_transcription)
        self.cancel_button.setEnabled(False)

        # 状态显示
        self.status_label = QLabel("状态：等待开始")
        self.status_label.setAlignment(Qt.AlignCenter)

        # 布局组装
        layout.addWidget(self.input_label)
        layout.addLayout(input_layout)

        layout.addWidget(self.output_label)
        layout.addLayout(output_layout)

        layout.addWidget(self.model_label)
        layout.addWidget(self.model_choice)

        layout.addWidget(self.compute_label)
        layout.addWidget(self.compute_choice)

        layout.addWidget(self.language_label)
        layout.addWidget(self.language_choice)
        
        layout.addWidget(self.llm_label)
        layout.addWidget(self.llm_choice)


        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def browse_input(self):
        folder = QFileDialog.getExistingDirectory(self, "选择输入文件夹")
        if folder:
            self.input_path.setText(folder)

    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹")
        if folder:
            self.output_path.setText(folder)

    def start_transcription(self):
        self.status_label.setText("开始转录...")
        self.start_button.setEnabled(False)
        self.cancel_button.setEnabled(True)

        # 收集配置项
        config = {
            "input_video_folder_path": self.input_path.text(),
            "output_video_folder_path": self.output_path.text(),
            "whisper_model_name": self.model_choice.currentText(),
            "whisper_compute_type": self.compute_choice.currentText(),
            "whisper_asr_options": {
                "multilingual": True,
                "hotwords": None,
                "length_penalty": 20,
                "word_timestamps": True
            },
            "align_model_language_code": self.language_choice.currentText(),
            "llm_model_name": self.llm_choice.currentText()

        }

        # 启动线程
        self.thread = TranscribeThread(config)
        self.thread.finished.connect(self.transcription_finished)
        self.thread.error.connect(self.transcription_error)
        self.thread.start()

    def cancel_transcription(self):
        if hasattr(self, 'thread') and self.thread.isRunning():
            self.thread.terminate()
            self.status_label.setText("已取消")
            self.start_button.setEnabled(True)
            self.cancel_button.setEnabled(False)

    def transcription_finished(self):
        self.status_label.setText("转录完成！")
        self.start_button.setEnabled(True)
        self.cancel_button.setEnabled(False)

    def transcription_error(self, msg):
        print("[错误调试] ", msg)  # 打印到终端（方便调试）
        self.status_label.setText(f"错误: {msg}")
        self.start_button.setEnabled(True)
        self.cancel_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranscribeWindow()
    window.show()
    sys.exit(app.exec_())
