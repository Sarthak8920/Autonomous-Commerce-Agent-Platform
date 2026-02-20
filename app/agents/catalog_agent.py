from app.tools.catalog_tools import suggest_alternatives

def catalog_agent(state: dict):
    return {"catalog_result": suggest_alternatives("mobile")}