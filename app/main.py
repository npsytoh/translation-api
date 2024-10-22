import uvicorn
from fastapi import FastAPI
from schemas import LanguagesEnum, TranslateResponse
from translation import get_usage_count, request_translation

app = FastAPI()


@app.get("/translate", response_model=TranslateResponse)
async def translate(text: str, source_lang: LanguagesEnum, target_lang: LanguagesEnum):
    languages = {
        "source": LanguagesEnum(source_lang).value,
        "target": LanguagesEnum(target_lang).value,
    }
    result = request_translation(text, languages)
    usage = get_usage_count()
    return {"text": result, "usage": usage}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
