import os, sys
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv

# загружаем переменные из файла .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY") or sys.exit("Ошибка: в файле .env отсутствует OPENROUTER_API_KEY")
id_model = "nvidia/nemotron-3-super-120b-a12b:free"         # <--- эта модель нам точно подойдет

# пишем нашу собственную функцию (инструмент)
def get_student_schedule(day: str) -> str:
    """
    Узнает расписание занятий студента на заданный день недели.

    Args:
        day (str): День недели на русском языке (например, 'понедельник', 'вторник').

    Returns:
        str: Список пар или сообщение о выходном.
    """
    schedule = {
        "понедельник": "1. Вышмат\n2. Программирование на Python\n3. Физика",
        "вторник": "1. Базы данных\n2. Английский язык",
        "среда": "1. Физкультура\n2. Алгоритмы",
    }

    # ищем день в словаре (переводим в нижний регистр для защиты от опечаток ИИ)
    result = schedule.get(day.lower().strip())

    if result:
        return f"Расписание на {day}:\n{result}"
    else:
        return f"На {day} пар нет! Можно спать спокойно."

# создаем агента и передаем ему нашу функцию в список tools
agent = Agent(
    model=OpenRouter(id=id_model),
    description="Ты - заботливый ИИ-староста группы. Твоя задача - помогать студентам с расписанием.",
    tools=[get_student_schedule],  # <--- передаем нашу функцию без скобок!
)

# запускаем диалог
print(agent.run("Привет! Подскажи, какие у меня завтра пары? Завтра вторник.").content)
print("-" * 40)
print(agent.run("А что в субботу?").content)

