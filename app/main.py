from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import TranslateParams, TranslateResponse
from app.translation import request_translation

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/translate", response_model=TranslateResponse)
async def translate(params: Annotated[TranslateParams, Query()]):
    return request_translation(params)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
