from crewai import Agent, LLM

llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

researcher = Agent(
    role="Researcher",
    goal="Research a topic and identify the most important information.",
    backstory="You are a careful researcher who provides clear and useful information.",
    llm=llm,
    verbose=True
)

summarizer = Agent(
    role="Summarizer",
    goal="Turn research into a short, clear summary.",
    backstory="You summarize information accurately without losing the key points.",
    llm=llm,
    verbose=True
)

research_result = researcher.kickoff("Research the benefits of electric vehicles.")
summary_result = summarizer.kickoff(
    f"""Here is the research produced by another agent:

{research_result}

Summarize the research into 3-5 clear bullet points."""
)

print("\n--- Researcher Output ---")
print(research_result)
print("\n--- Summarizer Output ---")
print(summary_result)
