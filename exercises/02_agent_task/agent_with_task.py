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


# TODO 1: Create a Task.
# Give it a clear description and expected output.
research_task = Task(
    description="TODO",
    expected_output="TODO",
    agent=researcher
)


# TODO 2: Create a one-agent Crew and add the task to it.
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)


# TODO 3: Run the Crew with a topic.
result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})

print("\n--- Task Result ---")
print(result)
