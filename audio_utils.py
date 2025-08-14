import os
import subprocess
from pathlib import Path
import numpy as np
import sounddevice as sd
from scipy.io import wavfile


FFMPEG_PATH = r"C:\Users\hi\ffmpeg\bin\ffmpeg.exe"

def record_to_numpy(seconds: float = 4.0, sample_rate: int = 16000, channels: int = 1, dtype='int16') -> np.ndarray:
    """Record audio from the default microphone into a NumPy array.
    Returns shape (samples, channels) for stereo; for mono, (samples, 1).
    """
    if channels not in (1, 2):
        raise ValueError("channels must be 1 (mono) or 2 (stereo)")

    frames = int(seconds * sample_rate)
    audio = sd.rec(frames, samplerate=sample_rate, channels=channels, dtype=dtype)
    sd.wait()
    return audio


def save_wav(path: str | Path, sample_rate: int, audio_np: np.ndarray) -> Path:
    path = Path(path)
    # If int dtype, write directly; if float, scale to int16
    if audio_np.dtype.kind == 'f':
        audio_np = np.clip(audio_np, -1.0, 1.0)
        audio_np = (audio_np * 32767).astype(np.int16)
    wavfile.write(path, sample_rate, audio_np)
    return path


def record_and_save(path: str | Path, seconds: float = 4.0, sample_rate: int = 16000, channels: int = 1) -> Path:
    audio = record_to_numpy(seconds=seconds, sample_rate=sample_rate, channels=channels, dtype='int16')
    return save_wav(path, sample_rate, audio)


# 🔹 Example: ffmpeg ka use karke WAV ko MP3 me convert karna
def convert_to_mp3(input_wav: str, output_mp3: str):
    subprocess.run([FFMPEG_PATH, "-i", input_wav, output_mp3], check=True)


if __name__ == "__main__":
    wav_file = "output.wav"
    record_and_save(wav_file)
    print(f"Audio saved: {wav_file}")

    # Example: WAV to MP3
    mp3_file = "output.mp3"
    convert_to_mp3(wav_file, mp3_file)
    print(f"Converted to: {mp3_file}")
