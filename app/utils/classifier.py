# app/utils/classifier.py

def classify_query(query: str) -> str:
    q = query.lower()

    # ------------------------------
    # HR
    # ------------------------------
    if any(w in q for w in [
        "benefit", "hiring", "recruit", "employee", "vacation", "pto", "hr", "human resources"
    ]):
        return "HR"

    # ------------------------------
    # Supply Chain
    # ------------------------------
    if any(w in q for w in [
        "inventory", "purchase", "supply", "supplier", "vendor", "materials", "procurement"
    ]):
        return "Supply Chain"

    # ------------------------------
    # Surgical Operations
    # ------------------------------
    if any(w in q for w in [
        "surgery", "surgical", "or room", "sterile", "case volume", "surgeon"
    ]):
        return "Surgical Operations"

    # ------------------------------
    # RCM (Revenue Cycle Management)
    # ------------------------------
    if any(w in q for w in [
        "authorization", "claims", "denial", "billing", "charge", "rcm", "collections"
    ]):
        return "RCM"

    # ------------------------------
    # Finance
    # ------------------------------
    if any(w in q for w in [
        "budget", "cost", "accounting", "financial", "forecast", "revenue", "expense"
    ]):
        return "Finance"

    # ------------------------------
    # Payer Contracting
    # ------------------------------
    if any(w in q for w in [
        "payer", "payor", "mco", "reimbursement", "contract rate", "allowed amount"
    ]):
        return "Payer Contracting"

    # ------------------------------
    # Compliance
    # ------------------------------
    if any(w in q for w in [
        "audit", "regulation", "hipaa", "policy", "compliance", "violation"
    ]):
        return "Compliance"

    # ------------------------------
    # Risk Management
    # ------------------------------
    if any(w in q for w in [
        "risk", "incident report", "safety", "liability"
    ]):
        return "Risk Management"

    # ------------------------------
    # Administration
    # ------------------------------
    if any(w in q for w in [
        "admin", "administration", "office", "front desk
