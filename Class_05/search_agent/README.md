# Search Agent

A web search agent built with OpenAI Agents that can search the internet for information using the Tavily API.

## Setup

1. **Install dependencies:**

   ```bash
   uv sync
   ```

2. **Create a `.env` file in the project root with your API keys:**

   ```env
   # Choose one of these:
   OPENAI_API_KEY=your_openai_api_key_here
   # OR
   GEMINI_API_KEY=your_gemini_api_key_here

   # Required for web search:
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

3. **Get API Keys:**
   - **OpenAI**: [Get your API key here](https://platform.openai.com/api-keys)
   - **Gemini**: [Get your API key here](https://makersuite.google.com/app/apikey)
   - **Tavily**: [Get your API key here](https://tavily.com/)

## Usage

Run the agent:

```bash
python main.py
```

The agent will search for information about "Who is Messi?" using the web search tool.

## Features

- Web search using Tavily API
- Support for both OpenAI and Gemini models
- Error handling and validation
- Environment variable configuration
