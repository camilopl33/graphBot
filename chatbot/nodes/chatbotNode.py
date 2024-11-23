from chatbot.models.commons.state import State
from chatbot.core.llm import llm_with_tools


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}
