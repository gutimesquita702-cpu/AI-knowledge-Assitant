import os
from google import genai


def gerar_resposta(pergunta: str, contexto: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Defina a variável de ambiente GEMINI_API_KEY para usar o Gemini.")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""Você é um assistente de conhecimento especializado e preciso.
Responda à pergunta usando estritamente as informações do contexto abaixo.
Não invente nem use conhecimentos externos.
Se a resposta não estiver no contexto, responda apenas:
"Desculpe, não encontrei essa informação no documento."
Seja direto, claro e objetivo.

Contexto:
{contexto}

Pergunta:
{pergunta}

Resposta:""",
    )
    if response.text is None:
        raise RuntimeError("O Gemini não retornou uma resposta em texto.")
    return response.text
