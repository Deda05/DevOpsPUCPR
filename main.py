from fastapi import FastAPI
import random
from pydantic import BaseModel
app = FastAPI()

class Estudante(BaseModel):
    name: str 
    curso: str
    ativo: bool


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")

#teste comentario
@app.get("/teste1")

async def funcaoteste():
    return{"teste": True, "NumAleatorio": random.randint(0, 20000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

