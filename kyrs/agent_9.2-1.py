import os, sys
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv

# импортируем наши инструменты
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.calculator import CalculatorTools
from agno.tools.yfinance import YFinanceTools

# загружаем переменные из файла .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY") or sys.exit("Ошибка: в файле .env отсутствует OPENROUTER_API_KEY")
id_model = os.getenv("ID_MODEL") or sys.exit("Ошибка: в файле .env отсутствует ID_MODEL")

# создаем агента
agent = Agent(
    model=OpenRouter(id=id_model),        # подключение модели
    description="Ты отвечаешь, используя актуальные данные из интернета",  # цель агента
    tools=[
        DuckDuckGoTools(),                # инструмент поиска в интернете
        Newspaper4kTools(),               # чтение статей с сайтов
        CalculatorTools(),                # калькулятор для точных вычислений
        YFinanceTools()                   # финансовые данные от Yahoo
    ],
    debug_mode=True                       # <== ВАЖНО: включаем "рентген" для просмотра мыслей ИИ!
)

# получение ответа
print(agent.run("Сколько сейчас стоит акция Apple?").content)
