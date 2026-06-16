from fastapi import HTTPException
import uuid
from api.security.jwt_handler import decode_token
from api.utils.utils import register_created_conversation
from api.database.repository.chats_repositories import create_conversation_repo


def create_conversation_service(db, conversation, token):
    
    conversation.uuid = uuid.uuid4()

    conversation.user_id = uuid.UUID(decode_token(token=token)["sub"])

    conversation.created_at = register_created_conversation(conversation=conversation)

    conversation.update_at = register_created_conversation(conversation=conversation)

    return create_conversation_repo(db=db, conversation=conversation)