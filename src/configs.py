import os

from dotenv import load_dotenv

if load_dotenv():
    DB_USER: str = os.getenv('DB_USER', 'admin')
    DB_PASS: str = os.getenv('DB_PASS', 'admin')
    DB_NAME: str = os.getenv('DB_NAME', 'db')
    DB_HOST: str = os.getenv('DB_HOST', 'localhost')
    DB_PORT: str = os.getenv('DB_PORT', '5432')
    JWT_SECRET: str = os.getenv("JWT_SECRET", "SECRET")
    USER_SECRET: str = os.getenv("USER_SECRET", "SECRET")
else:
    print('Нет файла ".env" с переменными окружения.')
