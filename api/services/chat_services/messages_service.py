from api.database.repository.chats_repositories import create_conversation_repo, register_message_repo
from api.utils.utils import register_created_message
import uuid


def register_message_service(db, message, conversation_uuid, token):

    message._uuid = uuid.uuid4()

    if not conversation_uuid:
        
        conversation = create_conversation(
            request=message.content, 
            db=db,
            token=token
            )

        message._conversation_id = conversation.id

    message._conversation_id = conversation_uuid

    message._created_at = register_created_message(message=message)

    message._conversation_id = uuid.UUID(message._conversation_id) 

    message = register_message_repo(db=db, message=message)

    return message