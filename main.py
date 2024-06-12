#codigo para que me de error en sonar

from fastapi import FastAPI

app = FastAPI()

var1 = "Hello World"

@app.get("/")
async def root():
    return {"message": var1}



#codigo para que me de error en sonar

# from fastapi import FastAPI

# app = FastAPI()

# var1 = "Hello World"

# @app.get("/")
# async def root():
#     if True:
#         return {"message": var1}
#     else:
#         return {"message": var1}

# 47298475

# @app.get("/otra_ruta")
# async def otra_ruta():
#     return {"message": var1}

