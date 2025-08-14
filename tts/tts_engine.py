import pyttsx3
from typing import Optional
import threading

_engine = None

def get_engine(rate: Optional[int] = None, voice_contains: Optional[str] = None):
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        # Default tweaks
        if rate is not None:
            _engine.setProperty('rate', rate)
        if voice_contains:
            for v in _engine.getProperty('voices'):
                if voice_contains.lower() in (v.name or '').lower():
                    _engine.setProperty('voice', v.id)
                    break
    return _engine


def speak(text, rate=150, voice_contains=None):
    engine = get_engine(rate=rate, voice_contains=voice_contains)
    engine.say(text)
    threading.Thread(target=engine.runAndWait).start()
    
    