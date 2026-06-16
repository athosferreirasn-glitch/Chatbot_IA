from fastapi import APIRouter, HTTPException, Depends
from api.schemas.chatbot_schemas import PromptRequest, Conversation
from api.app.user_routes import oauth2_scheme
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
    token: str = Depends(oauth2_scheme),
    db: session = Depends(get_db)
):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Gere um título para esse prompt {request.prompt}"
    )

    conversation = Conversation
    conversation.title = response.text
    conversation = create_conversation_service(db=db, conversation=conversation, token=token)

    if request.prompt == "Bitcoin":

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Valor atual do Bitcoin",
            config=GenerateContentConfig(
                tools=[GoogleSearch]
            )
        )

        return response.text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.prompt
    )

    return response.text