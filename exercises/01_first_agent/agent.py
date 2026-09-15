from crewai import Agent, LLM


# Connect CrewAI to Ollama
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# TODO 1: Create a Researcher Agent.
# Define its role, goal and backstory.
researcher = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)


# Run the agent
result = researcher.kickoff(
    "Explain what Artificial Intelligence is in simple terms."
)

print("\n--- Agent Response ---")
print(result)
