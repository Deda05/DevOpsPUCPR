from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#teste comentario
@app.get("/teste1")
async def funcaoteste():
    return{"teste": True, "NumAleatorio": random.randint(0, 1000)}


#fastapi dev main.py