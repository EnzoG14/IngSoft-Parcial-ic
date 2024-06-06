from fastapi import FastAPI

app = FastAPI()

var1="Hello World"
var2=var1
var3=var2
var4=var3
@app.get("/")
async def root():
    return {"message": var4}