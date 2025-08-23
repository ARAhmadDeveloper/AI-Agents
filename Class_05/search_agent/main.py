from agents import Agent, Runner, set_tracing_disabled,AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv, find_dotenv
import os

import requests
from tavily import TavilyClient

# Gemini LLm
# tavily for web search

load_dotenv(find_dotenv())
set_tracing_disabled(True)

gemini_api_key = os.environ.get("GEMINI_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")


# provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

llm_model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash",
)

# web_search_tool with the help of Tavily
@function_tool
def web_search_tool(query: str) -> str:
    print(f"Searching the web for: {query}")
    tavily_client = TavilyClient(api_key=tavily_api_key)
    response = tavily_client.search(query)
    return response




agent: Agent = Agent(
    name="Web Search Agent",
    instructions="You are a web search agent. You are given a query and you need to search the web for the information.",
    model=llm_model,
    tools=[web_search_tool],
    
)

runner = Runner.run_sync(agent, "what is the latest llm model released by china?")

print(runner.final_output)
