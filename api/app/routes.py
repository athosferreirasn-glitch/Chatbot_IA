from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.schemas.schemas import PromptRequest, PromptResponse
from api.services.service import register_chat_service
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

gemini_api_key = os.environ.get('API_KEY')

client = genai.Client(api_key=gemini_api_key)


@router.post("/gerar-texto")
async def gerar_texto(request: PromptRequest, db: session = Depends(get_db)):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="O prompt não pode estar vazio")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.prompt
    )

    return {"resposta": chat.response_ai}