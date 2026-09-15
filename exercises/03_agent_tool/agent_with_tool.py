from pathlib import Path

from crewai import Agent, LLM
from crewai.tools import tool


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "sample_data.txt"


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# TODO: This custom tool gives the agent access to the local data file.
@tool("Read sample data")
def read_sample_data() -> str:
    """Read the sample dataset provided for the workshop."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return file.read()


researcher = Agent(
    role="Data Analyst",
    goal="Read the provided data and answer questions about it",
    backstory="You are a careful analyst who works with simple datasets.",
    tools=[read_sample_data],
    llm=llm,
    verbose=True
)


# TODO: Change the question and observe how the agent uses its tool.
result = researcher.kickoff(
    "Read the data file and identify the product with the highest sales."
)

print("\n--- Agent Response ---")
print(result)
