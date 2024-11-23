def generate_graph(graph):
    try:
        mermaid_png = graph.get_graph().draw_mermaid_png()

        with open("chatbot_graph.png", "wb") as image_file:
            image_file.write(mermaid_png)
        print("Graph saved as 'chatbot_graph.png' in the root directory.")

    except Exception as e:
        print("Error generating graph:", str(e))
