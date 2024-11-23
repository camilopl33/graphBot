def stream_graph_updates(user_input: str, graph, config=None):
    for event in graph.stream(
        {"messages": [("user", user_input)]}, config, stream_mode="values"
    ):
        event["messages"][-1].pretty_print()
