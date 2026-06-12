from api.database.repository.user_repositories import create_user_repo
from api.security.password import get_password_hash, verify_password
from api.utils.utils import register_created_user
from fastapi import HTTPException
import uuid

def create_user_service(db, user):

    user.password = get_password_hash(password=user.password)

    user._created_at = register_created_user(user=user)

    user._uuid = uuid.uuid4()

    user = create_user_repo(db=db, user=user)

    return user