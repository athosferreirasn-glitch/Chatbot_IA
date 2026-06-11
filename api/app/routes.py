from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from api.services.user_service import create_user_service
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.schemas.schemas import PromptRequest, UserCreate
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

gemini_api_key = os.environ.get('API_KEY')

client = genai.Client(api_key=gemini_api_key)


@router.post('/create_users')
def create_user_router(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    user = create_user_service(db=db, user=user)
    
    return {
        'message': 'usuário criado e cadastrado com sucesso'
    }


@router.post("/gerar-texto")
async def gerar_texto(request: PromptRequest, db: session = Depends(get_db)):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="O prompt não pode estar vazio")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.prompt
    )

    return {"resposta": chat.response_ai}