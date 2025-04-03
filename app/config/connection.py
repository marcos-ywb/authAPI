import pymysql as mysql
from app.cfg import Config

def getConnection():
    try:
        conn = mysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            port=Config.DB_PORT,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return conn
    except mysql.Error as Err:
        print(f"Erro ao conectar no banco de dados: {Err}")