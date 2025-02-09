import pymysql
from config.settings import db_host, db_user, db_password, db_name


def create_table():
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS emails (
                id INT PRIMARY KEY AUTO_INCREMENT,
                email_id INT UNIQUE,  
                campaign_id INT,
                name VARCHAR(255),
                created_at DATETIME,
                updated_at DATETIME,
                send_at DATETIME NULL,
                status VARCHAR(50),
                type VARCHAR(50),
                leads_count INT NULL,
                is_predictive_sending BOOLEAN NULL,
                sending_is_imminent BOOLEAN NULL,
                engaged BOOLEAN NULL,
                disengaged BOOLEAN NULL,
                indeterminate BOOLEAN NULL
            )
            """
        )
    connection.commit()
    connection.close()