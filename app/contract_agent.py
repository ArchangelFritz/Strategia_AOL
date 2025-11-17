# app/contract_agent.py

from openai import OpenAI
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_contract(filename: str, full_text: str):
    json_schema = """
{
  "contract_metadata": {
    "payor_name": "",
    "provider_name": "",
    "effective_date": "",
    "termination_date": "",
    "auto_renewal": "",
    "contract_type": ""
  },
  "economic_terms": {
    "reimbursement_methodology": "",
    "rate_schedule_or_fee_basis": "",
    "claims_payment_timeline": "",
    "value_based_or_bonus_programs": "",
    "capitation_terms": "",
    "risk_adjustment_factors": ""
  },
  "operational_terms": {
    "authorization_requirements": "",
    "timely_filing_limits": "",
    "audit_rights_and_recoupment_terms": "",
    "network_access_or_steerage_terms": "",
    "provider_obligations": "",
    "dispute_resolution_process": ""
  },
  "compliance_terms": {
    "HIPAA_and_data_requirements": "",
    "quality_reporting_requirements": "",
    "termination_without_cause_notice_period": "",
    "most_favored_nation_or_parity_clauses": "",
    "delegation_or_subcontracting_limits": ""
  }
}
"""

    prompt = f"""
You are Strategia Systems' Contract Intelligence Agent.

Your task is to perform a deep, structured contract analysis of the payer contract below.

STRICT RULES:
- Return ONLY a JSON object.
- JSON must be syntactically valid.
- No trailing commas.
- No explanations before or after the JSON.
- Use null for anything not explicitly stated.
- Keep values concise (1-2 sentences maximum).
- Pretty-print the JSON.

Return your answer with the following JSON structure:

{json_schema}

CONTRACT FILENAME:
{filename}

CONTRACT TEXT:
{full_text}

Begin your analysis now.
"""

    completion = client.responses.create(
        model="gpt-4.1",
        input=prompt,
    )

    return completion.output_text
