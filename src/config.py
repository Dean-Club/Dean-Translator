# ============ 配置部分 ============
LLM_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
LLM_MODEL = "gemma-3-12b-it-qat"

# WhisperX 模型名称
WHISPER_MODEL_NAME = "medium"
WHISPER_COMPUTE_TYPE = "float16"  # 可视情况改为 "float32" 或 "float16"
WHISPER_ASR_OPTIONS = {
     "multilingual": True,
     "hotwords": None,
     "length_penalty": 20,  # 惩罚长句生成
     "word_timestamps": True  # 启用单词级时间戳
}

# 对齐模型语言代码（与源语言保持一致）
ALIGN_MODEL_LANGUAGE_CODE = "en"

input_video_folder_path = "Video_to_translate"
output_video_folder_path = "Generated_subtitles"