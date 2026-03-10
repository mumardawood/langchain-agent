# Research AI Agent
# using multiple tools

import os
import sys
from dotenv import load_dotenv

# LangChain
from langchain.agents import create_agent
from langchain.agents.middleware import (
    wrap_tool_call,
    ToolRetryMiddleware
) 
from langchain.messages import HumanMessage, AiMessage
from langchain.tools import tool

# LangChain Community
from langchain_community.tools import (
    DuckDuckGoSearchResults,
    WikipediaQueryRun,
    ArxivQueryRun
)
from langchain_community.utilities import (
    DuckDuckGoSearchAPIWrapper,
    WikipediaAPIWrapper,
    ArxizAPIWrapper
)

# LangGraph
from langgraph.checkpoint.memory import MemorySaver

# Model
from langchain_ollama import ChatOllama

# Load variables from the .env file into the environment
load_dotenv()

# Read configuration with sensible defaults
MODEL_NAME = os.getenv("MODEL_NAME", "minimax-m2.5")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TURNS = int(os.getenv("MAX_TURNS", "5"))

# LLM
# llm = ChatOllama(
#     model=MODEL_NAME,
#     temperature=TEMPERATURE
# )

# Research Tools 

ddgs_wrapper = DuckDuckGoSearchAPIWrapper(max_results=5)
web_search = DuckDuckGoSearchResults(
api_wrapper=ddgs_wrapper,
name= "web_search",
description=""

)

wiki_warpper = WikipediaAPIWrapper(top_k_results=3, )
wiki = WikipediaQueryRun(
    api_wrapper=wiki_warpper,
    name="wikipedia",
    description=""
)

arxiv_wrapper = ArxizAPIWrapper(top_k_result=3, doc_content_chars_max=2000)
arxiv_tool = ArxivQueryRun(
    api_wrapper=arxiv_wrapper,
    name="wikipedia",
    description=""
)

def get_current_datetime():
    """""""
    now_datetime = datetime.now()
    return now_datetime.strftime("")