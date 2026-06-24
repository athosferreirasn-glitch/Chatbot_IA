import os
from uuid import UUID
from sqlalchemy.orm import session
from dotenv import load_dotenv
from api.exceptions import custom_exception as exc
from groq import Groq
from groq._exceptions import APIError


load_dotenv()

groq_api_key = os.environ.get("API_KEY")

model = os.environ.get("MODEL")

client = Groq(api_key=groq_api_key)


def generate_title_conversation(prompt: str) -> str:
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                "role": "user",
                "content": f"Você é um gerador de títulos para conversas. Analise a conversa fornecida e gere apenas o título: {prompt}"
                }
            ]       
        )

        return response.choices[0].message.content
    
    except ServerError:
        raise exc.ErrorAPIAi()



def response_for_prompt(
    db: session, 
    request: object, 
    conversation_id: str = None
    ) -> object:

    try:

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                "role": "user",
                "content": f'Responda o prompt de forma objetiva. Prompt: {request.prompt}'
                }
            ]
        )

        return response

    except APIError:
        raise exc.ErrorAPIAi()