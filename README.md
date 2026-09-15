# Agentic AI Workshop — Part 1

This repository contains the hands-on exercises for Part 1 of the Agentic AI workshop.

The workshop uses **CrewAI + Ollama + a local LLM**, so no paid API key is required.

## Before You Begin

Install:

- Python 3.11
- Git
- Ollama

Make sure Ollama is running and download the model used in this workshop:

```bash
ollama pull llama3.2
```

You can test it with:

```bash
ollama run llama3.2
```

## Clone the Repository

```bash
git clone https://github.com/ShreyaKunda/AgenticAI-Workshop-Part1.git
cd AgenticAI-Workshop-Part1
```

## Create a Virtual Environment

### Windows

```bash
py -3.11 -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Workshop Exercises

| Exercise | Topic | Main idea |
| --- | --- | --- |
| 01 | First Agent | LLM → Agent |
| 02 | Agent + Task | Agent = who, Task = what |
| 03 | Agent + Tool | Giving an agent external capabilities |
| 04 | Specialized Agents | Passing output between agents |
| 05 | Create a Crew | Orchestrating multiple agents |

The exercises are intentionally small. The goal is to understand how agentic systems are constructed rather than copy a large application.

## Suggested Workshop Flow

1. Run Exercise 1 and observe the basic agent.
2. Add a Task in Exercise 2.
3. Give the agent a custom file-reading tool in Exercise 3.
4. Build a small two-agent workflow in Exercise 4.
5. Replace the manual workflow with a Crew in Exercise 5.
6. Discuss hallucinations, evaluation, failure handling, and human oversight.

## Repository Structure

```text
AgenticAI-Workshop-Part1/
├── README.md
├── requirements.txt
├── .gitignore
├── exercises/
│   ├── 01_first_agent/
│   │   └── agent.py
│   ├── 02_agent_task/
│   │   ├── README.md
│   │   └── agent_with_task.py
│   ├── 03_agent_tool/
│   │   ├── README.md
│   │   └── agent_with_tool.py
│   ├── 04_specialized_agents/
│   │   ├── README.md
│   │   └── multi_agent_workflow.py
│   └── 05_create_crew/
│       ├── README.md
│       └── crew.py
├── data/
│   └── sample_data.txt
└── solutions/
    ├── 01_first_agent.py
    ├── 02_agent_task.py
    ├── 03_agent_tool.py
    ├── 04_specialized_agents.py
    └── 05_create_crew.py
```

## Workshop Philosophy

You do not need to memorize CrewAI syntax. Focus on the architecture:

**Agent → Task → Tool → Multiple Agents → Crew**

Ask why each component exists and what capability it adds.

## Troubleshooting

### Ollama connection error

Make sure Ollama is running and that the model is available:

```bash
ollama list
```

If needed:

```bash
ollama pull llama3.2
```

### Python version

This workshop is designed for Python 3.11.

### Import errors

Make sure the virtual environment is activated and dependencies are installed:

```bash
pip install -r requirements.txt
```

## Important

The `solutions/` directory contains completed versions for reference. Try the exercises yourself before looking at the solutions.
