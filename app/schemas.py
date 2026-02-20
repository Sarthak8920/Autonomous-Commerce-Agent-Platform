from typing import TypedDict, Optional

class AgentState(TypedDict):
    query: str
    intent: Optional[str]

    catalog_result: Optional[str]
    order_result: Optional[str]
    payment_result: Optional[str]
    policy_result: Optional[str]

    final_answer: Optional[str]