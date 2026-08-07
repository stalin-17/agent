import asyncio
from agent import create_agent

async def main():
	agent = create_agent()
	while question := input("User: ").strip():
		await agent.aprint_response(question, stream=True)

asyncio.run(main())
