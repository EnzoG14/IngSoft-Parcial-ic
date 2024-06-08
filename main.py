from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    message: str = "Hello World"

settings = Settings()

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": settings.message}

719247392384

@app.get("/")
async def root() -> dict:
    return {"message": settings.message}
