import os
import time
import whisper

model = whisper.load_model("base")

input_folder = r"\Transcription\audios"
output_folder = r"\Transcription\transcriptions"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith((".mp3", ".wav", ".m4a")):
        audio_path = os.path.join(input_folder, filename)
        print (f"Transcribing {filename}")

        start_time = time.time()
        transcript = model.transcribe(audio_path)
        duration = time.time() - start_time

        text = transcript["text"].strip()
        text = text[0].upper() + text[1:] if text else text

        output_file = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Transcription saved to {output_file}, duration of transcription: {duration:.2f} seconds")
