from langchain_core.prompts import ChatPromptTemplate
from app.llm import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intent classification agent for an e-commerce platform."),
    ("human", "{query}\n\nClassify intent as: catalog, order, payment, multiple. Return only one word.")
])

def intent_router(state: dict):
    response = llm.invoke(prompt.format_messages(query=state["query"]))
    return {"intent": response.content.strip().lower()}