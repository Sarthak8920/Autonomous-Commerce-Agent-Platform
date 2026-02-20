from langgraph.graph import StateGraph, END
from app.schemas import AgentState

from app.agents.intent_router import intent_router
from app.agents.catalog_agent import catalog_agent
from app.agents.order_agent import order_agent
from app.agents.payment_agent import payment_agent
from app.agents.policy_agent import policy_agent
from app.agents.resolution_agent import resolution_agent

# ---------------- GRAPH INIT ----------------
workflow = StateGraph(AgentState)

# ---------------- NODES ----------------
workflow.add_node("intent", intent_router)
workflow.add_node("catalog", catalog_agent)
workflow.add_node("order", order_agent)
workflow.add_node("payment", payment_agent)
workflow.add_node("policy", policy_agent)
workflow.add_node("resolve", resolution_agent)

# ---------------- ENTRY ----------------
workflow.set_entry_point("intent")

# ---------------- CONDITIONAL ROUTING ----------------
def route_by_intent(state: AgentState):
    intent = state.get("intent", "")

    if intent == "catalog":
        return "catalog"
    elif intent == "order":
        return "order"
    elif intent == "payment":
        return "payment"
    else:
        # multiple or unknown → run all
        return ["catalog", "order", "payment"]

workflow.add_conditional_edges(
    "intent",
    route_by_intent,
)

# ---------------- MERGE TO POLICY ----------------
workflow.add_edge("catalog", "policy")
workflow.add_edge("order", "policy")
workflow.add_edge("payment", "policy")

# ---------------- FINAL ----------------
workflow.add_edge("policy", "resolve")
workflow.add_edge("resolve", END)

# ---------------- COMPILE ----------------
app = workflow.compile()