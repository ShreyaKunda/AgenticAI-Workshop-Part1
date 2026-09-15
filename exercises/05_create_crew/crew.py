from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

researcher = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)

threat_analyst = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)

security_advisor = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)

research_task = Task(
    description="TODO",
    expected_output="TODO",
    agent=researcher
)

analysis_task = Task(
    description="TODO",
    expected_output="TODO",
    agent=threat_analyst,
    context=[research_task]
)

recommendation_task = Task(
    description="TODO",
    expected_output="TODO",
    agent=security_advisor,
    context=[analysis_task]
)

crew = Crew(
    agents=[researcher, threat_analyst, security_advisor],
    tasks=[research_task, analysis_task, recommendation_task],
    verbose=True
)

result = crew.kickoff()

print("\n--- Final Result ---")
print(result)
