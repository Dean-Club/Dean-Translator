# English version
(Chinese version below)
(This tool is developed by Student from Friedlich Alexander University Erlangen-Nuernberg, was inspired by FAUtv)

# What is this tool?

This tool combines the OpenAI-based **WhisperX** speech transcription tool with **DeepL API** or local/cloud-based large language models (LLMs) to efficiently generate multilingual subtitles.  
WhisperX: https://github.com/m-bain/whisperX

---

## **Target Audience**
1. International students (supports mainstream languages such as English, French, German, Spanish, Japanese, Korean, etc.).
2. Subtitle teams and related professionals.
3. Video content creators and uploaders.
4. Creators who need to make multilingual subtitles for videos.

---

## **Required Software**
- **Python IDE**: An IDE that supports running Python scripts, such as VSCode or PyCharm.
- **LLM Software**: Recommended to use LMStudio (also supports GPT4All and other alternatives).
- **Video Player**: Recommended to use PotPlayer or any video player that supports the .srt subtitle format.

---

## **Do you need programming experience?**
- Only basic programming knowledge is required.
- If you have no programming experience, you can quickly get started with tools like ChatGPT, Doubao, or Kimi.
- The steps are simple and easy to follow, no worries!
---
## **Configuration Options**

#### **Recommended Speech Recognition (for all configurations)**
- **Whisper's *medium* model**  
  ➡️ Specially used for recognizing speech in videos, suitable for all configurations.

---

#### **Low-Configuration Computers**
- **Supported devices**:
  - 🍏 Apple M-series (or newer devices)
  - 💻 Windows laptop with a 1050Ti GPU (tested and supported)

- **Optional settings**:
  - Use **DeepL API**  
    ➡️ The free version supports approximately 15 hours of continuous speech-to-video translation per month. (Recommended)
  - Use **Llama 3.2 3B model**  
    ➡️ Unlimited translation usage, but occasional translation errors may occur.

---

#### **High-Configuration Computers**
- **Tested device**:
  - 💻 Device with **Nvidia 4060Ti 16GB VRAM**, smooth performance and excellent results.

