from fastapi import FastAPI

app = FastAPI()

var="hola mundo"

@app.get("/")
async def root():
    return {"message": var}