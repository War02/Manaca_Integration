import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Configurações da API
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
token_url = os.getenv("TOKEN_URL")
refresh_token = os.getenv("REFRESH_TOKEN")

# Variável global para armazenar o access_token
access_token = None


def renovar_token():
    """Renova o access_token usando o refresh_token."""
    global access_token, refresh_token

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        token_data = response.json()

        # 🔹 Atualiza as variáveis globais corretamente
        access_token = token_data["access_token"]
        refresh_token = token_data.get("refresh_token", refresh_token)  # Se houver um novo refresh_token, atualiza

        print("🔄 Token renovado com sucesso!")
    else:
        print(f"❌ Erro ao renovar o token: {response.status_code} - {response.text}")
        raise Exception("Falha na renovação do token.")


def obter_token():
    """Retorna um access_token válido, renovando se necessário."""
    global access_token

    if access_token is None:
        print("🔍 Token não encontrado, renovando...")
        renovar_token()

    return access_token


def verificar_token():
    """Verifica se o access_token é válido antes de fazer requisições."""
    global access_token

    headers = {"Authorization": f"Bearer {access_token}"}
    test_url = "https://api.rd.services/platform/emails"  # Endpoint de teste

    response = requests.get(test_url, headers=headers)

    if response.status_code == 401:
        print("⚠ Token expirado! Renovando...")
        renovar_token()
    elif response.status_code != 200:
        print(f"❌ Erro ao validar o token: {response.status_code} - {response.text}")

