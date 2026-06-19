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