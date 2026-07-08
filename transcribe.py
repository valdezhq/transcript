import os
import time
from dotenv import load_dotenv
from faster_whisper import WhisperModel

load_dotenv()
model = WhisperModel("small", device="cpu", compute_type="int8")

input_folder = os.getenv("INPUT_PATH")
output_folder = os.getenv("OUTPUT_PATH")


os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith((".mp3", ".wav", ".m4a")):

        audio_path = os.path.join(input_folder, filename)
        print (f"Transcribing {filename}")

        start_time = time.perf_counter()

        print("Loading:", audio_path)

        segments, info = model.transcribe(
            audio_path,
            language="pt",
            vad_filter=True
        )

        text_parts = []

        for segment in segments:
            text_parts.append(segment.text.strip())

        text = " ".join(text_parts)

        elapsed = time.perf_counter() - start_time

        output_file = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved transcription to {output_file}",
            f"Transcription completed in {elapsed:.2f} s")
