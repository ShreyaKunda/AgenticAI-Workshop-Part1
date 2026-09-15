from crewai import Agent, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


researcher = Agent(
    role="Researcher",
    goal="Research a topic and identify the most important information.",
    backstory="You are a careful researcher who provides clear and useful information.",
    llm=llm,
    verbose=True
)


summarizer = Agent(
    role="Summarizer",
    goal="Turn research from another agent into a concise summary.",
    backstory="You are a clear and precise summarizer who focuses on the most important points.",
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

    Summarize the research in five clear bullet points.
    """
)


print("\n--- Researcher Output ---")
print(research_result)

print("\n--- Summarizer Output ---")
print(summary_result)
