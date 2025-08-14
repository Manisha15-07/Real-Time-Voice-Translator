from deep_translator import GoogleTranslator

# List of supported languages (ISO codes)
SUPPORTED = {
    "en": "english",
    "hi": "hindi",
    "fr": "french",
    "es": "spanish",
    "de": "german",
    "ja": "japanese",
    "zh-cn": "chinese (simplified)"
}

def translate_text(text, src_lang="auto", dest_lang="en"):
    """
    Translate text from one language to another using GoogleTranslator.
    :param text: input string
    :param src_lang: source language code (e.g., 'en', 'hi', or 'auto')
    :param dest_lang: target language code (e.g., 'en', 'hi')
    :return: translated string
    """
    try:
        # Ensure language codes are lowercase
        src_lang = src_lang.lower()
        dest_lang = dest_lang.lower()

        # Map UI input to valid codes (if needed)
        if src_lang in SUPPORTED:
            src_lang = src_lang
        elif src_lang != "auto":
            raise ValueError(f"Unsupported source language: {src_lang}")

        if dest_lang not in SUPPORTED:
            raise ValueError(f"Unsupported target language: {dest_lang}")

        translator = GoogleTranslator(source=src_lang, target=dest_lang)
        translated = translator.translate(text)

        # Debug check
        if translated.strip() == text.strip():
            return f"(No change) {translated}"

        return translated

    except Exception as e:
        return f"Translation error: {e}"
