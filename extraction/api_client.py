import requests
from extraction.auth_manager import obter_token, verificar_token

class APIClient:
    def __init__(self):
        self.base_url = "https://api.rd.services/platform/"  # Base da API

    def _atualizar_headers(self):
        """Atualiza o token no cabeçalho antes de fazer requisições."""
        verificar_token()
        return {"Authorization": f"Bearer {obter_token()}", "Content-Type": "application/json"}

    def get(self, endpoint, params=None):
        """Faz requisições GET na API."""
        headers = self._atualizar_headers()
        response = requests.get(f"{self.base_url}{endpoint}", headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Erro na requisição GET {endpoint}: {response.status_code} - {response.text}")
            return None

    def post(self, endpoint, data):
        """Faz requisições POST na API."""
        headers = self._atualizar_headers()
        response = requests.post(f"{self.base_url}{endpoint}", headers=headers, json=data)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"❌ Erro na requisição POST {endpoint}: {response.status_code} - {response.text}")
            return None
