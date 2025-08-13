## Class 02 — APIs with Python (Hands‑on)

A compact walkthrough of calling public APIs with `requests` and using Google Generative AI (Gemini) from Python, via a notebook and a script.

### Table of Contents

- **Overview**
- **What’s included**
- **Quick start (TL;DR)**
- **Configuration**
- **API demos**
- **How to run**
- **Troubleshooting**
- **Next steps**
- **Credits**

## Overview

Learn how to:

- Call REST APIs, handle errors, and parse JSON
- Work with Gemini for text, chat (stateful), and multimodal prompts
- Keep API keys secure across Colab and local environments

## What’s included

- `api_basics_demo.ipynb`: step‑by‑step Colab notebook
- `api_basics_demo.py`: Python script mirroring the notebook’s core ideas

## Quick start (TL;DR)

```bash
# 1) Install deps
pip install requests google-genai openai

# 2) Set your key (Windows)
setx GEMINI_API_KEY "<your_key_here>"
# restart shell after setx

# 3) Run the script
python api_basics_demo.py
```

In Colab, use the notebook and store `GEMINI_API_KEY` in Colab secrets.

## Configuration

- **Colab**: `from google.colab import userdata` then `userdata.get('GEMINI_API_KEY')`
- **Local**: use an environment variable `GEMINI_API_KEY`
  - Windows (cmd): `setx GEMINI_API_KEY "<key>"`
  - macOS/Linux: `export GEMINI_API_KEY="<key>"`

Keep keys out of source control. Prefer environment variables or secret managers.

## API demos

### 1) Weather (Open‑Meteo) with `requests`

```python
import requests, pprint
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
resp = requests.get(url, timeout=10)
resp.raise_for_status()
weather = resp.json()
pprint.pp(weather)
```

Key ideas: timeouts, `raise_for_status()`, `resp.json()`.

### 2) Cat Fact API

```python
resp = requests.get("https://catfact.ninja/fact", timeout=10)
resp.raise_for_status()
print(resp.json()["fact"])
```

### 3) Gemini text generation (`google-generativeai`)

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
print(model.generate_content("Say hello!").text)
```

### 4) Multimodal prompt (image + text)

```python
import requests, google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content([
    "what is in this image?",
    {"mime_type": "image/jpeg", "data": requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg").content}
])
print(response.text)
```

### 5) Stateful chat

```python
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
chat = genai.GenerativeModel("gemini-2.5-flash").start_chat(history=[])
print(chat.send_message("hello").text)
# later
# print(chat.send_message("What did I just say?").text)
```

### 6) OpenAI‑compatible client for Gemini

```python
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
resp = client.chat.completions.create(model="gemini-2.5-flash", messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain AI simply."}
])
print(resp.choices[0].message.content)
```

## How to run

- **Notebook (recommended to explore):**
  1. Open `api_basics_demo.ipynb` in Colab
  2. Add `GEMINI_API_KEY` to Colab secrets
  3. Run cells top‑to‑bottom (weather, cat facts, Gemini text/image)
- **Script:**
  1. Install deps and set `GEMINI_API_KEY`
  2. `python api_basics_demo.py`

## Troubleshooting

- **401/403 unauthorized**: key missing/invalid; confirm `GEMINI_API_KEY` is set and shell was restarted (Windows `setx` needs a new session).
- **Timeout / connection errors**: check internet, retry, or increase `timeout`.
- **Colab `userdata` locally**: replace with `os.environ.get("GEMINI_API_KEY")` when not in Colab.
- **Model names change**: list models and pick an available one:

```python
import google.generativeai as genai
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
```

## Next steps

- Add retries/backoff around HTTP calls
- Cache API responses during development
- Explore streaming responses and tool/function calling
- Add tests for API wrappers

## Credits

Based on the Colab at `https://colab.research.google.com/github/panaversity/learn-agentic-ai/blob/main/01_ai_agents_first/02_what_is_api/api_basics_demo.ipynb`.

---

— arahmaddeveloper
