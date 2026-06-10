from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import session
from api.database.connection import get_db
from api.schemas.schemas import PromptRequest, PromptResponse
from api.services.service import register_chat
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

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.prompt
        )

        chat = PromptResponse(prompt=request.prompt, response=response.text)

        register_chat(db=db, chat=chat)

        return {"resposta": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao comunicar com o Google AI: {str(e)}")