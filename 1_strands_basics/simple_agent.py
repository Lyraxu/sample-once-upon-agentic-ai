from strands import Agent
import logging

# Create an agent with a specific model by passing the model ID string
agent = Agent()

# TODO: Step 1 - Add debug logging to see what your agent is thinking

logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# TODO: Step 2 - Create the agent with the following system prompt: "You are a game master for a Dungeon & Dragon game"
agent = Agent(
    system_prompt=(
        "You are a D&D game master. You will guide the player through a text-based adventure, providing descriptions of the environment, characters, and events. You will also respond to the player's actions and decisions, creating an engaging and immersive experience."
    )
)
# TODO: Step 3 - Invoke your agent with a basic query such as "Hi, I am an adventurer ready for adventure!"
Response = agent("Hi, I am an adventurer ready for adventure!")