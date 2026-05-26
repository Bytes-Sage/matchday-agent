from agent.prompt import SYSTEM_PROMPT
from config.settings import settings

try:
    from google.adk.agents import Agent
    from google.adk.tools.mcp_tool import McpToolset, StdioServerParameters
    
    mongodb_mcp_params = StdioServerParameters(
        command="npx",
        args=["-y", "mongodb-mcp-server@latest"],
        env={
            "MDB_MCP_CONNECTION_STRING": settings.MONGODB_URI,
            "MDB_MCP_READ_ONLY": "true",
            "MDB_MCP_LOG_LEVEL": "info"
        }
    )

    agent = Agent(
        name="matchday_agent",
        model=settings.GEMINI_MODEL,
        description="A World Cup 2026 match-day planning assistant",
        instruction=SYSTEM_PROMPT,
        tools=[McpToolset(server_params=mongodb_mcp_params)]
    )
except ImportError:
    # Fallback to genai if adk is not available
    from google import genai
    agent = None

def get_runner():
    try:
        from google.adk.runners import Runner
        return Runner(agent=agent)
    except ImportError:
        try:
            from google.adk.agents import Runner
            return Runner(agent=agent)
        except ImportError:
            # Maybe the agent itself is the runner
            if hasattr(agent, 'run_async'):
                return agent
            class FakeRunner:
                def __init__(self, agent):
                    self.agent = agent
                async def run_async(self, message, session_id):
                    return await self.agent.run_async(message)
            return FakeRunner(agent)