- **Optional settings**:
  - Use **Llama 3.1 8B model** (Recommended)  
    ➡️ High translation quality, supports unlimited free usage.
  - Use **ChatGPT API**  
    ➡️ Best translation quality, but requires payment. For pricing details, refer to [ChatGPT API Pricing](https://chatgpt.com/#pricing).

## **Setup and Usage Steps**

### **1. Clone the project from GitHub**
- Clone the project to your local machine.

---

### **2. Configure the environment (Windows OS)**
1. Use VSCode and open the terminal in the project folder.
2. Enter the following commands:
   ```bash
   py -3.11 -m venv .venv
   .venv/Scripts/activate

3. Install the GPU version of PyTorch:
- Make sure the CUDA drivers are installed.
- Use the following command to install:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```
- If you don’t have a GPU, install the CPU version:
   ```bash
   pip install torch torchvision torchaudio
   ```
4. Install all other required dependencies:
- Use the following command to install all necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```
   **Note**: The installation process may take some time and require more than 2.5GB of storage space. You can grab a cup of coffee while it installs.

---

### **3. Place the video files**
- Put the video files you need to translate into the `Video_to_translate` folder.
- The translated subtitle files will be automatically saved in the `Generated_subtitles` folder.

---

### **4. Start the translation**
#### **Using DeepL API**
1. Open the `Autotranslate_Deepl_WhisperX.py` script.
2. Replace the `deepL_API` in line 7 with your DeepL API key.
3. Run the script and be patient. The first run may take some time to configure.

---

#### **Using Local LLM**
1. Download and install LMStudio software.
2. Download the Llama-3.2-3B-Instruct-Q8_0 model in LMStudio.
3. Follow these steps:
   Developer → Choose the model to load → Llama 3.2 3B Instruct → Setting → Check Server Port → Enable CORS.
4. Modify the `Autotranslate_LLM_WhisperX.py` script and set the `LLM_MODEL` variable to the model name you downloaded in LMStudio.
5. Run the `Autotranslate_LLM_WhisperX.py` script.

---

### **5. Check the output**
- The subtitle files will be saved in the `Generated_subtitles` folder.
- Put the video file and subtitle file in the same folder and play the video with subtitles using PotPlayer or any compatible player.

---

---
## **Q&A Installation Issues**
### **1. Some warnings can be ignored**
   ```
   INFO:speechbrain.utils.quirks:Applied quirks (see `speechbrain.utils.quirks`): [disable_jit_profiling, allow_tf32]
   INFO:speechbrain.utils.quirks:Excluded quirks specified by the `SB_DISABLE_QUIRKS` environment (comma-separated list): []
   No language specified, language will be first be detected for each audio file (increases inference time).
   Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.5.0.post0. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint D:\Dean-Translator\.venv\Lib\site-packages\whisperx\assets\pytorch_model.bin`
   Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
   Model was trained with torch 1.10.0+cu102, yours is 2.5.1+cu124. Bad things might happen unless you revert torch to 1.x.
   ```
### **2. Unable to install models after installing LMStudio**
   You can try this tool to [fix the script](https://github.com/yuanyang749/lm-studio-fix)  
   Or manually modify the script.

---

## **Q&A**

### **1. How accurate is the translation of technical terms?**
- Large language models generally produce highly accurate translations by leveraging context. 
- The DeepL API is reliable, though it may occasionally misinterpret synonyms.

---

### **2. How long does transcription take?**
- After initial setup, transcription time depends on your hardware and model choice.
- Higher-performance computers and smaller models reduce processing time.

---

### **3. How accurate are the subtitles?**
- Accuracy depends on:
  - **Audio quality**: Clearer audio results in better transcriptions.
  - **Transcription model performance**: Whisper's *large-v3* model provides the highest accuracy.
  - **Translation model quality**: Larger LLMs produce superior translations.

---

### **4. Supported languages?**
- This tool supports almost all languages supported by Whisper, DeepL, and large language models, including Chinese, Japanese, Korean, English, French, German, and more.

---

### **5. What are the minimum hardware requirements?**
- Tested on a MacBook Air M1 (8GB RAM) and an Nvidia 4060Ti GPU. Any computer with similar or better performance should work smoothly.

---

### **6. What video formats are supported?**
- Most mainstream video and audio formats are supported. Refer to Whisper's official documentation for more details.

---

# 中文版
(这个工具由埃尔朗根-纽伦堡大学的学生开发，受到FAUtv的启发)
# 这个工具是什么？
本工具结合了基于OpenAI 的 **WhisperX** 语音转录工具，通过 **DeepL API** 或本地/云端的大语言模型（LLMs），高效生成多语言字幕。
WhisperX：https://github.com/m-bain/whisperX

---

## **适用人群**
1. 国际学生（支持英语、法语、德语、西班牙语、日语、韩语等主流语言）。
2. 字幕组及相关从业者。
3. 视频搬运者及内容创作者。
4. 需要制作多语言视频字幕的创作者。

---

## **所需软件**
- **Python IDE**：支持运行 Python 脚本的 IDE，例如 VSCode 或 PyCharm。
- **LLM 软件**：推荐使用 LMStudio（也支持 GPT4All 等其他选择）。
- **视频播放器**：推荐使用 PotPlayer，或任何支持 `.srt` 字幕格式的视频播放器。

---

## **需要编程基础吗？**
- 仅需非常基础的编程知识。
- 如果没有编程经验，可以借助 ChatGPT、豆包或 Kimi 等工具快速入门。
- 步骤简单易懂，无需担心！

---
## **配置选项**

---

#### **语音识别推荐（适用于所有配置）**
- **Whisper 的 *medium* 模型**  
  ➡️ 专门用于识别视频中的语音，适用于所有配置。

---

#### **低配置电脑**
- **支持设备**：
  - 🍏 苹果 M 系列（或更新的设备）
  - 💻 配备 1050Ti 显卡的 Windows 笔记本（已测试支持）
  
- **可选设置**：
  - 使用 **DeepL API**  
    ➡️ 免费版每月支持约 15 小时的连续语音视频翻译。（推荐）
  - 使用 **Llama 3.2 3B 模型**  
    ➡️ 翻译次数无限制，但偶尔会出现翻译错误。

---

#### **高配置电脑**
- **测试设备**：
  - 💻 配备 **Nvidia 4060Ti 16GB 显存** 的设备，运行流畅且效果出色。
  
- **可选设置**：
  - 使用 **Llama 3.1 8B 模型**（推荐）  
    ➡️ 翻译质量高，支持免费无限制使用。
  - 使用 **ChatGPT API**  
    ➡️ 翻译质量最佳，但需要付费，具体参考 [ChatGPT API 收费说明](https://chatgpt.com/#pricing)。


## **设置与使用步骤**

### **1. 从 GitHub 拉取项目**
- 将项目克隆到本地。

---

### **2. 配置环境（Windows操作系统）**
1. 使用 VScode，在项目文件夹中打开终端。
2. 输入以下命令：
   ```bash
   py -3.11 -m venv .venv
   .venv/Scripts/activate
   ```
3. 安装 GPU 版本的 PyTorch：
- 确保已安装 CUDA 驱动。
- 使用以下命令安装：
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```
- 如果没有 GPU，可安装 CPU 版本：
   ```bash
   pip install torch torchvision torchaudio
   ```
4. 安装所有其他依赖库：
- 使用以下命令安装所有必要的库：
   ```bash
   pip install -r requirements.txt
   ```
   **注意**：安装过程可能较慢，需要超过 2.5GB 存储空间。可以趁此时间喝杯咖啡。

---

### **3. 放置视频文件**
- 将需要翻译的视频文件放入 `Video_to_translate` 文件夹。
- 翻译完成的字幕文件会自动保存到 `Generated_subtitles` 文件夹中。

---

### **4. 开始翻译**
#### **使用 DeepL API**
1. 打开 `Autotranslate_Deepl_WhisperX.py` 脚本。
2. 将第 7 行的 `deepL_API` 替换为你的 DeepL API 密钥。
3. 运行脚本并耐心等待。首次运行时，配置可能需要一些时间。

---

#### **使用本地 LLM**
1. 下载并安装 **LMStudio** 软件。
2. 在 LMStudio 中下载 **Llama-3.2-3B-Instruct-Q8_0** 模型。
3. 按以下步骤操作：  
   *开发者* → *选择要加载的模型* → *Llama 3.2 3B Instruct* → *Setting* → *检查 Server Port* → *启用 CORS*。
4. 修改 `Autotranslate_LLM_WhisperX.py` 脚本中的 `LLM_MODEL` 变量为在 LMStudio 中下载的模型名字。
5. 运行 `Autotranslate_LLM_WhisperX.py` 脚本。

---

### **5. 查看输出结果**
- 字幕文件会保存到 `Generated_subtitles` 文件夹。
- 将视频文件和字幕文件放在同一文件夹下，使用 PotPlayer 等播放器即可播放带字幕的视频。
仓库中提供了示例视频‘2020S-Qiuqing-Tai-Tiktok.mp4’，可以供测试参考，此外在字幕生成文件夹中提供了多种生成的翻译的字幕文件，可以参考翻译效果。
---
## **Q&A 安装问题**
### **1. 有一些警告可以忽略**
```
INFO:speechbrain.utils.quirks:Applied quirks (see `speechbrain.utils.quirks`): [disable_jit_profiling, allow_tf32]
INFO:speechbrain.utils.quirks:Excluded quirks specified by the `SB_DISABLE_QUIRKS` environment (comma-separated list): []
No language specified, language will be first be detected for each audio file (increases inference time).
Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.5.0.post0. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint D:\Dean-Translator\.venv\Lib\site-packages\whisperx\assets\pytorch_model.bin`
Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
Model was trained with torch 1.10.0+cu102, yours is 2.5.1+cu124. Bad things might happen unless you revert torch to 1.x.
```
### **2. 安装LMStudio后不能安装模型**
可以试试这个工具[修改脚本](https://github.com/yuanyang749/lm-studio-fix)
或者手动修改

---

## **Q&A 常见问题**

### **1. 专业术语翻译准确吗？**
- 使用大语言模型时，凭借上下文理解能力，专业术语翻译非常准确。
- 使用 DeepL API 时，可能会偶尔出现同义词翻译错误，但整体表现优秀。推荐使用参数较大的模型以提升翻译质量。

---

### **2. 转录需要多长时间？**
- 初次配置可能稍耗时间。之后，转录和翻译的速度主要取决于电脑性能。
- 配置越高，模型越小，处理时间越快。

---

### **3. 字幕的精确度如何？**
- 精确度取决于以下三点：
  1. **音频质量**：音频越清晰，转录越准确。
  2. **转录模型性能**：如使用 Whisper 的 *large-v3* 模型，转录效果最佳，但速度较慢。
  3. **翻译模型质量**：参数更多的 LLM 模型翻译效果更好。

---

### **4. 支持哪些语言？**
- 本工具支持 Whisper、DeepL 和大语言模型所支持的所有语言，包括中文、日语、韩语、英语、法语、德语等。

---

### **5. 最低硬件要求是什么？**
- 经测试，在 MacBook Air M1（8GB RAM）和 Nvidia 4060Ti（16GB 显存）上运行流畅。
- 性能不低于 MacBook Air M1 的设备基本都能运行。

---

### **6. 支持哪些视频格式？**
- 支持大多数主流视频和音频格式。详情可参考 Whisper 的官方文档。

---
