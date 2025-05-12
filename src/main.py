import os
import torch
from whisperx_utils import load_whisperx_model
from srt_generator import generate_translated_srt
from config import input_video_folder_path, output_video_folder_path

def main(
    input_video_folder_path,
    output_video_folder_path,
    whisper_model_name,
    whisper_compute_type,
    whisper_asr_options,
    align_model_language_code,
    llm_model_name  # ✅ 新增参数
):
    print("[DEBUG] 使用 LLM 模型：", llm_model_name)
    torch.cuda.empty_cache()

    video_files = [
        file for file in os.listdir(input_video_folder_path)
        if os.path.isfile(os.path.join(input_video_folder_path, file))
        and file.endswith(('.mp4', '.m4v'))
    ]

    # ✅ 将配置参数传给模型加载函数（你需在 whisperx_utils 中相应修改）
    whisper_model, align_model, metadata = load_whisperx_model(
        whisper_model_name,
        whisper_compute_type,
        whisper_asr_options,
        align_model_language_code
    )

    for video_file in video_files:
        video_file_path = os.path.join(input_video_folder_path, video_file)
        video_name = os.path.splitext(video_file)[0]
        output_srt_file_path = os.path.join(output_video_folder_path, f"{video_name}.srt")

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