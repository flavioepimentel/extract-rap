
import os
import datetime
import time
import json
from requests import Session
from dotenv import load_dotenv
from services import RapService
from services import AuthService
from services import ProjetosService


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

    # Segunda e sexta da semana atual
    segunda, sexta = semana_para_datas()

    all_raps = raps_service.get_all_raps(
        auth_service.cookies,
        auth_service.headers,
        segunda,
        sexta,
        "Flávio Pimentel"
    )
    """Categoria
    {'id': 43, 'sigla': 'AP', 'valor': 'Acompanhamento de projetos', 'empresa_id': 1, 'created_at': '2022-04-02T22:30:37.000000Z', 'updated_at': '2022-04-02T22:30:37.000000Z', 'deleted_at': None, 'isMarco': 0}
    """

    """Tipo
    {'id': 8, 'sigla': 'CA', 'valor': 'Cliente (Acompanhamento/Aprendizado)', 'empresa_id': 1, 'created_at': '2022-03-31T10:36:06.000000Z', 'updated_at': '2025-12-02T19:00:57.000000Z', 'deleted_at': None, 'isTempoConsumivel': 1}
    """

    """RAP
    {
  "id": 33027,
  "projeto_id": 396,
  "categoria_rap_id": 54,
  "tipo_rap_id": 7,
  "atuacao": null,
  "rascunho": 0,
  "visita": "Cronstrução de realatório",
  "contato": "Murilo",
  "data": "2026-09-28",
  "periodo_inicio": "08:00",
  "periodo_fim": "11:00",
  "intervalo": 0,
  "descricao": "Cronstrução de realatório:\n- SOLICITAÇÕES ATENDIDAS POR ESPECIALIDADE, tem o objetivo de exibir todos os atendimentos e respectivas especialidades;\n- RELATÓRIO DE SOLICITAÇÕES, exibe a relatório solicitações despachadas para pacientes e importa as informações do primeiro relatório para conciliar as solicitações por especialidade.",
  "emails": null,
  "conquistas": null,
  "noticias": null,
  "pendencias": "- Validação do cliente.",
  "proximos_passos": null,
  "reivind_ocorrencias": null,
  "outras_infos": null,
  "created_at": "2026-09-29T10:35:26.000000Z",
  "updated_at": "2026-09-29T10:35:38.000000Z",
  "deleted_at": null,
  "responsavel_id": 52,
  "categoria_rap": {
    "id": 54,
    "sigla": "AI",
    "valor": "Atividades Internas",
    "empresa_id": 1,
    "created_at": "2022-06-05T22:40:34.000000Z",
    "updated_at": "2022-06-05T22:40:34.000000Z",
    "deleted_at": null,
    "isMarco": 0
  },
  "tipo_rap": {
    "id": 7,
    "sigla": "CL",
    "valor": "Cliente",
    "empresa_id": 1,
    "created_at": "2022-03-31T10:09:23.000000Z",
    "updated_at": "2022-03-31T10:09:23.000000Z",
    "deleted_at": null,
    "isTempoConsumivel": 1
  },
  "avancos": [],
  "projeto": {
    "id": 396,
    "titulo": "IMAIS [Laboratório e clínica] Implantação do Klingo",
    "cliente_id": 50,
    "empresa_id": 1,
    "mercadoria_id": 6,
    "observacao": null,
    "numero_op": null,
    "inicio": "2023-05-10",
    "fim": "2025-09-30",
    "horas_contratadas": 200,
    "escopo": "Implantação Klingo",
    "objetivo": null,
    "fora_escopo": null,
    "premissas": null,
    "restricoes": null,
    "tags": "[]",
    "status_id": 1,
    "responsavel": {
      "id": 10,
      "name": "Romario Sena",
      "email": "romario@wisetech.com.br",
      "email_verified_at": "2022-03-21T22:01:56.000000Z",
      "provider": null,
      "provider_id": null,
      "created_at": "2022-03-21T22:01:33.000000Z",
      "updated_at": "2022-03-21T22:01:56.000000Z",
      "deleted_at": null
    },
    "created_at": "2025-08-16T14:06:37.000000Z",
    "updated_at": "2025-08-16T14:06:37.000000Z",
    "deleted_at": null,
    "data_cancelado": null,
    "data_finalizado": null,
    "data_suspenso": null,
    "lider_tecnico": {
      "id": 10,
      "name": "Romario Sena",
      "email": "romario@wisetech.com.br",
      "email_verified_at": "2022-03-21T22:01:56.000000Z",
      "provider": null,
      "provider_id": null,
      "created_at": "2022-03-21T22:01:33.000000Z",
      "updated_at": "2022-03-21T22:01:56.000000Z",
      "deleted_at": null
    },
    "consultor": {
      "id": 7,
      "name": "Lucas Nunes",
      "email": "lucas.nunes@softfy.com.br",
      "email_verified_at": "2022-03-21T21:58:16.000000Z",
      "provider": null,
      "provider_id": null,
      "created_at": "2022-03-21T21:57:35.000000Z",
      "updated_at": "2025-08-19T19:00:55.000000Z",
      "deleted_at": null
    },
    "horas_consumidas": 701.32,
    "horas_gerais": 0,
    "empresa": {
      "id": 1,
      "created_at": "2022-03-21T22:03:53.000000Z",
      "updated_at": "2022-04-25T20:32:53.000000Z",
      "nome": "Wisetech",
      "cnpj": "06166173000160",
      "dominio": "https://wisetech.com.br/",
      "deleted_at": null
    },
    "cliente": {
      "id": 50,
      "empresa_id": 1,
      "descricao": "Laboratório IMAIS",
      "created_at": "2022-04-02T23:07:28.000000Z",
      "updated_at": "2024-01-02T14:55:05.000000Z",
      "deleted_at": null,
      "arredondamento": 15
    }
  },
  "responsavel": {
    "id": 52,
    "name": "Flávio Pimentel",
    "email": "flavio.pimentel@wisetech.com.br",
    "email_verified_at": "2025-10-06T19:38:36.000000Z",
    "provider": null,
    "provider_id": null,
    "created_at": "2025-09-30T17:12:40.000000Z",
    "updated_at": "2025-10-06T19:38:36.000000Z",
    "deleted_at": null
  }
}
    """

    """Cliente
    {'id': 4, 'empresa_id': 1, 'descricao': 'Laboratório Santa Maria', 'created_at': '2022-03-30T09:55:22.000000Z', 'updated_at': '2025-07-30T17:13:13.000000Z', 'deleted_at': None, 'arredondamento': 20, 'empresa': {'id': 1, 'created_at': '2022-03-21T22:03:53.000000Z', 'updated_at': '2022-04-25T20:32:53.000000Z', 'nome': 'Wisetech', 'cnpj': '06166173000160', 'dominio': 'https://wisetech.com.br/', 'deleted_at': None}}
    """

    """
    | ID | TITULO | DATA | CLIENTE | PROJETO | RESPONSÁVEL | CONTATO | HORAS REALIZADAS | CATEGORIA RAP | TIPO RAP | ATIVIDADES REALIZADAS | PENDÊNCIAS | PRÓXIMOS PASSOS | OUTRAS INFORMAÇÕES | CONQUISTAS | NOTÍCIAS |
    """

    """
CLIENTE: 

PERÍODO: DD/MM/AAAA a DD/MM/AAAA

PROJETO: 

CONSULTOR: 

📋 RESUMO EXECUTIVO
-

✅ O QUE FOI REALIZADO NA SEMANA:
-

⏳ O QUE FALTA / PENDÊNCIAS:
-

📌 O QUE SERÁ REALIZADO NA PRÓXIMA SEMANA:
- 
    """
    # f.write(
    #     "ID;TÍTULO;DATA;CLIENTE;PROJETO;RESPONSÁVEL;CONTATO;HORAS REALIZADAS;CATEGORIA RAP;TIPO RAP;ATIVIDADES REALIZADAS;PENDÊNCIAS;PRÓXIMOS PASSOS;OUTRAS INFORMAÇÕES;CONQUISTAS;NOTÍCIAS\n"
    # )
    obj_raps = {"data": []}
    print(all_raps.json())
    for rap in all_raps.json()["data"]:
        obj_raps["data"].append(
            {
                "id": rap['id'],
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

    with open("all_raps.json", "w", encoding="utf-8") as f:
        f.write(str(all_raps.json()["data"]).replace(
            "'", '"').replace("None", "null"))
    # for rap in all_raps.json()["data"]:
    #     print(f"ID: {rap['id']}")
    #     print(f"TÍTULO: {rap['projeto']['titulo']}")
    #     print(f"DATA: {rap['data']}")
    #     print(f"CLIENTE: {rap['projeto']['cliente']['descricao']}")
    #     print(f"PROJETO: {rap['projeto']['titulo']}")
    #     print(f"RESPONSÁVEL: {rap['responsavel']['name']}")
    #     print(f"CONTATO: {rap['contato']}")
    #     print(
    #         f"HORAS REALIZADAS: {rap['periodo_inicio']} - {rap['periodo_fim']}")
    #     print(f"CATEGORIA RAP: {rap['categoria_rap']['valor']}")
    #     print(f"TIPO RAP: {rap['tipo_rap']['valor']}")
    #     print(f"ATIVIDADES REALIZADAS: {rap['descricao']}")
    #     print(f"PENDÊNCIAS: {rap['pendencias']}")
    #     print(f"PRÓXIMOS PASSOS: {rap['proximos_passos']}")
    #     print(f"OUTRAS INFORMAÇÕES: {rap['outras_infos']}")
    #     print(f"CONQUISTAS: {rap['conquistas']}")
    #     print(f"NOTÍCIAS: {rap['noticias']}")
    #     print("-" * 50)
    #     print("\n\n\n\n")
    #     time.sleep(5)

    # print(clientes.json()[0])

# 1.5 Chamar download dos raps
# 1.6 Salvar raps em PDF
# 1.7 Ler raps em PDF
# 1.8 Dispor arquivos em api
