# tests/test_connection.py
from config.database import get_connection

def test_db_connection():
    """Testa a conexão com o banco de dados executando uma consulta simples."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")  # Testa a conexão com uma consulta simples
                result = cursor.fetchone()
                print("Conexão bem-sucedida! Resultado da consulta:", result)
        except Exception as e:
            print("Erro ao executar consulta:", e)
        finally:
            conn.close()  # Fechar a conexão após o teste
    else:
        print("Falha ao conectar ao banco de dados.")

if __name__ == "__main__":
    test_db_connection()
