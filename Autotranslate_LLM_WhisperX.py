import os
import torch
import requests
import whisperx

# ============ 配置部分 ============
LLM_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
LLM_MODEL = "gemma-3-12b-it-qat"

# WhisperX 模型名称
WHISPER_MODEL_NAME = "medium"
WHISPER_COMPUTE_TYPE = "int8"  # 可视情况改为 "float32" 或 "float16"
WHISPER_ASR_OPTIONS = {
    #  "multilingual": True,
    # "hotwords": None,
    # "patience": 1.2,  # 允许稍微耐心地生成文本，确保完整性
     "length_penalty": 20,  # 惩罚长句生成
     "word_timestamps": True  # 启用单词级时间戳
    # "max_new_tokens": 100  # 限制生成文本长度，避免过长
}

# 对齐模型语言代码（与源语言保持一致）
ALIGN_MODEL_LANGUAGE_CODE = "en"

def local_translate_with_memory(text: str, conversation_history: list) -> str:
    """
    调用本地 LLM（通过 LLM_API_URL）来翻译文本，并支持上下文对话记忆。
    """
    # 动态提示（例如动态追加提示）
    dynamic_prompt = "直接翻译成中文:"
    conversation_history.append({"role": "user", "content": f"{dynamic_prompt}\n\n{text}"})

    payload = {
        "model": LLM_MODEL,
        "messages": conversation_history,
        "max_tokens": 200,
        "temperature": 0.5
    }
    try:
        response = requests.post(LLM_API_URL, json=payload, timeout=600)
        response.raise_for_status()
        data = response.json()
        translation = data["choices"][0]["message"]["content"].strip()
        conversation_history.append({"role": "assistant", "content": translation})
        return translation
    except Exception as e:
        print(f"Error calling local LLM API: {e}")
        return "[Translation Error]"


def load_whisperx_model():
    """
    加载 WhisperX 模型及对齐模型，返回 (whisper_model, align_model, metadata)。
    """
    device_type = "cuda" if torch.cuda.is_available() else "cpu"
    # 加载 Whisper 模型
    whisper_model = whisperx.load_model(
        WHISPER_MODEL_NAME,
        device_type,
        compute_type=WHISPER_COMPUTE_TYPE,
        asr_options=WHISPER_ASR_OPTIONS
    )
    # 加载对齐模型
    align_model, metadata = whisperx.load_align_model(
        language_code=ALIGN_MODEL_LANGUAGE_CODE,
        device=device_type
    )
    return whisper_model, align_model, metadata

def format_srt_time(seconds: float) -> str:
    """
    将浮点秒数格式化成 SRT 时间格式（HH:MM:SS,mmm）。
    """
    total_milliseconds = int(seconds * 1000)
    hours, remainder = divmod(total_milliseconds, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def generate_translated_srt(
        video_file_path: str,
        output_srt_file_path: str,
        whisper_model,
        align_model,
        metadata
    ):
    """
    生成带翻译的 SRT 文件，利用 WhisperX 进行精准转录与对齐，然后调用本地 LLM 翻译。
    """
    device_type = "cuda" if torch.cuda.is_available() else "cpu"

    # 每次文件处理都使用新的会话历史
    conversation_history = [
        {
            "role": "system",
            "content": (
                "你是一名字幕翻译员，负责将各种类型的字幕高效、准确地翻译成自然流畅的简体中文，请遵守以下标准：\n\n"
            "- 自然流畅：符合中文语言习惯。\n"
            "- 语境精准：理解语境，准确传达原意，确保逻辑清晰。\n"
            "- 术语专业：根据语境，准确翻译专业术语。\n"
            "- 文化适配：本地化俚语和隐喻。\n"
            "- 清晰简洁：表达简明易懂。\n"
            "- 专注内容：只翻译字幕内容，不添加多余信息。\n"
            "目标是提供高质量字幕翻译，让观众理解准确、阅读流畅，请注意，我并不是在和你交流。\n"
            )
        }
    ]

    # Step 1: 加载音频并转录
    video = whisperx.load_audio(video_file_path)
    result = whisper_model.transcribe(video, batch_size=1, 
                                      chunk_size=30, 
                                      language="de"
                                      )
    print("Initial transcription segments:", result["segments"])

    # Step 2: wav2vec2 精准对齐
    aligned_result = whisperx.align(result["segments"], align_model, metadata, video, device_type)
    print("Aligned transcription segments:", aligned_result["segments"])

    # Step 3: 输出到 SRT 文件
    with open(output_srt_file_path, 'w', encoding='UTF-8') as srt_file:
        for i, segment in enumerate(aligned_result["segments"], start=1):
            start_srt = format_srt_time(segment["start"])
            end_srt = format_srt_time(segment["end"])

            text = segment["text"].strip()
            # print(f"Translating text: {text}")
            translated_text = local_translate_with_memory(text, conversation_history)
            # print(f"Translated text: {translated_text}")

            # 写入 SRT
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_srt} --> {end_srt}\n")
            srt_file.write(f"{translated_text}\n")
            srt_file.write(f"{text}\n\n")

    print(f"SRT 文件已保存至: {output_srt_file_path}")


def main():
    """
    主入口：批量遍历文件夹中的音频/视频文件，并生成对应的翻译 SRT 文件。
    """
    torch.cuda.empty_cache()

    video_folder_path = "Video_to_translate"
    video_finished_path = "Generated_subtitles"
    # 获取所有 mp4 或 wav 文件
    video_files = [
        file for file in os.listdir(video_folder_path)
        if os.path.isfile(os.path.join(video_folder_path, file))
        and file.endswith(('.mp4', '.m4v'))
    ]

    # 只加载一次模型
    whisper_model, align_model, metadata = load_whisperx_model()

    for video_file in video_files:
        video_file_path = os.path.join(video_folder_path, video_file)
        video_name = os.path.splitext(video_file)[0]
        output_srt_file_path = os.path.join(video_finished_path, f"{video_name}.srt")

        generate_translated_srt(
            video_file_path,
            output_srt_file_path,
            whisper_model,
            align_model,
            metadata
        )
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
