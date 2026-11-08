from strands import Agent
from strands.models.anthropic import AnthropicModel
# TODO: Step 1 - Import MCPClient from strands.tools.mcp
from strands.tools.mcp import MCPClient

# TODO: Step 1 - Create an MCPClient with the url "http://localhost:8002/mcp"
mcp_dice_client = MCPClient(url="http://localhost:8002/mcp")

# Use the Anthropic API directly instead of the default Amazon Bedrock model.
# Reads the API key from the ANTHROPIC_API_KEY environment variable.
model = AnthropicModel(model_id="claude-haiku-5-5", max_tokens=4096)

gamemaster = Agent(
    model=model,
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in fantasy role-playing adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about the game mechanics, always use the appropriate tools when applicable - never make up results!""",
    # TODO: Step 2 - Add the MCP tool to the gamemaster agent
    tools=[mcp_dice_client]
)

gamemaster("Help me create a new fantasy character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")
