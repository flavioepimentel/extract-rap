

from controllers.usuarios_controller import UsuariosController
import requests as r


class UsuariosService:
    def __init__(self, session: r.Session):
        self.session = session
        self.usuarios_controller = UsuariosController(session)

    def get_all_users(self, cookies: dict, headers: dict) -> r.Response:
        return self.usuarios_controller.get_usuarios(cookies, headers)
