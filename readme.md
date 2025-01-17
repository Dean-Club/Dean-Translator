# What is this tool?
This tool combines OpenAI's **WhisperX** speech transcription tool with translation options using the **DeepL API** or local/cloud-based **large language models (LLMs)** to efficiently generate multilingual subtitles.

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
