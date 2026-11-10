import os

import requests

# Endereço da aplicação. Por padrão, o contêiner publicado na porta 8000.
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


def test_pagina_inicial_responde_200():
    resposta = requests.get(f"{BASE_URL}/", timeout=5)
    assert resposta.status_code == 200
    assert "mensagem" in resposta.json()


def test_health_retorna_status_ok():
    resposta = requests.get(f"{BASE_URL}/health", timeout=5)
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_soma_retorna_resultado_correto():
    resposta = requests.get(f"{BASE_URL}/soma", params={"a": 2, "b": 3}, timeout=5)
    assert resposta.status_code == 200
    assert resposta.json()["resultado"] == 5


def test_soma_com_parametro_invalido_retorna_400():
    resposta = requests.get(f"{BASE_URL}/soma", params={"a": "abc", "b": 3}, timeout=5)
    assert resposta.status_code == 400