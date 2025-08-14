# stt/whisper_stt.py
import whisper

# Load Whisper model once (choose: "tiny", "base", "small", "medium", "large")
# "small" is a good speed-accuracy balance
model = whisper.load_model("small")

def transcribe_wav(path: str, language: str = None) -> str:
    """
    Transcribes a WAV file using Whisper STT.
    Automatically detects language if not provided.
    
    :param path: Path to WAV audio file
    :param language: Optional language code (e.g., 'en', 'hi', 'fr')
    :return: Transcribed text as a string
    """
    print(f"[INFO] Transcribing audio: {path}")
    result = model.transcribe(path, language=language)
    
    detected_lang = result.get("language", "unknown")
    text = result.get("text", "").strip()

    print(f"[INFO] Detected language: {detected_lang}")
    print(f"[INFO] Transcription: {text}")

    return text
