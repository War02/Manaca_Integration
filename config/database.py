import pymysql
from config.settings import db_host, db_user, db_password, db_name

# Função para estabelecer a conexão com o banco de dados
def get_connection():
    try:
        conn = pymysql.connect(
            host=db_host,        # Exemplo: "localhost" ou IP do servidor
            user=db_user,      # Exemplo: "root"
            password=db_password,    # Sua senha do MySQL
            database=db_name     # O nome do banco de dados
        )
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return conn
    except pymysql.MySQLError as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
