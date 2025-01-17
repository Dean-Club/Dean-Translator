--Chinese version velow--

# What is this tool?
This tool combines based on OpenAI's **WhisperX** speech transcription tool with translation options using the **DeepL API** or local/cloud-based **large language models (LLMs)** to efficiently generate multilingual subtitles.

---

## **Target Audience**
1. International students (supports mainstream languages like English, French, German, Spanish, Japanese, Korean, etc.).
2. Subtitle teams or content creators.
3. Video reuploaders and creators requiring accurate subtitles.
4. Multilingual video creators aiming to produce subtitles in multiple languages.

---

## **Required Software**
- **Python IDE**: VSCode, PyCharm, or any IDE capable of running Python scripts.
- **LLM Software**: Recommended: LMStudio (alternatives like GPT4All are also supported).
- **Video Player**: Recommended: PotPlayer, or any video player that supports `.srt` subtitle files.

---

## **Do You Need Programming Knowledge?**
- Minimal programming knowledge is needed.
- If you're new to programming, tools like ChatGPT, Doubao, or Kimi can help guide you through the setup process.
- The steps are straightforward, so don't worry!

---

## **Configuration Options**

### **For Low-Spec Computers**
- **Recommended Devices**: Apple M-series (or later) or Windows laptops with GPUs equivalent to Nvidia 1050Ti (tested and supported).
- **Suggested Setup**: Whisper *medium* model + DeepL API.

#### **Using the DeepL API (Recommended)**
- **Limitations**: Free tier supports around 15 hours of video translation per month for continuous speech videos.
  
#### **Using Llama 3.2 3B**
- **Advantages**: Unlimited translations.
- **Disadvantages**: May occasionally produce translation errors.

---

### **For High-Spec Computers**
- **Tested Devices**: Nvidia 4060Ti GPU with 16GB VRAM for smooth performance and accurate results.

#### **Using Llama 3.1 8B (Recommended)**
- **Advantages**: High translation quality and free unlimited use.

#### **Using the ChatGPT API**
- **Advantages**: Best translation quality available.
- **Disadvantages**: Requires a paid API plan. Refer to the ChatGPT API pricing documentation.

---

## **Steps to Set Up and Use**

### **1. Register for a DeepL Account**
- Enable the API feature. Search online for setup instructions. A credit card or Mastercard is required.

---

### **2. Clone the Project from GitHub**
- Clone the repository to your local machine.

---

### **3. Set Up the Environment**
#### **For Windows:**
1. Open a terminal in the project folder.
2. Run the following commands:
   ```bash
   py -3.11 -m venv .venv
   .venv/Scripts/activate
   ```

#### **For GPU Version of PyTorch:**
- Ensure your CUDA driver matches the CUDA 12.4 version.
- Install PyTorch:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```

#### **For CPU Version of PyTorch:**
- If you don't have a GPU, install the CPU version:
   ```bash
   pip install torch torchvision torchaudio
   ```

#### **Install All Other Dependencies:**
- Use the following command to install all necessary packages:
   ```bash
   pip install -r requirements.txt
   ```
   **Note**: The installation may take some time and requires over 2.5GB of memory. Feel free to take a break during the process.

---

### **4. Place Video Files for Translation**
- Place the videos to be translated in the `Video_to_translate` folder.
- The translated subtitle files will automatically be saved in the `Generated_subtitles` folder.

---

### **5. Using the DeepL Translator**
- Open the `Autotranslate_Deepl_WhisperX.py` script.
- Replace the placeholder `deepL_API` key on line 7 with your own DeepL API key.
- Run the script. Note that the first-time setup may take longer.

---

### **6. Using a Local LLM for Translation**
1. Download and install **LMStudio**.
2. In LMStudio, download the **Llama-3.2-3B-Instruct-Q8_0** model.
3. Navigate to *Developer* → *Select Model to Load* → *Llama 3.2 3B Instruct* → *Server Port* → *Enable*.
4. Run the `Autotranslate_LLM_WhisperX.py` script.

---

### **7. View the Output**
- The subtitle files will be saved in the `Generated_subtitles` folder.
- Place the video file and subtitle file in the same folder to play the video with subtitles using software like PotPlayer.

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

# 这个工具是什么？
本工具结合了基于OpenAI 的 **WhisperX** 语音转录工具，通过 **DeepL API** 或本地/云端的大语言模型（LLMs），高效生成多语言字幕。

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

### **低配置电脑**
- **支持设备**：苹果 M 系列（或更新设备），或配备 1050Ti 显卡的 Windows 笔记本（已测试支持）。
- **推荐设置**：使用 Whisper 的 *medium* 模型搭配 DeepL API。

#### **使用 DeepL API（推荐）**
- **限制**：免费版本每月支持约 15 小时的连续语音视频翻译。

#### **使用 Llama 3.2 3B**
- **优点**：翻译次数无限制。
- **缺点**：偶尔可能会出现翻译错误。

---

### **高配置电脑**
- **测试设备**：配备 Nvidia 4060Ti 16GB 显存的设备，运行流畅且效果出色。

#### **使用 Llama 3.1 8B（推荐）**
- **优点**：翻译质量高，支持免费无限制使用。

#### **使用 ChatGPT API**
- **优点**：翻译质量最佳。
- **缺点**：需要付费，具体参考 ChatGPT API 收费说明。

---

## **设置与使用步骤**

### **1. 注册 DeepL 账号**
- 开通 API 功能。可在网上搜索详细的注册与设置教程。需要信用卡或万事达卡。

---

### **2. 从 GitHub 拉取项目**
- 将项目克隆到本地。

---

### **3. 配置环境**
#### **对于 Windows：**
1. 在项目文件夹中打开终端。
2. 输入以下命令：
   ```bash
   py -3.11 -m venv .venv
   .venv/Scripts/activate
   ```

#### **安装 GPU 版本的 PyTorch：**
- 确保你的 CUDA 驱动与 CUDA 12.4 版本匹配。
- 使用以下命令安装：
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```

#### **安装 CPU 版本的 PyTorch：**
- 如果没有 GPU，可安装 CPU 版本：
   ```bash
   pip install torch torchvision torchaudio
   ```

#### **安装所有其他依赖库：**
- 使用以下命令安装所有必要的库：
   ```bash
   pip install -r requirements.txt
   ```
   **注意**：安装过程可能较慢，需要超过 2.5GB 内存。可以趁此时间喝杯咖啡。

---

### **4. 放置视频文件**
- 将需要翻译的视频文件放入 `Video_to_translate` 文件夹。
- 翻译完成的字幕文件会自动保存到 `Generated_subtitles` 文件夹中。

---

### **5. 使用 DeepL 翻译器**
- 打开 `Autotranslate_Deepl_WhisperX.py` 脚本。
- 将第 7 行的 `deepL_API` 替换为你的 DeepL API 密钥。
- 运行脚本并耐心等待。首次运行时，配置可能需要一些时间。

---

### **6. 使用本地 LLM 进行翻译**
1. 下载并安装 **LMStudio** 软件。
2. 在 LMStudio 中下载 **Llama-3.2-3B-Instruct-Q8_0** 模型。
3. 按以下步骤操作：  
   *开发者* → *选择要加载的模型* → *Llama 3.2 3B Instruct* → *Server Port* → *开启*。
4. 运行 `Autotranslate_LLM_WhisperX.py` 脚本。

---

### **7. 查看输出结果**
- 字幕文件会保存到 `Generated_subtitles` 文件夹。
- 将视频文件和字幕文件放在同一文件夹下，使用 PotPlayer 等播放器即可播放带字幕的视频。

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
