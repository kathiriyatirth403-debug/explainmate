import json
import boto3

bedrock = boto3.client("bedrock-runtime")
MODEL_ID = "amazon.nova-micro-v1:0"

SYSTEM_PROMPT = """You are ExplainMate, a warm, friendly senior developer who explains code
to students and beginners. Rules:
- Explain in plain, simple language. No jargon dumps.
- Structure: (1) one-line summary, (2) step-by-step walkthrough, (3) a tiny real-world analogy.
- Be encouraging and kind — the reader is learning.
- End with a "Confidence Meter" line (a clarity % between 85-99) and ONE short motivating sentence.
Keep it concise. Never rewrite the code unless asked."""


def explain_code(snippet, language="auto"):
    user_msg = f"Explain this {language} code to a beginner:\n\n```\n{snippet}\n```"
    resp = bedrock.converse(
        modelId=MODEL_ID,
        system=[{"text": SYSTEM_PROMPT}],
        messages=[{"role": "user", "content": [{"text": user_msg}]}],
        inferenceConfig={"maxTokens": 800, "temperature": 0.5},
    )
    return resp["output"]["message"]["content"][0]["text"]


def lambda_handler(event, context):
    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body or "{}")
        elif body is None:
            body = event

        snippet = (body or {}).get("code", "").strip()
        language = (body or {}).get("language", "auto")

        if not snippet:
            return _resp(400, {
                "error": "No code provided",
                "hint": "Send JSON like {\"code\": \"print(1+1)\"}"
            })

        explanation = explain_code(snippet, language)
        return _resp(200, {"explanation": explanation})

    except Exception as e:
        return _resp(500, {
            "error": "Oops! ExplainMate tripped over something.",
            "detail": str(e),
            "hint": "Check that Bedrock model access is enabled for Nova in this region."
        })


def _resp(status, payload):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(payload),
    }