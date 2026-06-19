from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.services.user_service import create_user_service, auth_login_service, auth_autorization_request
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.schemas.user_schemas import UserCreate


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

user_router = APIRouter()


def header_auth(token: str = Depends(oauth2_scheme)):

    token = auth_autorization_request(token=token)

    if token:

        return token


@user_router.post("/token")
def token_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = auth_login_service(db=db, user_data_login=form_data)

    if not token:
        raise HTTPException(
            status_code=500,
            detail="Token não criado"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@user_router.post('/create_users')
def create_user_router(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    user = create_user_service(db=db, user=user)
    
    return {
        'message': 'usuário criado e cadastrado com sucesso'
    }
