from crewai import Agent, LLM


# Connect to Ollama
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# Agent 1: Researcher
researcher = Agent(
    role="Researcher",
    goal="Research a topic and identify the most important information.",
    backstory="You are a careful researcher who provides clear and useful information.",
    llm=llm,
    verbose=True
)


# Agent 2: Summarizer
summarizer = Agent(
    role="Summarizer",
    goal="Todo",
    backstory="Todo",
    llm=llm,
    verbose=True
)


# Step 1: Ask the Researcher to do its job
research_result = researcher.kickoff(
    "Research the benefits of electric vehicles."
)


# Step 2: Pass the Researcher's output to the Summarizer
summary_result = summarizer.kickoff(
    f"""
    Here is the research produced by another agent:

    {research_result}

    Todo
    """
)


# Display both outputs
print("\n--- Researcher Output ---")
print(research_result)

print("\n--- Summarizer Output ---")
print(summary_result)
