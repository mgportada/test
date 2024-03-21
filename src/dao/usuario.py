from typing import List, Optional
from schemas import Usuario


class UsuarioLocalDAO:
    def __init__(self):
        self.usuarios = [
            Usuario(id=1, nombre="Manuel", correo="manuel@iesportada.org", nacimiento=2000),
            Usuario(id=2, nombre="Lourdes", correo="lourdes@iesportada.org", nacimiento=2023)
        ]

    def obtener_usuarios(self) -> List[Usuario]:
        return [usuario for usuario in self.usuarios]

    def obtener_usuario(self, id) -> Optional[Usuario]:
        match = [usuario for usuario in self.usuarios if usuario.id == id]
        if match:
            return match[0]
        else:
            return None

    def agregar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def agregar_usuarios(self, usuarios: List[Usuario]):
        self.usuarios.extend(usuarios)

    def eliminar_usuarios(self, id: int):
        self.usuarios = [usuario for usuario in self.usuarios if usuario.id != id]

    def actualizar_correo(self, id: int, correo: str) -> Optional[Usuario]:
        match_user = [usuario for usuario in self.usuarios if usuario.id == id]
        if match_user:
            match_user[0].correo = correo
            return match_user[0]
        else:
            return None
