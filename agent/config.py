import os, sys
from dotenv import load_dotenv

# загружаем переменные один раз для всего проекта
load_dotenv()

# получаем ключи
api_key = os.getenv("DEEPSEEK_API_KEY") or sys.exit("Ошибка: в файле .env отсутствует OPENAI_API_KEY")
id_model = os.getenv("ID_MODEL") or sys.exit("Ошибка: в файле .env отсутствует ID_MODEL")
