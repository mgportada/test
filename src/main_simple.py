import os
from typing import List

import uvicorn
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi import FastAPI

app = FastAPI()

host = os.environ.get("host", "localhost")
port = int(os.environ.get("port", "8000"))

from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "correo": self.correo}

lista_usuarios = [
    Usuario(id=1, nombre="Manuel", correo="manuelgarces@iesportada.org"),
    Usuario(id=2, nombre="Manuel2", correo="manuelgarces2@iesportada.org")
    ]


@app.get("/usuarios", response_model=List[Usuario])
async def obtener_usuarios():
    return lista_usuarios


@app.get("/ui/home", response_class=HTMLResponse)
async def read_home():
    htmldireccion = "./html/juego.html"
    return FileResponse(htmldireccion)


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")


@app.get("/demo")
async def demo_function():
    return {"name": "Manuel"}


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
