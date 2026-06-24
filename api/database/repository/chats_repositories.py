from api.database.models import Conversations, Messages


def create_conversation_repo(db, conversation):
    conversation_db = Conversations(
        id=conversation.uuid,
        user_id=conversation.user_id,
        title=conversation.title,
        created_at=conversation.created_at,
        update_at=conversation.update_at
    )

    db.add(conversation_db)
    
    db.commit()

    db.refresh(conversation_db)

    return conversation_db


def register_message_repo(db, message):
    message_db = Messages(
        id=message.uuid,
        conversation_id=message.conversation_id,
        role=message.role,
        content=message.content,
        created_at=message.created_at
    )


    db.add(message_db)

    db.commit()

    db.refresh(message_db)

    return message_db