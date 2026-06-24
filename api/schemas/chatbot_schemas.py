from pydantic import BaseModel, Field
from typing import Any


class Conversation(BaseModel):
    uuid: Any = None
    user_id: Any = None
    title: Any = None
    created_at: Any = None
    update_at: Any = None


class Message(BaseModel):
    uuid: Any = None
    conversation_id: Any = None
    role: str = None
    content: str = None
    created_at: Any = None

class PromptRquest(BaseModel):
    prompt: str