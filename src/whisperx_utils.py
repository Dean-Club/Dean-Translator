from config import WHISPER_MODEL_NAME, WHISPER_COMPUTE_TYPE, WHISPER_ASR_OPTIONS, ALIGN_MODEL_LANGUAGE_CODE
import whisperx
import torch

def load_whisperx_model(whisper_model_name,
                        whisper_compute_type,
                        whisper_asr_options,
                        align_model_language_code):
    """
    加载 WhisperX 模型及对齐模型，返回 (whisper_model, align_model, metadata)。
    """
    device_type = "cuda" if torch.cuda.is_available() else "cpu"
    # 加载 Whisper 模型
    whisper_model = whisperx.load_model(
        whisper_model_name,
        device_type,
        compute_type=whisper_compute_type,
        asr_options=whisper_asr_options
    )
    # 加载对齐模型
    align_model, metadata = whisperx.load_align_model(
        language_code=align_model_language_code,
        device=device_type
    )
    return whisper_model, align_model, metadata