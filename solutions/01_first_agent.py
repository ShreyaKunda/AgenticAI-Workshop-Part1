from crewai import Agent, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


researcher = Agent(
    role="Researcher",
    goal="Find and explain useful information about a given topic",
    backstory="You are a curious researcher who explains complex topics simply.",
    llm=llm,
    verbose=True
)


result = researcher.kickoff(
    "Explain what Artificial Intelligence is in simple terms."
)

print("\n--- Agent Response ---")
print(result)
