import argparse
from pathlib import Path
from utils.audio_io import record_and_save
from stt.google_stt import transcribe_wav
from translate.translator import translate_text
from tts.tts_engine import speak


def main():
    parser = argparse.ArgumentParser(description="One-shot voice → translate → speak (no FFmpeg)")
    parser.add_argument('--seconds', type=float, default=4.0, help='Record duration in seconds')
    parser.add_argument('--sr', type=int, default=16000, help='Sample rate')
    parser.add_argument('--src', type=str, default='en-US', help='Speech recognition language (e.g., en-US, hi-IN)')
    parser.add_argument('--dst', type=str, default='hi', help='Target translation language (e.g., hi, en, es)')
    parser.add_argument('--voice', type=str, default=None, help='pyttsx3 voice name contains (optional)')
    args = parser.parse_args()

    out_wav = Path('recording.wav')
    print(f"Recording {args.seconds}s… (sample_rate={args.sr})")
    record_and_save(out_wav, seconds=args.seconds, sample_rate=args.sr, channels=1)

    print("Transcribing…")
    text = transcribe_wav(str(out_wav), language=args.src)
    print("You said:", text or "[No speech detected]")

    print("Translating →", args.dst)
    translated = translate_text(text, args.dst) if text else ""
    print("Translation:", translated or "[Empty]")

    print("Speaking translation…")
    speak(translated, voice_contains=args.voice)


if __name__ == '__main__':
    main()