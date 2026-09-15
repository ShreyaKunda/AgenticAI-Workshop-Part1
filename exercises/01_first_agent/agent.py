from crewai import Agent, LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

assistant = Agent(
    role="AI Assistant",
    goal="Answer questions clearly and accurately.",
    backstory="You are a helpful AI assistant.",
    llm=llm,
    verbose=True
)

result = assistant.kickoff("Explain what Artificial Intelligence is in simple terms.")
print(result)
