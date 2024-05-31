from fastapi import FastAPI

app = FastAPI()

var1="Hello World"

@app.get("/")
async def root():
    return {"message": var1}