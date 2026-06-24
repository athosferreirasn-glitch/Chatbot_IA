from api.database.repository.chats_repositories import register_message_repo
from api.utils.utils import register_created_message
from api.services.chat_services.conversation_service import create_conversation_service
import uuid
from api.schemas.chatbot_schemas import Conversation


def register_message_user_service(db, message, conversation_uuid, token):

    message.uuid = uuid.uuid4()

    if not conversation_uuid:

        conversation = Conversation()
        
        conversation = create_conversation_service(
            db=db, 
            conversation=conversation,
            request=message.content,
            token=token
        )

        message.conversation_id = conversation.id

    if not message.conversation_id:
        message.conversation_id = uuid.UUID(conversation_uuid)

    message.created_at = register_created_message(message=message)

    message = register_message_repo(db=db, message=message)

    return message



def register_message_AI_service(db, message, conversation_uuid, token):

    if not conversation_uuid:
        raise exc.ConversationIdInvalidError()

    message.uuid = uuid.uuid4()

    message.conversation_id = conversation_uuid

    message.created_at = register_created_message(message=message)

    message = register_message_repo(db=db, message=message)

    return message