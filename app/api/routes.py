from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

gemini_api_key = os.environ.get('API_KEY')

client = genai.Client(api_key=gemini_api_key)

class PromptRequest(BaseModel):
    prompt: str

@router.post("/gerar-texto")
async def gerar_texto(request: PromptRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="O prompt não pode estar vazio")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.prompt,
        )
        return {"resposta": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao comunicar com o Google AI: {str(e)}")