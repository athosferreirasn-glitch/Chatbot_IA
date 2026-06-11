from datetime import datetime

def register_created_user(user):

    user._created_at = datetime.now().timestamp()

    return user._created_at