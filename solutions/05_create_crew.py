from crewai import Agent, Task, Crew, LLM

llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

researcher = Agent(
    role="Researcher",
    goal="Research a cybersecurity topic and provide useful evidence.",
    backstory="You are a careful cybersecurity researcher.",
    llm=llm,
    verbose=True
)

threat_analyst = Agent(
    role="Threat Analyst",
    goal="Analyze research and identify relevant threats and risks.",
    backstory="You analyze technical findings and distinguish evidence from assumptions.",
    llm=llm,
    verbose=True
)

security_advisor = Agent(
    role="Security Advisor",
    goal="Recommend practical security improvements based on the analysis.",
    backstory="You turn security findings into actionable recommendations.",
    llm=llm,
    verbose=True
)

research_task = Task(
    description="Research the cybersecurity topic of phishing attacks. Explain the main risks, common techniques, and why organizations are affected.",
    expected_output="A concise research summary covering risks, techniques, and organizational impact.",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research findings. Identify the most important threats, likely attack paths, and areas of risk.",
    expected_output="A structured threat analysis that separates observations from interpretations.",
    agent=threat_analyst,
    context=[research_task]
)

recommendation_task = Task(
    description="Based on the threat analysis, recommend practical controls and actions that an organization could take.",
    expected_output="A prioritized list of practical security recommendations with a short reason for each.",
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
