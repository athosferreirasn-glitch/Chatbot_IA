from fastapi import APIRouter, HTTPException, Depends
from api.exceptions import custom_exception as exc
from fastapi.exceptions import ResponseValidationError
from api.schemas.chatbot_schemas import Conversation, Message, PromptRquest
from api.app.user_routes import header_auth
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.services.chat_services.conversation_service import create_conversation_service
from api.services.ai_service import response_for_prompt
from api.services.chat_services.messages_service import register_message_user_service, register_message_AI_service

chatbot_router = APIRouter()

@chatbot_router.post("/new_chat")
def generate_new_chat(
    request: PromptRquest,
    conversation_id: str = None,
    token: str = Depends(header_auth),
    db: session = Depends(get_db)
    ) -> dict:

    try:
        response = response_for_prompt(
            db=db, 
            request=request, 
            conversation_id=conversation_id
            ) 

        
        if request:
            message = Message()

            message.role = "user"

            message.content = request.prompt

            message_user = register_message_user_service(
                db=db, 
                message=message, 
                conversation_uuid=conversation_id, 
                token=token
                )

        if response:

            message = Message()

            message.role = "AI"

            message.content = response.choices[0].message.content

            message = register_message_AI_service(
                db=db, 
                message=message, 
                conversation_uuid=message_user.conversation_id, 
                token=token
                )

            return {
                "conversation_id": message.conversation_id,
                "response": response.choices[0].message.content
            }
    
    except ResponseValidationError:
        raise exc.ResponseError()