from pathlib import Path
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mcp import MCPTools

def load_prompt() -> str:
	path = Path("prompt.txt")
	if not path.exists():
		return "Ты агент-программист."
	return path.read_text(encoding="utf-8")


filesystem_mcp = MCPTools(
	command="npx -y @modelcontextprotocol/server-filesystem ."
)

git_mcp = MCPTools(
	command="uvx mcp-server-git --repository ."
)

memory_mcp = MCPTools(
	command="npx -y @modelcontextprotocol/server-memory"
)


serena_mcp = MCPTools(
	command="serena start-mcp-server --project-from-cwd --context desktop-app --open-web-dashboard False"
)

context7_mcp = MCPTools(
	command="npx -y @upstash/context7-mcp"
)

thinking_mcp = MCPTools(
	command="npx -y @modelcontextprotocol/server-sequential-thinking"
)



def get_tools() -> list:
	return [
        DuckDuckGoTools(),
		filesystem_mcp,
		#git_mcp,
		#memory_mcp,
		serena_mcp,
		#context7_mcp,
		#thinking_mcp,
	]
