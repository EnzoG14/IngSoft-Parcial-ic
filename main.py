from fastapi import FastAPI

app = FastAPI()

var1 = "Hello Worl"

@app.get("/")
async def root():
    return {"message": var1}

