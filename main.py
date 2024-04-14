from fastapi import FastAPI

app = FastAPI()

var="Hello World"

@app.get("/")
async def root():
    return {"message": var}