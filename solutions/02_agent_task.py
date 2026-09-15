from crewai import Agent, Task, Crew, LLM

llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
researcher = Agent(role="Researcher", goal="Provide useful explanations", backstory="You explain technical concepts clearly.", llm=llm, verbose=True)
research_task = Task(description="Explain {topic} in simple terms. Include a definition, two key ideas, and one real-world example.", expected_output="A clear explanation with a definition, two key ideas, and one real-world example.", agent=researcher)
crew = Crew(agents=[researcher], tasks=[research_task], verbose=True)
result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})
print(result)
