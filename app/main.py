from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query

from app.schemas import TranslateParams, TranslateResponse
from app.translation import get_usage_count, request_translation

app = FastAPI()


@app.get("/translate", response_model=TranslateResponse)
async def translate(params: Annotated[TranslateParams, Query()]):
    languages = {
        "source": params.source_lang.value,
        "target": params.target_lang.value,
    }
    result = await request_translation(params.text, languages)
    usage = await get_usage_count()
    return {"text": result, "usage": usage}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
