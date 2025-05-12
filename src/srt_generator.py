import torch
import whisperx
from llm_integration import local_translate_with_memory

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
