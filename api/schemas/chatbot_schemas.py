from pydantic import BaseModel, Field
from typing import Any


class PromptRequest(BaseModel):
    prompt: str

class Conversation(BaseModel):
    uuid: Any = None
    user_id: Any = None
    title: Any = None
    created_at: Any = None
    update_at: Any = None