import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Banco de Dados
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# API
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
token_url = os.getenv("TOKEN_URL")
api_url = os.getenv("API_URL")
refresh_token = os.getenv("REFRESH_TOKEN")

print(f"Conectando ao banco: {db_host}, usuário: {db_user}")
