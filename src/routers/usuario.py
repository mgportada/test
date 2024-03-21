from http.client import HTTPException
from typing import List, Optional
from fastapi import APIRouter, Body

from dao.usuario import UsuarioLocalDAO
from schemas import Usuario

router = APIRouter(tags=["Usuarios"])

usuario_dao = UsuarioLocalDAO()


@router.get("/usuarios", response_model=List[Usuario])
async def obtener_usuarios():
    return usuario_dao.obtener_usuarios()


@router.get("/usuarios/{id}", response_model=Usuario)
async def obtener_usuario(id: int):
    return usuario_dao.obtener_usuario(id)


@router.post("/usuarios/", response_model=dict)
async def crear_usuarios(usuarios: List[Usuario]):
    usuario_dao.agregar_usuarios(usuarios)
    return {"mensaje": f"Se han creado {len(usuarios)} usuario"}


@router.delete("/usuarios/{id}", response_model=dict)
async def eliminar_usuario(id: int):
    usuario_dao.eliminar_usuarios(id)
    return {"mensaje": "Se han ejecutado la eliminación de usuario"}


@router.put("/usuarios/{id}/actualizar-email", response_model=Usuario)
async def actualizar_email(id: int, correo_nuevo: str = Body(..., embed=True)):
    # Buscar el usuario por ID
    usuario = usuario_dao.obtener_usuario(id)

    # Si no se encuentra el usuario, devolver un error 404
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar el correo electrónico
    usuario_actualizado = usuario_dao.actualizar_correo(id, correo_nuevo)

    # Devolver el usuario actualizado
    return usuario_actualizado


@router.get("/usuarios-filter", response_model=List[Usuario])
async def filtrar_usuarios(start_year: Optional[int] = None, end_year: Optional[int] = None):
    usuarios = usuario_dao.obtener_usuarios()

    # Filtrar por año de nacimiento si se proporciona
    if start_year is not None:
        usuarios = [usuario for usuario in usuarios if start_year <= usuario.nacimiento]
    if end_year is not None:
        usuarios = [usuario for usuario in usuarios if usuario.nacimiento <= end_year]

    return usuarios
