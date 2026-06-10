from api.database.models import Chats
from fastapi import HTTPException


def register_chat(db, chat):
    db_chat = Chats(
        user_prompt=chat.prompt,
        response_ai=chat.response
    )

    db.add(db_chat)

    db.commit()

    db.refresh(db_chat)

    return db_chat