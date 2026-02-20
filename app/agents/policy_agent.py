from app.tools.policy_tools import check_refund_policy

def policy_agent(state: dict):
    # derive conditions from previous agents
    payment_failed = False
    order_days = 2  # later: derive from order DB

    if state.get("payment_result"):
        payment_failed = "deducted" in state["payment_result"].lower()

    policy = check_refund_policy(
        order_days=order_days,
        payment_failed=payment_failed
    )

    return {
        "policy_result": (
            f"Eligible: {policy['eligible']}. "
            f"Reason: {policy['reason']}"
        )
    }