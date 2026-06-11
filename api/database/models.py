from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, LargeBinary, TIMESTAMP, Uuid, VARCHAR, TEXT

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id = Column(Uuid(225), primary_key=True, unique=True, nullable=False)
    name = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(225), unique=False, nullable=False)
    created_at = Column(TIMESTAMP)


class Conversations(Base):
    __tablename__ = "conversations"

    id = Column(Uuid(225), primary_key=True, unique=True, nullable=False)
    user_id = Column(Uuid(225), nullable=False)
    title = Column(VARCHAR(500), nullable=False)
    created_at = Column(TIMESTAMP)
    update_at = Column(TIMESTAMP)


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Uuid(225), primary_key=True, unique=True, nullable=False)
    conversation_id = Column(Uuid(225), nullable=False)
    role = Column(VARCHAR(50), nullable=False)
    content = Column(TEXT(5000), nullable=False)
    created_at = Column(TIMESTAMP)