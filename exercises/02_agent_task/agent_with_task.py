from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

researcher = Agent(
    role="Researcher",
    goal="Research a topic and provide useful information",
    backstory="You are a researcher who explains technical topics clearly.",
    llm=llm,
    verbose=True
)

research_task = Task(
    description="TODO",
    expected_output="TODO",
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff(
    inputs={"topic": "Artificial Intelligence"}
)

print("\n--- Task Result ---")
print(result)
