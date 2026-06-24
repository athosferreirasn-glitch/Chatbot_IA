from datetime import datetime

def register_created_user(user: object) -> float:

    user._created_at = datetime.now().timestamp()

    return user._created_at


def register_created_conversation(conversation: object) -> float:

    conversation.created_at = datetime.now().timestamp()

    return conversation.created_at


def register_created_message(message: object) -> float:

    message.created_at = datetime.now().timestamp()

    return message.created_at