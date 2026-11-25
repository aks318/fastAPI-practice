from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from pydantic import BaseModel
from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = "postgresql://aakash:Aakash@123@localhost:5432/chatbot"



llm = ChatOllama(model="llama3.2:1b")


def generateRes(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }

def getWorkflow(checkpointer):
    graph = StateGraph(MessagesState)

    graph.add_node("generateRes", generateRes)

    graph.add_edge(START, "generateRes")
    graph.add_edge("generateRes", END)

    return graph.compile(checkpointer=checkpointer)

