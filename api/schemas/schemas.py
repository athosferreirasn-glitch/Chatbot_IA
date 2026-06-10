from pydantic import BaseModel
from typing import Any


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse():
    def __init__(self, prompt, response):
        self.prompt = prompt
        self.response = response