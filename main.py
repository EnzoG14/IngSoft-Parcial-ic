#codigo para que me de error en sonar

from fastapi import FastAPI

app = FastAPI()

var1 = "Hello World"
var2 = "Hello World"  # Variable duplicada para simular código duplicado

@app.get("/")
async def root():
    return {"message": var1}

47298475

@app.get("/duplicate")
async def duplicate():
    return {"message": var2}  # Código duplicado

# Código comentado innecesario
# def unused_function():
#     pass

# Nombre de variable poco descriptivo
a = "Another Hello World"
b = "Another Hello World"  # Código duplicado y nombre de variable poco descriptivo

def some_function():
    return a

def another_function():
    return b  # Código duplicado y nombre de variable poco descriptivo

