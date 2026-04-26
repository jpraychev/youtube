# Build an AI agent

0. Prerequisites

```
# Python >= 3.10
# Google AI Studio API key
```

1. Install google's ADK in a virtual environment

```
python -m venv venv

# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1

pip install google-adk
```

2. Create the project

```
adk create my_agent
```

3. Explore the project you've just created

When exploring the project, you will see a single file called agent.py which hold the source code
for your AI agent. Looking at the code its not much but it is a starting point.

```
my_agent
├── __init__.py
└── agent.py

# agent.py
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
```

4. Start the agent

```
adk web
```

Once you start the agent you should navigate to `http://127.0.0.1:8000` and see the following welcome screen.