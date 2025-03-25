# Subtitles Generator:

Automatically generate `.srt` subtitles from `.wav` files using **Vosk Speech Recognition**.

## 🚀 Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Xzerne/subtitles-generator.git
cd subtitles-generator
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Install ffmpeg (Linux/WSL)
```sh
apt-get update && apt-get install -y ffmpeg
```
❗ Note: On Windows, download and install FFmpeg and add it to Path.
https://ffmpeg.org/download.html

## 📥 Prepare the Model
* Download a Vosk model from: alphacephei.com/vosk/models

* Extract it into the directory vosk-model-small-en-us-0.15/
(Or use a different model based on your language)

## How to Use
### 1️⃣ Convert .mp3 to .wav (if needed)
```sh
ffmpeg -i your_input_mp3.mp3 -ar 16000 -ac 1 your_output_wav.wav
```

### 2️⃣ Run the Script to Generate Subtitles
```sh
python main.py
```
✅ Run the script and get automatic subtitles! 🚀

