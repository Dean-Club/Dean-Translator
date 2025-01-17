import whisperx
import os
import torch
from datetime import timedelta
import deepl  # 引入 DeepL 包

# 设置 DeepL API 密钥
DEEPL_API_KEY = 'deepL_API'  # 替换为你的 DeepL API 密钥
translator = deepl.Translator(DEEPL_API_KEY)

torch.cuda.empty_cache()

def format_srt_timestamp(seconds):
    """
    格式化秒数为 SRT 时间戳格式 (hh:mm:ss,ms)。
    """
    td = timedelta(seconds=seconds)
    total_seconds = td.total_seconds()
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"

def generate_translated_srt(audio_file_path, output_srt_file_path, source_lang="en", target_lang="zh"):
    """
    从音频文件生成带翻译的 SRT 字幕文件，结合 WhisperX 实现精准的字母级时间戳对齐和断句。

    参数:
    audio_file_path (str): 音频文件的路径。
    output_srt_file_path (str): 输出 SRT 文件的路径。
    source_lang (str): 源语言代码。
    target_lang (str): 目标语言代码。
    """

    # Step 1: 加载 WhisperX 模型并转录
    device = "cuda" if torch.cuda.is_available() else "cpu"  # 使用GPU或CPU
    compute_type = "int8"  # 如果没有 GPU 或 GPU 不支持 float16，使用 float32 或 int8
    whisper_model = whisperx.load_model("medium", device, compute_type=compute_type, asr_options={
        "multilingual": True,
        "hotwords": None
    })

    # 加载音频
    audio = whisperx.load_audio(audio_file_path)

    # 使用 WhisperX 进行初步转录
    result = whisper_model.transcribe(
        audio,
        batch_size=1,
        chunk_size=30,  # 增大 chunk_size
    )

    print("Initial transcription segments:", result["segments"])

    # Step 2: 使用 wav2vec2 对字母进行精确对齐
    align_model, metadata = whisperx.load_align_model(language_code=source_lang, device=device)
    aligned_result = whisperx.align(result["segments"], align_model, metadata, audio, device)
    print("Aligned transcription segments:", aligned_result["segments"])

    # Step 3: 将结果转换为 SRT 格式并保存
    with open(output_srt_file_path, 'w', encoding='UTF-8') as srt_file:
        for i, segment in enumerate(aligned_result["segments"], start=1):
            start_seconds = segment["start"]
            end_seconds = segment["end"]

            # 格式化开始和结束时间为 SRT 格式
            start_srt = format_srt_timestamp(start_seconds)
            end_srt = format_srt_timestamp(end_seconds)

            # 原始文本
            text = segment["text"]

            # 翻译文本 (通过 DeepL API)
            print(f"Translating text: {text}")
            try:
                result_translation = translator.translate_text(text, target_lang=target_lang)  # 自动检测输入语言
                translated_text = result_translation.text
            except deepl.DeepLException as e:
                print(f"Error with DeepL API: {e}")
                translated_text = "[Translation Error]"

            print(f"Translated text: {translated_text}")

            # 写入 SRT 文件
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_srt} --> {end_srt}\n")
            srt_file.write(f"{translated_text}\n")
            srt_file.write(f"{text}\n\n")

    print(f"SRT 文件已保存至：{output_srt_file_path}")

# 设置音频文件路径和输出
audio_folder_path = "Video_to_translate"
video_finished_path = "Generated_subtitles"
# 获取所有 mp4 或 wav 文件
audio_files = [
    file for file in os.listdir(audio_folder_path)
    if os.path.isfile(os.path.join(audio_folder_path, file))
    and file.endswith(('.mp4', '.m4v'))
]

# 遍历音频文件路径列表并生成对应的 SRT 文件
for audio_file in audio_files:
    audio_file_path = os.path.join(audio_folder_path, audio_file)
    audio_name = os.path.splitext(audio_file)[0]
    output_srt_file_path = os.path.join(audio_folder_path, f'{audio_name}.srt')
    generate_translated_srt(audio_file_path, video_finished_path)
