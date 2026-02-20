from app.tools.order_tools import get_order_status

def order_agent(state: dict):
    return {"order_result": get_order_status("ORDER123")}