from langchain_core.tools import tool


@tool
def get_favorite_food(name: str):
    """
    Get the favorite food of the user.
    """
    MOCK_DB = {
        "Alice": "Pizza",
        "Bob": "Pasta",
        "Charlie": "Burger",
        "David": "Sushi",
    }

    try:
        return MOCK_DB[name]
    except KeyError:
        return "I don't know your favorite food. Please tell me!"


tools = [get_favorite_food]
