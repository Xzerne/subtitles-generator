import wave
import json
import srt
import os
import random
from datetime import timedelta
from vosk import Model, KaldiRecognizer

# Read README.md first to see how it works !
# Path To Vosk
MODEL_PATH = "vosk-model-small-en-us-0.15" # Download from https://alphacephei.com/vosk/models

# Check if downloaded model
if not os.path.exists(MODEL_PATH):
    print(f" Model not found {MODEL_PATH}. Download from https://alphacephei.com/vosk/models")
    exit(1)

# Generate random id
def generate_random_id():
    return str(random.randint(10000, 99999)) 

# Speech recognition & SRT file generation
def transcribe_to_srt(wav_file, model_path, mode="word"):
    if not os.path.exists(wav_file):
        print(f"File {wav_file} not found")
        return
    
    print("Processing voice recognition...")

    # Generate random ID and file name
    random_id = generate_random_id()
    srt_file = f"{random_id}-XZERNE.srt"

    model = Model(model_path)
    wf = wave.open(wav_file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    subtitles = []
    index = 1
    sentence = ""
    start_time = None

    while True:
        data = wf.readframes(4000)
        if not data:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())

            if mode == "word":
                # Subtitiles each word
                for word in result.get("result", []):
                    start = timedelta(seconds=word["start"])
                    end = timedelta(seconds=word["end"])
                    subtitles.append(srt.Subtitle(index=index, start=start, end=end, content=word["word"]))
                    index += 1

            elif mode == "sentence":
                # Subtitles each sentence (movie subtitles)
                sentence = result.get("text", "").strip()
                if sentence:
                    words = result.get("result", [])
                    if words:
                        start_time = timedelta(seconds=words[0]["start"])
                        end_time = timedelta(seconds=words[-1]["end"])
                        subtitles.append(srt.Subtitle(index=index, start=start_time, end=end_time, content=sentence))
                        index += 1

    
    with open(srt_file, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    
    print(f"Created Subtitles: {srt_file}")

# WAV files to be recognized
wav_path = "your_wav_video.wav"

# Recognition mode: "word" or "sentence"
mode = "sentence"  # Or "word"

transcribe_to_srt(wav_path, MODEL_PATH, mode=mode)
