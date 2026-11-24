from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from pydantic import BaseModel



llm = ChatOllama(model="llama3.2:1b")


def generateRes(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }

def getWorkflow():
    graph = StateGraph(MessagesState)

    graph.add_node("generateRes", generateRes)

    graph.add_edge(START, "generateRes")
    graph.add_edge("generateRes", END)

    return graph.compile()


workflow = getWorkflow()