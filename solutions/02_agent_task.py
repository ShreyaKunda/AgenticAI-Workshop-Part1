from crewai import Agent, Task, Crew, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


researcher = Agent(
    role="Researcher",
    goal="Research a topic and provide accurate information",
    backstory="You are a researcher who explains technical topics clearly.",
    llm=llm,
    verbose=True
)


research_task = Task(
    description="""
    Research the topic: {topic}

    Explain:
    1. What it is
    2. Why it is important
    3. One real-world example
    """,
    expected_output="A short explanation containing a definition, importance, and one real-world example.",
    agent=researcher
)


crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)


result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})

print("\n--- Task Result ---")
print(result)
