import deepl

from app import config


def get_connection() -> any:
    auth_key = config.DEEPL_API_KEY
    translator = deepl.Translator(auth_key)
    return translator


def request_translation(params: object) -> object:
    try:
        translator = get_connection()
    except Exception as e:
        return f"Error: {e}"

    usage = translator.get_usage()
    if usage.any_limit_reached:
        return "Error: request limit reached"

    result = translator.translate_text(
        params.text, source_lang=params.source_lang.value, target_lang=params.target_lang.value
    )

    return {
        "text": result.text,
        "usage": {"count": usage.character.count, "limit": usage.character.limit},
    }
