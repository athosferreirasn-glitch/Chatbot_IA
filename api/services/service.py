from api.database.repository.repositories import register_chat


def register_chat(db, chat):
    chat = register_chat(db=db, chat=chat)