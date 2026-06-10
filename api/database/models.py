from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, LargeBinary

class Base(DeclarativeBase):
    pass

class Chats(Base):
    __tablename__ = "prompt_chat"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_prompt = Column(String(3000), nullable=False)
    response_ai = Column(String(5000), nullable=False)