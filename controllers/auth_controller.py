from typing import Optional
import requests as r
from bs4 import BeautifulSoup as bs


class AuthController:

    def __init__(self, session: r.Session):
        self.session = session

    def get_home(self):
        self.session.get('http://wisetech.dyndns.org:8000/home',
                         cookies=self.session.cookies, headers=self.session.headers, verify=False)

    def get_login(self) -> r.Response:
        return self.session.get(
            "http://wisetech.dyndns.org:8000/login"
        )

    def post_login(self, payload: dict, headers) -> bool:
        return self.session.post(
            "http://wisetech.dyndns.org:8000/login",
            data=payload,
            headers=headers
        )
