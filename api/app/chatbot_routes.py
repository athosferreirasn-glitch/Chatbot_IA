from fastapi import APIRouter, HTTPException, Depends
from api.exceptions import custom_exception as exc
from fastapi.exceptions import ResponseValidationError
from api.schemas.chatbot_schemas import Conversation, Message
from api.app.user_routes import header_auth
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.services.chat_services.conversation_service import create_conversation_service
from api.services.chat_services.messages_service import register_message_service

chatbot_router = APIRouter()


def create_conversation(
    request: str,
    token: str = Depends(header_auth),
    db: session = Depends(get_db)
    ):

    try:
        conversation = Conversation()

        conversation = create_conversation_service(
            db=db, 
            conversation=conversation, 
            token=token,
            request=request
            )

        return conversation

    except ResponseValidationError:
        raise exc.ResponseError()



@chatbot_router.post("/new_chat")
def generate_new_chat(
    message: Message,
    conversation_uuid = None,
    token: str = Depends(header_auth),
    db: session = Depends(get_db)
):
    try:

        message._role = "user"

        message = register_message_service(
            db=db, 
            message=message, 
            conversation_uuid=conversation_uuid, 
            token=token
            )

    except ResponseValidationError:
        raise exc.ResponseError()