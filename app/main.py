from enum import Enum

import uvicorn
from fastapi import FastAPI
from translation import get_usage_count, request_translation

app = FastAPI()


class Languages(str, Enum):
    JA = "JA"
    EN = "EN"
    KO = "KO"
    ZH = "ZH"
    FR = "FR"
    IT = "IT"
    RU = "RU"
    DE = "DE"


@app.get("/translate")
async def translate(text: str, source_lang: Languages, target_lang: Languages):
    languages = {"source": Languages(source_lang).value, "target": Languages(target_lang).value}
    result = request_translation(text, languages)
    usage = get_usage_count()
    return {"text": result, "usage": usage}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
