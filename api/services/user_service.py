from api.database.repository.user_repositories import create_user_repo, get_user_by_email_repo
from api.security.password import get_password_hash, verify_password
from api.utils.utils import register_created_user
from fastapi import HTTPException
import uuid
from api.security.jwt_handler import create_acess_token, decode_token

def create_user_service(db, user):

    user.password = get_password_hash(password=user.password)

    user._created_at = register_created_user(user=user)

    user._uuid = uuid.uuid4()

    user = create_user_repo(db=db, user=user)

    return user


def auth_login_service(db, user_data_login):

    user = get_user_by_email_repo(db=db, email=user_data_login.username)

    if not user:
        raise HTTPException(
            status_code=400,
            detail='Usuário não encontrado'
        )
        
    if not verify_password(plain_password=user_data_login.password, hashed_password=user.password_hash):
        raise HTTPException(
            status_code=401,
            detail='Senha incorreta'
        )

    token = create_acess_token(
        data={
            "sub": str(user.uuid),
            "role": "user"
        },
    )

    return token


def auth_autorization_request(token):

    if not token or token in {"undefined", "null"}:
        raise HTTPException(
            status_code=401,
            detail='Token não enviado'
        )

    
    try:

        decode_token(token=token)

        return token

    except Exception:
        raise HTTPException(
            status_code=401,
            detail='Não autorizado'
        )