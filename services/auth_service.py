from typing import Optional
from controllers.auth_controller import AuthController
from bs4 import BeautifulSoup as bs
import requests as r
from urllib.parse import urlparse


class AuthService:

    def __init__(self, email: str, password: str, session: r.Session):
        self.email = email
        self.password = password
        self.session = session
        self.auth_controller = AuthController(self.session)
        self.last_response = self.auth_controller.get_login() or None

    def _extract_token(self) -> str:
        soup: bs = bs(self.last_response.text, "html.parser")
        self.token: str = soup.find("input", {"name": "_token"})["value"]
        return self.token

    def _extract_cookies(self) -> dict:
        return self.session.cookies

    def _extract_csrf_token(self, html_content: str) -> Optional[str]:
        soup = bs(html_content, "html.parser")
        meta_tag = soup.find("meta", attrs={"name": "csrf-token"})
        if meta_tag and meta_tag.get("content"):
            return str(meta_tag["content"])

        input_tag = soup.find("input", attrs={"name": "_token"})
        if input_tag and input_tag.get("value"):
            return str(input_tag["value"])

        return None

    def _build_headers(self) -> dict:
        return {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Referer': 'http://wisetech.dyndns.org:8000/home',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'X-XSRF-TOKEN': self.session.cookies.get("XSRF-TOKEN"),

        }

    def _build_payload(self) -> dict:
        self.payload = {
            "_token": self.token,
            "email": self.email,
            "password": self.password,
            'remember': 'on',
        }
        return self.payload

    def _get_redirect_url(self, response: r.Response) -> Optional[str]:
        if response.is_redirect:
            return response.headers.get("Location")
        return None

    def _is_login_successful(self, response: r.Response) -> bool:
        if response.status_code == 200:
            houve_redirect = any(
                item.is_redirect or item.is_permanent_redirect
                for item in response.history
            )
            caminho_final = urlparse(response.url).path.rstrip("/")
            return True if houve_redirect and caminho_final == "/home" or caminho_final == "js/vuex-persistedstate.es.js.map" else False
        return False

    def login(self):
        self.token = self._extract_token()
        self.headers = self._build_headers()
        self.payload = self._build_payload()
        self.cookies = self._extract_cookies()

        self.auth_controller = AuthController(self.session)
        self.last_response = self.auth_controller.post_login(
            self.payload, self.headers)
        print("Resposta do login:", self.last_response.status_code)
        if self._is_login_successful(self.last_response):
            print("Login bem-sucedido!")
