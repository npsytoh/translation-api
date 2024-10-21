import deepl


def request_translation(text: str, lang: str):
    auth_key = ""
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(text, target_lang=lang)
    return result.text
