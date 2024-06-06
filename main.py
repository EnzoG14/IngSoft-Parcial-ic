from fastapi import FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    message: str = "Hello World"

settings = Settings()

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": settings.message}