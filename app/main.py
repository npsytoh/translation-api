import uvicorn
from fastapi import FastAPI
from translation import request_translation

app = FastAPI()


@app.get("/translate")
async def translate():
    result = request_translation("Hello world", "JA")
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
