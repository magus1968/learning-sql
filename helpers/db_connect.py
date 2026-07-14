import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Автоматически находим .env в корне проекта и загружаем переменные
load_dotenv(find_dotenv())

def get_mysql_engine():
    """Создает и возвращает SQLAlchemy Engine для подключения к MySQL,
    используя переменные из .env"""
    connection_url = URL.create(
        drivername="mysql+pymysql",
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME", "ozerova"),
        username=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
    )
    return create_engine(connection_url)

engine = get_mysql_engine()