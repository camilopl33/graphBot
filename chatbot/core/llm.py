from langchain_anthropic import ChatAnthropic
from chatbot.core.tools import tools

from chatbot.config import ANTHROPIC_MODEL, ANTHROPIC_API_KEY

# LLM SETUP
llm = ChatAnthropic(model=ANTHROPIC_MODEL, api_key=ANTHROPIC_API_KEY)
llm_with_tools = llm.bind_tools(tools)
