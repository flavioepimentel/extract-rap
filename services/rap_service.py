from typing import Optional
from controllers.auth_controller import AuthController
from controllers.raps_controller import RapController
from bs4 import BeautifulSoup as bs
import requests as r


class RapService:

    def __init__(self, session: r.Session):
        self.session = session
        self.rap_controller = RapController(self.session)
        self.last_response: Optional[r.Response] = None

    def get_categorias_rap(self, cookies, headers):
        return self.rap_controller.get_categorias_rap(cookies, headers)

    def get_tipos_rap(self, cookies, headers):
        return self.rap_controller.get_tipos_rap(cookies, headers)

    def post_rap(self, cookies, headers: str, projeto_id: int, json_data: dict) -> r.Response:
        return self.rap_controller.post_rap(cookies, headers, projeto_id, json_data)

    def get_all_raps(self, cookies: dict, headers: dict, inicio: str, final: str, usuario: str | None = None, cliente: str | None = None, categoria: str | None = None, tipo: str | None = None):
        return self.rap_controller.get_all_raps(cookies, headers, inicio, final, usuario, cliente, categoria, tipo)
