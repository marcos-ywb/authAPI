from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_TYPE = os.getenv("SESSION_TYPE")
    
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    API_HOST = os.getenv("API_HOST")
    API_PORT = os.getenv("API_PORT")
