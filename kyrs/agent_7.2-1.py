import os, sys
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# загружаем переменные из файла .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY") or sys.exit("Ошибка: в файле .env отсутствует OPENROUTER_API_KEY")
id_model = "nvidia/nemotron-3-super-120b-a12b:free"         # <= эта модель нам точно подойдет

# создаем строгую схему данных с помощью Pydantic
class UserProfile(BaseModel):
    name: str = Field(description="Имя пользователя")
    age: int = Field(description="Возраст пользователя в годах")
    hobbies: list[str] = Field(description="Список увлечений и хобби")
    is_student: bool = Field(description="Учится ли пользователь в данный момент (True/False)")

# создаем агента и передаем ему нашу схему
agent = Agent(
    model=OpenRouter(id=id_model),
    description="Ты - опытный HR-аналитик. Твоя задача: извлекать данные из текста и строго следовать формату.",
    output_schema=UserProfile,  # <= ключевой момент! Заставляем агента отвечать по схеме UserProfile
)

# неструктурированный текст (например, из голосового сообщения)
user_message = """
Привет! Меня зовут Максим, мне двадцать один год. 
Я сейчас учусь в универе на программиста. 
В свободное время обожаю кататься на сноуборде, играть в приставку и есть пиццу.
"""

# запускаем агента
print("Анализирую текст...\n")
response = agent.run(user_message)

# выводим результат. Обрати внимание: response.content - это теперь не строка, а объект UserProfile!
profile = response.content

print("Тип данных:", type(profile))
print("Имя:", profile.name)
print("Возраст:", profile.age)
print("Хобби:", profile.hobbies)
print("Студент:", profile.is_student)

