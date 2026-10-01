

from controllers.projetos_controller import ProjetosController
import requests as r


class ProjetosService:
    def __init__(self, session: r.Session):
        self.session = session
        self.projetos_controller = ProjetosController(session)

    def get_all_clients(self, cookies: dict, headers: dict) -> r.Response:
        return self.projetos_controller.get_all_clients(cookies, headers)
