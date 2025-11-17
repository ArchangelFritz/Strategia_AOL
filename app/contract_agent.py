# app/contract_agent.py

from openai import OpenAI
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_contract(filename: str, full_text: str):
    prompt = f"""
You are Strategia Systems' Contract Intelligence Agent.

Your task is to perform a deep, structured contract analysis of the payer contract below.

Return your answer in JSON with the following fields:

- summary                : High level summary
- reimbursement_terms    : Detailed breakdown of reimbursement methodology
- carve_outs             : List of carve-outs or special conditions
- red_flags              : Potential risks or unusual terms
- term_and_termination   : Contract duration, renewal, & termination clauses
- obligations            : Key obligations for provider and payer
- rate_escalators        : Any rate changes or escalators
- credentialing_requirements : Any credentialing or eligibility rules
- appeal_and_dispute     : Appeal / dispute resolution process

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
