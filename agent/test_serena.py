import asyncio
from agno.tools.mcp import MCPTools

async def main():
	serena = MCPTools(
		command="serena start-mcp-server --project-from-cwd --context desktop-app --open-web-dashboard False"
	)
	await serena.connect()

	print("Функции Serena MCP:")
	for name in serena.functions.keys():
		print(f"  - {name}")

	await serena.close()

asyncio.run(main())
