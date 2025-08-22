from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, set_default_openai_api, set_default_openai_client, function_tool
import os
import asyncio
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

set_default_openai_api("chat_completions")
gemini_api_key = os.environ.get("GEMINI_API_KEY")


# Tracing disabled
set_tracing_disabled(disabled=True)

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)


# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


# Agent -? llm_model -?
# 1. can it be configured at run time? INstead of at agent creation time?
# 2. can it be configured once globally?


# config = RunConfig(
#     model=llm_model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

@function_tool
def add(x: int, y: int) -> int:
    print(f"Adding {x} and {y}")
    return x + y

@function_tool
def subtract(x: int, y: int) -> int:
    print(f"Subtracting {y} from {x}")
    return x - y

@function_tool
def multiply(x: int, y: int) -> int:
    print(f"Multiplying {x} and {y}")
    return x * y

@function_tool
def divide(x: int, y: int) -> int:
    print(f"Dividing {x} by {y}")
    return x / y

@function_tool
def power(x: int, y: int) -> int:
    print(f"Raising {x} to the power of {y}")
    return x ** y



math_agent: Agent = Agent(
    name="Alex - Math Genius Agent",
    instructions="You are a helpful math assistant.",
    # model="gemini-2.0-flash",
    tools=[add, subtract, multiply, divide, power],
    model=llm_model,
) # gemini-2.5 as agent brain - chat completions


# Run Agents in Sync Mode
# math_agent: Agent = Agent(name="HistoryAgent",
#                      instructions="You are a helpful History assistant.",
#                      model=llm_model) # gemini-2.5 as agent brain - chat completions

# result: Runner = Runner.run_sync(math_agent, "What are the fourteen points of Muhammad Ali Jinnah?")

# print("\nCALLING AGENT\n")
# print(result.final_output)



# Run Agents in Async Mode
async def Calling_Agent():
    get_user_input = input("Enter your prompt: ")

    result: Runner = await Runner.run(
        starting_agent=math_agent, 
        input=get_user_input,
    )

    print("\nCALLING AGENT\n")
    print(result.final_output)
    
asyncio.run(Calling_Agent())



# There are 3 types of Tools in OpenAI Agents
# 1. Hosted Tools: These are tools that are hosted on the OpenAI platform. They can be used by any agent.
# 2. Function Tools: These are tools that are defined as functions and can be used by any agent.
# 3. Agents as Tools: These are tools that are defined as agents and can be used by any agent.