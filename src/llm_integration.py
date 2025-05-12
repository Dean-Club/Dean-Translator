import requests
from config import LLM_API_URL, LLM_MODEL

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