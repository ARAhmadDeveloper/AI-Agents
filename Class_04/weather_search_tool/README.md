## Tavily Web Search Tool (with OpenAI Agents and Gemini)

This project implements a simple agent that can decide when to call a web search tool powered by Tavily. The agent runs on the OpenAI Agents SDK using the Chat Completions API, backed by Google's Gemini model. It also includes a few math function tools to demonstrate multi‑tool reasoning.

### Key Features

- **Agentic search**: The agent autonomously invokes a `search_web` tool (Tavily) when needed.
- **Multiple tools**: Includes math tools (`add`, `subtract`, `multiply`, `divide`, `power`) to show tool selection.
- **Async run**: Interacts via an async runner that prompts the user for input.

### How It Works

At a glance, the agent is created with:

- an OpenAI‑compatible client pointing at Gemini (`gemini-2.0-flash`),
- a set of function tools decorated with `@function_tool`, including `search_web` that calls Tavily,
- simple instructions and a name.

When you run the script, it asks for a prompt. The agent decides whether to answer directly, use math tools, or call Tavily search to gather web context.

### Project Structure

```text
weather_search_tool/
  ├─ main.py              # Agent, tools, and async runner
  ├─ pyproject.toml       # Python project and dependencies
  ├─ uv.lock              # Lockfile (if using uv)
  └─ README.md            # This file
```

### Requirements

- Python 3.12+
- API keys:
  - **GEMINI_API_KEY** (Google AI Studio / Gemini)
  - **TAVILY_API_KEY** (Tavily)

### Installation

You can use either `uv` or `pip`.

#### Option A: Using uv

```bash
# Install uv if needed (see https://docs.astral.sh/uv/)
uv venv
uv sync
```

#### Option B: Using pip

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
pip install -U pip
pip install -r <(python - <<PY
import tomllib, sys
from pathlib import Path
data = tomllib.loads(Path('pyproject.toml').read_text())
print('\n'.join(data['project']['dependencies']))
PY
)
```

Alternatively, install the two dependencies directly:

```bash
pip install openai-agents>=0.2.9 tavily-python>=0.7.11 python-dotenv
```

### Environment Variables

Create a `.env` file in the project root (or set environment variables in your shell):

```env
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Notes:

- `main.py` loads `.env` automatically via `python-dotenv`.
- Tavily usage requires a valid `TAVILY_API_KEY`.

### Run

```bash
python main.py
```

You will be prompted:

```text
Enter your prompt:
```

Try queries like:

- "What is the capital of Japan? Also square 12."
- "Summarize the latest news about quantum computing in 3 bullet points."
- "Calculate 23\*17 and then search for the winner of the 2023 World Chess Championship."

The agent will choose between answering directly, using math tools, or calling Tavily search.

### Implementation Notes

- **LLM client and model**: The code creates an OpenAI‑compatible async client pointed to the Gemini endpoint and selects the `gemini-2.0-flash` chat‑completions model.
- **Tools**: Functions are registered via `@function_tool`. The `search_web(query: str)` tool constructs a `TavilyClient` with `TAVILY_API_KEY` and returns the JSON search response.
- **Agent**: Built with `Agent(...)`, providing name, instructions, tools, and the model. Execution is handled by `Runner.run(...)` (async) with the user input.
- **Tracing**: Explicitly disabled in the code.

### Troubleshooting

- **Missing API keys**: Ensure `.env` contains `GEMINI_API_KEY` and `TAVILY_API_KEY` and that your shell session can read them if not using `.env`.
- **HTTP/401 or 403**: Double‑check both keys and that they’re active.
- **SSL/Network issues**: Verify internet access and that no proxy/firewall is blocking requests.
- **Model errors**: Ensure the configured model (`gemini-2.0-flash`) is available to your key.

### Why Tavily?

Tavily provides fast, quality web search with a developer‑friendly API and structured results, making it ideal for agents that need just‑in‑time retrieval.


### Author

- Username: <arahmaddeveloper>
