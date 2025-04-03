from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    DB_HOST = os.getenv("127.0.0.1")
    DB_USER = os.getenv("root")
    #DB_PORT = os.getenv("3306")
    DB_PASSWORD = os.getenv("root")
    DB_NAME = os.getenv("banco_dados")

    API_HOST = os.getenv("127.0.0.1")
    API_PORT = os.getenv("5000")
