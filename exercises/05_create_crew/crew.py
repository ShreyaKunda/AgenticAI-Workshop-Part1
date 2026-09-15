from crewai import Agent, Task, Crew, LLM


# Connect to Ollama
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# --------------------------------------------------
# Agent 1: Researcher
# --------------------------------------------------

researcher = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)


# --------------------------------------------------
# Agent 2: Threat Analyst
# --------------------------------------------------

analyst = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)


# --------------------------------------------------
# Agent 3: Security Advisor
# --------------------------------------------------

advisor = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)


# --------------------------------------------------
# Task 1: Research
# --------------------------------------------------

research_task = Task(
    description="""
    Research the major risks associated with phishing attacks.

    Identify the common ways phishing can affect individuals
    and organizations.
    """,
    expected_output="A concise summary of the major risks associated with phishing.",
    agent=researcher
)


# --------------------------------------------------
# Task 2: Analyse
# --------------------------------------------------

analysis_task = Task(
    description="""
    Review the research produced by the Researcher.

    Identify the three most important security risks
    and briefly explain why each one is important.
    """,
    expected_output="Three key phishing risks with short explanations.",
    agent=analyst,
    context=[research_task]
)


# --------------------------------------------------
# Task 3: Recommend
# --------------------------------------------------

recommendation_task = Task(
    description="""
    Review the risk analysis produced by the Threat Analyst.

    Recommend practical actions that an organization
    could take to reduce these risks.
    """,
    expected_output="A list of practical security recommendations.",
    agent=advisor,
    context=[analysis_task]
)


# --------------------------------------------------
# Create the Crew
# --------------------------------------------------

crew = Crew(
    agents=[
        researcher,
        analyst,
        advisor
    ],
    tasks=[
        research_task,
        analysis_task,
        recommendation_task
    ],
    verbose=True
)


# --------------------------------------------------
# Run the Crew
# --------------------------------------------------

result = crew.kickoff()

print("\n--- Final Crew Output ---")
print(result)
