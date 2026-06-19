import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig, GoogleSearch
from google.genai.errors import ServerError
from api.exceptions import custom_exception as exc


load_dotenv()

gemini_api_key = os.environ.get("API_KEY")

client = genai.Client(api_key=gemini_api_key)


def generate_title_conversation(prompt: str) -> str:
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Você é um gerador de títulos para conversas.

Sua única função é analisar o conteúdo de uma conversa e criar um título curto, claro e descritivo que represente o assunto principal discutido.

Regras:

1. O título deve ter entre 3 e 8 palavras.
2. Seja objetivo e específico.
3. Identifique o tema principal da conversa, não detalhes secundários.
4. Não utilize aspas, emojis, hashtags ou pontuação desnecessária.
5. Não escreva explicações, comentários ou texto adicional.
6. Retorne apenas o título.
7. Se a conversa abordar múltiplos assuntos, escolha o tema predominante.
8. Prefira títulos que facilitem a organização e busca futura das conversas.
9. Use linguagem natural em português.
10. Evite títulos genéricos como:
   - Conversa sobre programação
   - Ajuda com código
   - Pergunta sobre investimento

Exemplos:

Conversa:
"Estou recebendo um erro 503 ao chamar a API do Gemini."

Resposta:
Erro 503 na API Gemini

Conversa:
"Quero montar uma carteira de investimentos focada em dividendos."

Resposta:
Carteira de Dividendos

Conversa:
"Meu token JWT está retornando Not enough segments."

Resposta:
Erro JWT Not Enough Segments

Conversa:
"Qual Xiaomi vale mais a pena até R$ 1.300?"

Resposta:
Melhor Xiaomi até R$ 1300

Analise a conversa fornecida e gere apenas o título: {prompt}"""
        )

        return response.text
    
    except ServerError:
        raise exc.ErrorAPIAi()