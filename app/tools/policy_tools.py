from typing import Dict


# --- Mock policy database (replace with DB / vector store later) ---
POLICY_RULES = {
    "refund": {
        "max_days": 7,
        "payment_failure": True,
        "delivery_delay": True
    },
    "return": {
        "max_days": 10,
        "damaged_product": True,
        "wrong_item": True
    }
}


def check_refund_policy(order_days: int, payment_failed: bool) -> Dict:
    """
    Check refund eligibility based on platform policy.
    """
    if payment_failed and order_days <= POLICY_RULES["refund"]["max_days"]:
        return {
            "eligible": True,
            "reason": "Payment failed and refund requested within allowed timeframe."
        }

    return {
        "eligible": False,
        "reason": "Refund conditions not met as per policy."
    }


def check_return_policy(order_days: int, issue_type: str) -> Dict:
    """
    Check return eligibility based on issue type.
    """
    allowed_issues = ["damaged_product", "wrong_item"]

    if (
        issue_type in allowed_issues
        and order_days <= POLICY_RULES["return"]["max_days"]
    ):
        return {
            "eligible": True,
            "reason": f"Return allowed for issue: {issue_type}."
        }

    return {
        "eligible": False,
        "reason": "Return request does not satisfy policy conditions."
    }


def get_policy_summary() -> str:
    """
    Human-readable policy summary for LLM consumption.
    """
    return (
        "Refunds are allowed within 7 days for payment failures or delivery issues. "
        "Returns are allowed within 10 days for damaged or incorrect products."
    )