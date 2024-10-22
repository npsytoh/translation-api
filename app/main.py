import uvicorn
from fastapi import FastAPI
from translation import get_usage_count, request_translation

app = FastAPI()


@app.get("/translate")
async def translate():
    result = request_translation("Hello world", "EN", "JA")
    usage = get_usage_count()
    return {"text": result, "usage": usage}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
