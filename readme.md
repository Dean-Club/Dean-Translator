chinese version below
### What is this tool?
This tool uses the WhisperX speech transcription tool, which is based on OpenAI's Whisper, for audio transcription. It then offers translation options via the DeepL API or large language models (LLMs) running locally or in the cloud.
#### Target Audience
1. International students (supports mainstream languages like English, French, German, Spanish, Japanese, Korean, etc.)
2. Subtitle groups
3. Video reuploaders and content creators
4. Creators producing multilingual video subtitles
#### Required Software List
- **Script execution software**: IDEs capable of running Python scripts, such as VSCode or PyCharm
- **Large language model software**: Recommended: LMStudio (alternatively, GPT4All)
- **Video playback software**: Recommended: PotPlayer, or any video player that supports `.srt` subtitles
#### Do you need programming knowledge? What if you have no programming experience?
Only minimal programming knowledge is needed. If you lack experience, tools like ChatGPT, Doubao, or Kimi can help you get started. The process is straightforward, so don’t worry!
### Configuration Options
#### For Low-Spec Computers
- **Supported Devices**: Apple M-series (and later) or Windows laptops with a 1050Ti dedicated GPU (tested and supported).
- **Recommended Setup**: Use Whisper's *medium* model combined with the DeepL API.
##### Using the DeepL API (Recommended)
- **Limitations**: Free tier allows translation of approximately 15 hours of video with continuous speech per month.
##### Using Llama 3.2 3B
- **Pros**: Unlimited translations.
- **Cons**: Occasional translation errors.
#### For High-Spec Computers
- **Tested Setup**: Nvidia 4060Ti with 16GB VRAM delivers smooth performance with excellent results.
##### Using Llama 3.1 8B (Recommended)
- **Pros**: High-quality translation and free unlimited usage.
##### Using ChatGPT API
- **Pros**: Best translation quality.
- **Cons**: Paid API usage. Refer to the ChatGPT API pricing documentation for details.
### Steps:
1. **Register for a DeepL Account**
Enable the API feature. Search online for detailed guides; a credit card or Mastercard is required.
2. **Clone the Project from GitHub**
3. **Set Up the Environment**
Open the terminal and enter the following commands:
**For Windows**:
```bash
py -3.11 -m venv .venv
.venv/Scripts/activate
```
**For GPU version of PyTorch**:
- CUDA version: 12.4. Ensure your installed CUDA driver matches. Install with:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
**For CPU version of PyTorch**:
- If you don’t have a GPU, install the CPU version:
```bash
pip install torch torchvision torchaudio
```
**Note**: The installation of `torch` and related libraries requires over 2.5GB of memory and may take a while. You can grab a coffee while you wait!
**Install all other dependencies**:
```bash
pip install -r requirements.txt
```
These steps create a virtual environment and set up all necessary libraries.
4. **Place Video Files for Translation**
Put the video files to be translated in the *Video_to_translate* folder. Translated files will automatically be saved in the *Generated_subtitles* folder.
5. **Using the DeepL Translator**
- If using the DeepL API, open the *Autotranslate_Deepl_WhisperX.py* script and replace the `deepL_API` key on line 7 with your own DeepL API key. Then run the program and wait. Note that the first-time setup may take some time.
6. **Using a Local LLM for Translation**
- Download the *LMStudio* software and the *Llama-3.2-3B-Instruct-Q8_0* model.
- In LMStudio, go to *Developer* → *Select Model to Load* → *Llama 3.2 3B Instruct* → *Server Port* → *Enable*.
- Run the *Autotranslate_LLM_WhisperX.py* script.
7. **View the Output**
The subtitle files will be in the *Generated_subtitles* folder. Place the video and subtitle file in the same folder to view subtitles using software like PotPlayer.
### Q&A
#### 1. **How accurate is the translation of technical terms?**
Technical terms are generally translated well, especially when using large language models that leverage context for improved accuracy. The DeepL API may occasionally produce synonymous translation errors but performs well overall. Models with more parameters are highly recommended for best results.
#### 2. **How long does transcription take?**
Initial configuration may take some time, but subsequent translations depend on your computer's performance. Faster hardware and smaller models result in quicker transcriptions.
#### 3. **How accurate are the subtitles?**
Accuracy depends on three factors:
- **Audio quality** of the video.
- **Performance of the transcription model** (e.g., Whisper's *large-v3* offers the best accuracy but is slower).
- **Translation model quality** (larger LLMs provide better translations).
#### 4. **Supported languages?**
Nearly all languages supported by Whisper, DeepL, or large language models are supported, including Chinese, Japanese, Korean, English, French, German, and more.
#### 5. **What are the minimum hardware requirements?**
Tested on a MacBook Air M1 with 8GB RAM and an Nvidia 4060Ti 16GB GPU. Computers with performance equal to or better than the MacBook Air M1 should run smoothly.
#### 6. **What video formats are supported?**
Mainstream video and audio formats are supported. Refer to Whisper's official documentation for a complete list.

### 这个工具是什么?
字幕制作使用基于openai的Whisper的WhisperX语音转录工具进行语音转录，再选择使用DeepL的API或本地或云端的大语言模型进行翻译。
#### 面对群体
1. 各国留子，英法德西日韩等等主流语言均可
2. 字幕组
3. 视频搬运up主
4. 制作多语视频字幕的up主
#### 所需软件列表
程序脚本运行软件：VScode pycharm等能运行python程序的IDE
大语言模型软件：推荐使用LMStudio，其他诸如gpt4all也可
视频播放软件：推荐使用PotPlayer，其他能播放srt格式字幕的视频播放软件也可
#### 需要编程基础吗？完全不会编程怎么办？
需要一点点编程基础，不会也没关系，查查Chatgpt/豆包/Kimi等等也能弄明白，非常简单，不要害怕。

### 选择说明
#### 低配电脑
苹果M系列及之后电脑，windows 笔记本1050ti独立显卡亲测可用。推荐使用 Whisper的*medium*和*DeepL API*的组合。
##### 使用DeepL API（推荐）
免费额度有限量，每个月可以翻译15小时左右的课程视频（视频从头到尾都有人讲话的那种）。
##### 使用llama 3.2 3B
无限翻译，但是有时候会有翻译错误。
#### 高配电脑
笔者使用Nvidia 4060ti 16G显卡，可以流畅运行且效果很好。
##### 使用llama 3.1 8B（推荐）
推荐，翻译质量很不错，可以免费无限次使用。一般配置的
##### 使用ChatGPT API
翻译质量最高，但是API收费，详细资料参考 ChatGPT API收费说明。
### 步骤：
1. 注册一个DeepL账号，开通API功能，此步骤可以自行搜索，需要信用卡或万事达卡等。
2. 从github拉取项目
3. 在终端中输入命令 
   windows：
```
   py -3.11 -m venv .venv 
   .venv/Scripts/activate
```
	GPU版本的pytorch安装
		使用的是CUDA12.4版本，注意电脑安装的CUDA驱动版本要匹配。命令为：
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
	CPU版本的pytorch安装
		没有GPU的就使用cpu版本安装，速度略慢，命令为：
```
pip3 install torch torchvision torchaudio
```
	注意：torch等其他库的安装需要2.5G以上的内存，持续时间较长，可以去冲一杯咖啡~
	安装其他所有环境：
```
pip install -r requirements.txt
```
	以上步骤是创建虚拟环境，并配置好所有的需要的库
4. 把需要翻译的视频文件放入 *Video_to_translate* 文件夹下，翻译好的文件会自动放入*Generated_subtitles*的文件夹中
5. 如果使用本地LLM模型翻译的话，跳过这一步。如果使用deepL翻译的话，打开*Autotranslate_Deepl_WhisperX.py*程序，把程序中第7行的*deepL_API*替换为你的DeepL的API，此时可以直接点击程序运行了，程序点击运行之后，耐心等待一会儿，第一次配置的时间较长。
6. 如果使用本地LLM模型翻译的话，需要下载*LMStudio*软件，并在LM Studio中下载*Llama-3.2-3B-Instruct-Q8_0*模型，打开*开发者*-->*选择要加载的模型*-->*Llama 3.2 3B Instruct*-->*Server Port*-->*选择开启*，运行*Autotranslate_LLM_WhisperX.py*程序即可。
8. 可以看到字幕文件放在了*Generated_subtitles*文件夹下，当视频文件和这个字幕文件置于同一文件夹下，便可通过类似于Potplayer这样的软件进行播放带字幕的视频了。
### Q&A
#### 1. 专业词汇翻译效果怎么样？
大部分专业词汇翻译得非常不错，特别是当使用大语言模型的时候，能参考上下文，此时的准确度最高，如果使用deepL API的话，可能存在同义词翻译错误的问题，但总体表现良好。最推荐参数多的大语言模型。
#### 2. 转录文件时间的长短？
一次配置需要稍稍花点时间配置一下环境，配置好之后后续翻译就看电脑性能啦，电脑性能越高，转录翻译越快。还取决于选择的模型大小，模型越大，精确度越高，转录时间越长。
#### 3. 字幕文件的精确度如何？
精确度取决于三个部分，一是视频中音频的质量，二是转录模型的性能，三是翻译模型的性能。当使用whisper的*large-v3*转录模型的时候，转录的效果最好，同时需要的时间也最长，适合高精度转义，语言翻译过程相对较快。使用*medium*模型的时候综合速度和转录效果最好，性价比最高。翻译模型中，越大参数的LLM模型翻译质量越好。
#### 4. 支持语言种类？
中日韩 英法德等各种语种几乎都支持，可以这么说，只要Whisper和DeepL还有大语言模型支持的语言，本翻译器都支持。
#### 5. 电脑内存？电脑性能？
笔者使用 Macbook air m1 8G内存版和Nvidia 4060ti 16G进行测试，均可运行，可以说，性能等于或者好过Macbook air m1的电脑，均可运行。
#### 6. 什么样的视频格式？
主流视频格式，音频格式都支持，可以参考Whisper的官方说明。
