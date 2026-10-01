from typing import Optional
import requests as r
from bs4 import BeautifulSoup as bs


class ProjetosController:

    def __init__(self, session: r.Session):
        self.session = session

    def get_projetos(self, cookies: dict, headers: dict) -> r.Response:
        return self.session.get('http://wisetech.dyndns.org:8000/usuario/projetos', cookies=cookies, headers=headers, verify=False)

    def get_all_clients(self, cookies: dict, headers: dict) -> r.Response:
        return self.session.get('http://wisetech.dyndns.org:8000/usuario/clientes', cookies=cookies, headers=headers, verify=False)
