from app.llm import llm

def resolution_agent(state: dict):
    context = f"""
Payment: {state.get('payment_result')}
Order: {state.get('order_result')}
Catalog: {state.get('catalog_result')}
Policy: {state.get('policy_result')}
"""

    response = llm.invoke(
        f"Generate a professional customer support response using the following data:\n{context}"
    )

    return {"final_answer": response.content}