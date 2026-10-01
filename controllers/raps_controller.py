import datetime
from typing import Optional
import requests as r
from bs4 import BeautifulSoup as bs
import urllib.parse

LOGIN_URL = "http://wisetech.dyndns.org:8000/login"


class RapController:

    def __init__(self, session: r.Session):
        self.session = session
        self.headers = None
        self.cookies = None
        self.last_response: Optional[r.Response] = None

    def get_categorias_rap(self, cookies, headers):
        return self.session.get(
            'http://wisetech.dyndns.org:8000/empresas/1/categorias-rap',
            cookies=cookies,
            headers=headers,
            verify=False,
        )

    def get_tipos_rap(self, cookies, headers):
        return self.session.get('http://wisetech.dyndns.org:8000/empresas/1/tipos-rap', cookies=cookies, headers=headers, verify=False)

    def post_rap(self, cookies, headers: str, projeto_id: int, json_data: dict) -> r.Response:
        return self.session.post(
            f'http://wisetech.dyndns.org:8000/empresas/1/projetos/{projeto_id}/raps',
            cookies=cookies,
            headers=headers,
            json=json_data,
            verify=False,
        )

    def get_all_raps(self, cookies: dict, headers: dict, /, inicio: str, final: str, usuario: str | None = None, cliente: str | None = None, categoria: str | None = None, tipo: str | None = None):
        """
        Retorna todos os raps criados no periodo mencionado.
        - inicio: Data de início no formato YYYY-MM-DD
        - final: Data de fim no formato YYYY-MM-DD
        - usuario: Nome do usuário (opcional)
        - cliente: Nome do cliente (opcional)   
        - categoria: Sigla da categoria do rap (opcional) 
        - tipo: Sigla do tipo do rap (opcional)
        """
        categoria = \
            "%22" + urllib.parse.quote(categoria.strip()) + "%22" \
            if categoria else ""

        tipo = \
            "%22" + urllib.parse.quote(tipo.strip()) + "%22" \
            if tipo else ""

        cliente = \
            "%22" + urllib.parse.quote(cliente.strip()).replace("%20", "+") + "%22" \
            if cliente else ""

        usuario = \
            "%22" + urllib.parse.quote(usuario.strip()).replace("%20", "+") + "%22" \
            if usuario else ""

        return self.session.get(
            f'http://wisetech.dyndns.org:8000/usuario/raps?inicio={inicio}&final={final}&page=1&perPage=50&formattedFilter=%7B%22category%22:[{categoria}],%22type%22:[{tipo}],%22client%22:[{cliente}],%22responsable%22:[{usuario}]%7D',
            cookies=cookies,
            headers=headers,
            verify=False,
        )
