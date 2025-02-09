import pymysql
from config.database import get_connection

def insert_email(data):
    connection = get_connection()
    if not connection:
        return

    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO emails (
                    email_id, campaign_id, name, created_at, updated_at, send_at, 
                    status, type, leads_count, is_predictive_sending, sending_is_imminent, 
                    engaged, disengaged, indeterminate
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                data["id"], data["campaign_id"], data["name"], data["created_at"],
                data["updated_at"], data.get("send_at"), data.get("status"), data["type"],
                data.get("leads_count"), data.get("is_predictive_sending"), data.get("sending_is_imminent"),
                data["behavior_score_info"].get("engaged"), data["behavior_score_info"].get("disengaged"),
                data["behavior_score_info"].get("indeterminate")
            )

            cursor.execute(sql, values)
        connection.commit()
    except Exception as e:
        print(f"❌ Erro ao inserir email {data.get('id')}: {e}")  # Exibe qual email causou o erro
        # Salva o erro em um arquivo de log ou lista para futura análise, caso necessário
        with open("errors.log", "a") as log_file:
            log_file.write(f"Erro ao inserir email {data.get('id')}: {e}\n")
    finally:
        connection.close()
