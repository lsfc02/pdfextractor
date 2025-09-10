import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Prompt fixo para todos os PDFs
DEFAULT_PROMPT = """
Organize os dados em JSON com os campos: nome, valor, data.
Devolva apenas em JSON válido.
Campos: nome, valor, data e se tiver, retorne CPF (não confundir com matrículas, apenas se for realmente CPF).
"""

def structure_text_with_ai(raw_text: str) -> dict:
    prompt = f"""
    Extraia os dados do documento abaixo e devolva em JSON válido.
    Seja rigoroso para não inventar valores.

    Documento:
    {raw_text}

    {DEFAULT_PROMPT}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response["choices"][0]["message"]["content"]
    usage = response.get("usage", {})  # pega os tokens gastos

    try:
        parsed = json.loads(content)
    except:
        parsed = {"raw_response": content}

    return {
        "data": parsed,
        "usage": {
            "prompt_tokens": usage.get("prompt_tokens", 0),
            "completion_tokens": usage.get("completion_tokens", 0),
            "total_tokens": usage.get("total_tokens", 0)
        }
    }
