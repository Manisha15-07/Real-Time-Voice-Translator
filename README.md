# Real-Time Voice Translator

A modular and scalable Python Streamlit app that records live speech, transcribes it using **OpenAI Whisper**, translates the text into a target language, and speaks it aloud via offline TTS—no FFmpeg dependency needed.

##  Features :
- **Speech-to-Text (STT):** Powered by Whisper with automatic language detection.  
- **Translation:** Uses `deep-translator` (Google Translate backend).  
- **Text-to-Speech (TTS):** Offline audio output with `pyttsx3`, running asynchronously.  
- **Web UI:** Built with Streamlit for quick testing and demonstration.

##  Project Structure:

Real-Time-Voice-Translator/
│
├── app.py # Main Streamlit application
├── audio_utils.py # Custom audio recording helper
├── stt/
│ └── whisper_stt.py # Whisper-based speech recognition
├── translate/
│ └── translator.py # Language translation module
├── tts/
│ └── tts_engine.py # Text-to-speech engine
├── cli_translate.py # One-shot CLI recorder (optional)
├── requirements.txt # Project dependencies
└── README.md # This documentation

###  How to Use:
1.Adjust Record duration and Sample rate as needed.
2.Select the source speech language (e.g., hi-IN for Hindi).
3.Choose a target translation language (e.g., en for English).
4.(Optional) Use the TTS voice hint to select a particular system voice.

#### SCREENSHOTS:
