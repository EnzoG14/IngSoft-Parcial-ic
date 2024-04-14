from fastapi import FastAPI

app = FastAPI()

var="Hello Worl"

@app.get("/")
async def root():
    return {"message": var}