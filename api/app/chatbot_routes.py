from fastapi import APIRouter, HTTPException, Depends
from api.schemas.chatbot_schemas import PromptRequest, Conversation
from api.app.user_routes import oauth2_scheme, header_auth
from google import genai
from google.genai.types import GenerateContentConfig, GoogleSearch
from dotenv import load_dotenv
from sqlalchemy.orm import session
import os
from api.database.connection import get_db
from api.services.chat_service import create_conversation_service

load_dotenv()

gemini_api_key = os.environ.get("API_KEY")

client = genai.Client(api_key=gemini_api_key)

chatbot_router = APIRouter()


@chatbot_router.post("/generate_chat")
def generate_chat(
    request: PromptRequest,
    token: str = Depends(header_auth),
    db: session = Depends(get_db)
):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Gere um título para esse prompt {request.prompt}. Independentemente do tamanho do prompt. 
        Público alvo: investidores, tom: Educacional. Evite um título grande, apenas algumas palavras.
        Preciso guardar esse título em uma variável, então, crie o título e envie apenas ele, SEM NENHUM TEXTO JUNTO."""
    )

    conversation = Conversation()
    conversation.title = response.text

    if request.prompt == "Bitcoin":

        conversation.title = "Valor do Bitcoin"
        conversation = create_conversation_service(db=db, conversation=conversation, token=token)


        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Valor atual do Bitcoin, mesmo que não seja o exato, diga o valor mais aproxiamdo que puder",
            config=GenerateContentConfig(
                tools=[GoogleSearch]
            )
        )

        return response.text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.prompt
    )

    conversation = create_conversation_service(db=db, conversation=conversation, token=token)

    return response.text