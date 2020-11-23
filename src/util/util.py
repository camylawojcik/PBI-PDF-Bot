from typing import List

from src.config.config import Config


def get_info(raiz: str, grupo: str):
    items = [Config.get(raiz, grupo)]
    lista = []
    for i in items:
        lista = (list(i.keys()))

    if lista:
        lista_url = []
        for i in lista:
            lista_url.append(Config.get(raiz, grupo, i))

        return lista_url

# def get_info(raiz: str, items: List[str]):
#     if items:
#         lista_url = []
#         for i in items:
#             lista_url.append(Config.get(raiz, i))
#
#         return lista_url