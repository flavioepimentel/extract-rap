
import os
import datetime
import time
import json
from requests import Session
from dotenv import load_dotenv
from services import RapService, UsuariosService, AuthService, ProjetosService


load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")


def semana_para_datas():
    hoje = datetime.date.today()
    # Captura o número da semana ISO
    ano_iso, semana_iso, dia_semana = hoje.isocalendar()
    # Segunda-feira da semana
    segunda = datetime.date.fromisocalendar(ano_iso, semana_iso, 1)
    # Sexta-feira da mesma semana
    sexta = datetime.date.fromisocalendar(ano_iso, semana_iso, 5)
    return segunda, sexta


if __name__ == "__main__":
    # 1. login
    session = Session()
    print(f"Usuário: {USUARIO}")
    auth_service = AuthService(USUARIO, SENHA, session)
    projetos_service = ProjetosService(session)
    usuarios_service = UsuariosService(session)
    raps_service = RapService(session)

# 1.1 Chamar login
    auth_service.login()
# 1.3 Receber resposta do login chamar  raps filtrados
    categoria_rap = raps_service.get_categorias_rap(auth_service.cookies,
                                                    auth_service.headers)
    tipo_rap = raps_service.get_tipos_rap(auth_service.cookies,
                                          auth_service.headers)
    clientes = projetos_service.get_all_clients(auth_service.cookies,
                                                auth_service.headers)

    usuarios = usuarios_service.get_all_users(auth_service.cookies,
                                              auth_service.headers)

    # Segunda e sexta da semana atual
    segunda, sexta = semana_para_datas()

    all_raps = raps_service.get_all_raps(
        auth_service.cookies,
        auth_service.headers,
        segunda,
        sexta,
        "Flávio Pimentel"
    )

    all_raps.json()["data"][0]

    for user in usuarios.json():
        raps = raps_service.get_all_raps(
            auth_service.cookies,
            auth_service.headers,
            segunda,
            sexta,
            user['name']
        )
        obj_raps = []
        for rap in raps.json()["data"]:
            obj_raps.append(
                {
                    "id": rap['id'],
                    "visita": rap['visita'],
                    "titulo": rap['projeto']['titulo'],
                    "data": rap['data'],
                    "cliente": rap['projeto']['cliente']['descricao'],
                    "projeto": rap['projeto']['titulo'],
                    "responsavel": rap['responsavel']['name'],
                    "contato": rap['contato'],
                    "periodo_inicio": rap['periodo_inicio'],
                    "periodo_fim": rap['periodo_fim'],
                    "categoria_rap": rap['categoria_rap']['valor'],
                    "tipo_rap": rap['tipo_rap']['valor'],
                    "descricao": rap['descricao'],
                    "pendencias": rap['pendencias'],
                    "proximos_passos": rap['proximos_passos'],
                    "outras_infos": rap['outras_infos'],
                    "conquistas": rap['conquistas'],
                    "noticias": rap['noticias']
                }
            )
        print(f"Raps do usuário {user['name']}: {raps.json()["data"]}")
        if raps.json()["data"] not in [None, []]:
            with open(f"{str(user['name']).replace(" ", "_").lower()}.json", "w", encoding="utf-8") as f:
                f.write(str(json.dumps(obj_raps, ensure_ascii=False, indent=4)))


# 1.5 Chamar download dos raps
# 1.6 Salvar raps em PDF
# 1.7 Ler raps em PDF
# 1.8 Dispor arquivos em api
