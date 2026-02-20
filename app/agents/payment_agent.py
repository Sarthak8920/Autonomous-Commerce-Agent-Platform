from app.tools.payment_tools import get_payment_status

def payment_agent(state: dict):
    return {"payment_result": get_payment_status("ORDER123")}