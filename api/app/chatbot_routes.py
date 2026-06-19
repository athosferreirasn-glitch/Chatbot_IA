from fastapi import APIRouter, HTTPException, Depends
from api.exceptions import custom_exception as exc
from fastapi.exceptions import ResponseValidationError
from api.schemas.chatbot_schemas import PromptRequest, Conversation
from api.app.user_routes import header_auth
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.services.chat_service import create_conversation_service
from api.services.ai_service import generate_title_conversation


chatbot_router = APIRouter()


@chatbot_router.post("/create_conversation")
def create_conversation(
    request: PromptRequest,
    token: str = Depends(header_auth),
    db: session = Depends(get_db)
    ):

    try:
        conversation = Conversation()

        conversation.title = generate_title_conversation(prompt=request.prompt)

        conversation = create_conversation_service(
            db=db, 
            conversation=conversation, 
            token=token
            )

        return HTTPException(
            status_code=200,
            detail="Conversa criada e registrada"
        )

    except ResponseValidationError:
        raise exc.ResponseError()