from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from agno.db.sqlite import SqliteDb
from tools import *

from config import api_key
from knowledge import knowledge

# память агента (база данных одна для всех)
db = SqliteDb(db_file="data.db")

# оборачиваем создание агента в функцию!
def create_agent(session_id="console_agent"):
    agent = Agent(
        model=DeepSeek(id="deepseek-v4-flash"),
        description="Ты - дружелюбный ИИ-помощник, который умеет пользоваться интернетом и базой знаний.",
        instructions=[load_prompt()],
        tools=get_tools(),
        session_id=session_id,      
        db=db,
        add_history_to_context=True,
        num_history_runs=50,       
        knowledge=knowledge,        
        search_knowledge=True,
        debug_mode=True
    )
    return agent

