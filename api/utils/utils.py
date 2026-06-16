from datetime import datetime

def register_created_user(user):

    user._created_at = datetime.now().timestamp()

    return user._created_at


def register_created_conversation(conversation):

    conversation.created_at = datetime.now().timestamp()

    return user._created_at