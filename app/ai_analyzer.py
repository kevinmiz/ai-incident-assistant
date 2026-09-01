import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors


def build_incident_prompt(incident, category, severity, errors):
    error_text = "\n".join(
        f"{error['timestamp']} {error['level']} {error['message']}"
        for error in errors
    )

    prompt = f"""
You are an IT Operations Incident Analyst.

Analyze the following incident and application logs.

INCIDENT:
{incident}

SYSTEM CLASSIFICATION:
Category: {category}
Severity: {severity}

ERROR LOGS:
{error_text}

Provide the following information:

1. Incident Summary
2. Category
3. Severity
4. Impact
5. Evidence
6. Possible Root Cause
7. Investigation Steps
8. Recommended Action
9. Escalation Recommendation

Important rules:
- Do not invent facts that are not present in the incident or logs.
- Clearly distinguish evidence from assumptions.
- If the root cause cannot be confirmed, state that it is a possible root cause.
- Recommendations should be practical for an IT Operations team.
"""

    return prompt


def analyze_with_ai(prompt):
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=api_key)
    
    try:
       interaction = client.interactions.create(
           model="gemini-3.6-flash",
           input=prompt
       )

       return interaction.output_text

    except errors.ServerError:
        return (
            "AI analysis temporarily unavailable. "
            "Gemini service returned a server error."
        )


    except errors.ClientError as error:
        return f"AI analysis unavailable due to API error: {error}"


    except Exception as error:
        return f"AI analysis failed unexpectedly: {error}"


if __name__ == "__main__":
    incident = "Payment API timeout causing transactions to fail"
    category = "Payment Service"
    severity = "SEV-2"
    errors = [
        {
            "timestamp": "2026-08-31 10:01:18",
            "level": "ERROR",
            "message": "Connection timeout"
        },
        {
            "timestamp": "2026-08-31 10:01:18",
            "level": "ERROR",
            "message": "Payment service unavailable"
        }
    ]

    prompt = build_incident_prompt(
        incident,
        category,
        severity,
        errors
    )

    print("Sending incident analysis to Gemini...")

    result = analyze_with_ai(prompt)

    print("\n=== AI INCIDENT ANALYSIS ===")
    print(result)
