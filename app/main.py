from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import app as graph_app

api = FastAPI(title="AURA-CX Multi-Agent AI")


class ChatRequest(BaseModel):
    query: str


# @api.post("/chat")
# def chat(request: ChatRequest):
#     result = graph_app.invoke({"query": request.query})
#     return {"response": result["final_answer"]}

@api.post("/chat")
def chat(request: ChatRequest):
    # IMPORTANT: create a NEW dict every time
    initial_state = {
        "query": request.query,
        "intent": None,
        "catalog_result": None,
        "order_result": None,
        "payment_result": None,
        "policy_result": None,
        "final_answer": None,
    }

    result = graph_app.invoke(initial_state)
    return {"response": result["final_answer"]}


@api.get("/")
def root():
    return {
        "message": "AURA-CX backend is running",
        "usage": {
            "chat": "POST /chat",
            "docs": "/docs"
        }
    }