from langgraph.graph import StateGraph, START, END

from chatbot.models.commons.state import State
from chatbot.nodes.basicToolNode import BasicToolNode
from chatbot.utils.generate_graph import generate_graph
from chatbot.utils.stream_graph import stream_graph_updates
from chatbot.nodes.chatbotNode import chatbot
from chatbot.utils.route_tools import route_tools
from chatbot.core.tools import tools
from chatbot.core.memory import memory

# GRAPH SETUP
graph_builder = StateGraph(State)

tool_node = BasicToolNode(tools=tools)

# GRAPH SETUP
graph_builder.add_edge(START, "chatbot")

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge("chatbot", END)

# Manage routing to the tool node
graph_builder.add_conditional_edges(
    "chatbot",
    route_tools,
    {"tools": "tools", END: END},
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")


# COMPILE GRAPH
graph = graph_builder.compile(checkpointer=memory)

# GENERATE GRAPH IMAGE
generate_graph(graph)

# EXAMPLE CONFIG
config = {"configurable": {"thread_id": "1"}}

# EXAMPLE USAGE
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input, graph, config)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input, graph, config)
        break
