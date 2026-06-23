from pydantic import BaseModel, Field
from typing import Any


class Conversation(BaseModel):
    uuid: Any = None
    user_id: Any = None
    title: Any = None
    created_at: Any = None
    update_at: Any = None


class Message(BaseModel):
    _uuid: Any = None
    _conversation_id: Any = None
    _role: str = None
    content: str = None
    _created_at: Any = None