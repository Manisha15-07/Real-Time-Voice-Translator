import io
from pathlib import Path
import streamlit as st
from audio_utils import record_and_save
from stt.whisper_stt import transcribe_wav 
from translate.translator import translate_text
from tts.tts_engine import speak

st.set_page_config(page_title="Real-time Voice Translation", page_icon="🗣️", layout="centered")

st.title("🗣️ Real-time Voice Translation")
st.caption("Record → Transcribe → Translate → Speak")

with st.sidebar:
    st.header("Settings")
    seconds = st.slider("Record duration (s)", 1.0, 15.0, 4.0, 0.5)
    sr = st.select_slider("Sample rate", options=[16000, 22050, 24000, 32000], value=16000)
    src = st.selectbox("Speech language (STT)", [
        'en-US','en-IN','hi-IN','bn-IN','mr-IN','te-IN','ta-IN','gu-IN','kn-IN','ml-IN','pa-IN'
    ], index=0)
    dst = st.selectbox("Target language (translation)", [
        'hi','en','bn','mr','te','ta','gu','kn','ml','pa','ur','es','fr','de','zh-cn'
    ], index=0)
    voice_hint = st.text_input("TTS voice contains (optional)", value="")

st.write("Click **Record** and speak a short sentence.")

col1, col2, col3 = st.columns(3)
rec_btn = col1.button("🎙️ Record")

placeholder_audio = st.empty()
placeholder_text = st.empty()
placeholder_trans = st.empty()

if rec_btn:
    out_wav = Path('st_record.wav')
    with st.spinner("Recording…"):
        record_and_save(out_wav, seconds=seconds, sample_rate=sr, channels=1)
    st.success("Recording complete.")

    # Playback in app
    with open(out_wav, 'rb') as f:
        wav_bytes = f.read()
    placeholder_audio.audio(wav_bytes, format='audio/wav')

    with st.spinner("Transcribing…"):
        # Map UI-selected language to Whisper-compatible code
        lang_map = {
            'en-US': 'en',
            'en-IN': 'en',
            'hi-IN': 'hi',
            'bn-IN': 'bn',
            'mr-IN': 'mr',
            'te-IN': 'te',
            'ta-IN': 'ta',
            'gu-IN': 'gu',
            'kn-IN': 'kn',
            'ml-IN': 'ml',
            'pa-IN': 'pa'
        }
        whisper_lang = lang_map.get(src, None)  # None = auto-detect
        text = transcribe_wav(str(out_wav), language=whisper_lang)
    placeholder_text.info(f"**Transcription:** {text or '[No speech detected]'}")

    if text:
        with st.spinner("Translating…"):
            translated = translate_text(text, dst)
        placeholder_trans.success(f"**Translation ({dst}):** {translated}")

        # Speak (local audio output through system speakers)
        speak(translated, voice_contains=voice_hint or None)
