import requests as r

class UsuariosController:
    def __init__(self, session: r.Session):
        self.session = session

    def get_usuarios(self, cookies: dict, headers: dict) -> r.Response:
        return self.session.get('http://wisetech.dyndns.org:8000/empresas/1/funcionarios', cookies=cookies, headers=headers, verify=False)
