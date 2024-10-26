import pymysql as mysql
from app.cfg import Config

def getConnection():
    try:
        conn = mysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return conn

    except Exception as E:
        print(f"Erro ao conectar no banco de dados {E}")