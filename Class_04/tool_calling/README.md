## Tool Calling – Class 04

Leveling up with AI agents, structured function calls, and smooth developer workflows.

---

### What we learned today

- **Tool calling fundamentals**: Designing clear function schemas, validating inputs/outputs, and mapping model intents to deterministic actions.
- **Parallel execution**: Running independent tools concurrently to reduce latency and keep UX snappy.
- **Agent loop best practices**: Status updates, small reliable steps, and stopping criteria to avoid runaway loops.
- **Readable, safe code**: Guard clauses, explicit typing where it matters, and error handling that informs rather than obscures.
- **Project hygiene**: Keeping dependencies pinned (`uv`), linting early, and documenting decisions in the README.

---

### Quick start

```bash
# Create and activate a virtual environment (example)
uv venv && . .venv/bin/activate  # Windows PowerShell: . .venv/Scripts/Activate.ps1

# Install
uv pip install -r pyproject.toml

# Run
python main.py
```

---

### Project structure

```text
tool_calling/
  ├─ main.py            # Entry point
  ├─ pyproject.toml     # Project + dependencies
  ├─ uv.lock            # Locked, reproducible env
  └─ README.md          # You are here
```

---

### Notes and tips

- **Schemas first**: Start with precise tool/function contracts; implementation follows naturally.
- **Fail fast**: Validate inputs early; return helpful errors.
- **Log meaningfully**: Prefer structured logs for tool calls and results.
- **Keep it human**: Short, skimmable sections in docs help future you.

---

Made with curiosity and care.

— arahmaddeveloper
