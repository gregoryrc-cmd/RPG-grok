"""Funções para ler e gravar arquivos JSON."""
import json
import os


def carregar_json(caminho, padrao=None):
    """Lê o JSON; se o arquivo não existir, devolve padrao."""
    if not os.path.exists(caminho):
        return padrao
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(caminho, dados):
    """Grava os dados em JSON, substituindo o conteúdo anterior."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)
