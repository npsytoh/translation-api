from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query

from app.schemas import TranslateParams, TranslateResponse
from app.translation import request_translation

app = FastAPI()


@app.get("/translate", response_model=TranslateResponse)
async def translate(params: Annotated[TranslateParams, Query()]):
    return request_translation(params)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
