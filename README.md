# Crew AI Workshop Part 1

A hands-on workshop for building AI agents and multi-agent workflows using **CrewAI** and **Ollama**.

---

# Workshop Goal

By the end of Part 1, you will be able to:

* Create an AI agent
* Define an agent's role, goal, and backstory
* Assign tasks to an agent
* Give an agent a tool
* Create specialized agents
* Pass information between agents
* Build a multi-agent Crew

---

# 1. Before You Begin

Before starting the exercises, make sure the following are installed.

| Software | Required | Check Command |
| --- | --- | --- |
| Python 3.11 | Yes | `python --version` |
| Git | Yes | `git --version` |
| Ollama | Yes | `ollama --version` |

You will also need the `llama3.2` model in Ollama.

## Check Python

Run:

```bash
python --version
```

Python 3.11 is recommended for the workshop so everyone uses the same environment.

If `python` does not work on macOS/Linux, try:

```bash
python3 --version
```

## Check Git

```bash
git --version
```

## Check Ollama

```bash
ollama --version
```

If Ollama is not installed, download it from:

https://ollama.com

Then restart your terminal and run the command again.

## Check Your Ollama Model

Run:

```bash
ollama list
```

You should see `llama3.2` in the list.

If you do not have it, download it using:

```bash
ollama pull llama3.2
```

---

# 2. Test Ollama

Before continuing, make sure Ollama is working correctly.

Run:

```bash
ollama run llama3.2
```

Try asking:

```text
What is an AI agent?
```

If you receive a response, Ollama is working correctly.

To exit the Ollama session, use:

```text
/bye
```

or press `Ctrl+C`.

---

# 3. Clone the Repository

Run:

```bash
git clone https://github.com/ShreyaKunda/AgenticAI-Workshop-Part1.git
cd AgenticAI-Workshop-Part1
```

You should see files and folders such as:

```text
README.md
requirements.txt
exercises
data
solutions
```

---

# 4. Create a Virtual Environment

A virtual environment keeps the workshop dependencies separate from other Python projects.

## Windows

```bash
py -3.11 -m venv .venv
.venv\Scripts\activate
```

## macOS / Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

After activation, you should see `(.venv)` at the beginning of your terminal.

---

# 5. Install the Workshop Dependencies

Make sure your virtual environment is activated.

Then run:

```bash
pip install -r requirements.txt
```

This installs CrewAI for the workshop. Ollama runs separately as the local LLM provider.

You can verify CrewAI with:

```bash
pip show crewai
```

---

# 6. Run the Workshop Exercises

The exercises are located inside:

```text
exercises/
```

Start with Exercise 1 and follow the exercises in order. Each exercise introduces one new concept and builds toward creating a multi-agent Crew.

## Exercise Progression

```text
Exercise 1: Agent
       ↓
Exercise 2: Agent + Task
       ↓
Exercise 3: Agent + Tool
       ↓
Exercise 4: Agent → Agent
       ↓
Exercise 5: Multi-Agent Crew
```

Solutions are provided in the `solutions/` folder for reference after attempting each exercise.

---

# Workshop Philosophy

The exercises are intentionally small. The goal is to understand how agents, tasks, tools, and Crews fit together rather than simply copy a large application.
