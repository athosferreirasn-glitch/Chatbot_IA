from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, LargeBinary, Uuid, VARCHAR, TEXT

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    uuid = Column(Uuid(225), primary_key=True, unique=True, nullable=False)
    name = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(TEXT, unique=False, nullable=False)
    created_at = Column(TEXT)


class Conversations(Base):
    __tablename__ = "conversations"

    id = Column(Uuid(225), primary_key=True, unique=True, nullable=False)
    user_id = Column(Uuid(225), nullable=False)
    title = Column(VARCHAR(500), nullable=False)
    created_at = Column(TEXT)
    update_at = Column(TEXT)


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Uuid(225), primary_key=True, unique=True, nullable=False)
    conversation_id = Column(Uuid(225), nullable=False)
    role = Column(VARCHAR(50), nullable=False)
    content = Column(TEXT, nullable=False)
    created_at = Column(TEXT)