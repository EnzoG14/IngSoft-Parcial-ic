#codigo para que me de error en sonar

from fastapi import FastAPI

app = FastAPI()

var1 = "Hello World" # Variable duplicada para simular código duplicado

@app.get("/")
async def root():
    if True:
        return {"message": var1}
    else:
        return {"message": var1}

47298475

@app.get("/otra_ruta")
async def otra_ruta():
    return {"message": var1}  # Código duplicado

