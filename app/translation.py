import config
import deepl


def get_connection():
    auth_key = config.DEEPL_API_KEY
    translator = deepl.Translator(auth_key)
    return translator


def request_translation(text: str, source_lang: str, target_lang: str):
    try:
        translator = get_connection()
    except Exception as e:
        return f"Error: {e}"

    usage = translator.get_usage()
    if usage.any_limit_reached:
        return "Error: request limit reached"

    result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    return result.text


def get_usage_count():
    translator = get_connection()
    usage = translator.get_usage()
    return {"character": {"count": usage.character.count, "limit": usage.character.limit}}
