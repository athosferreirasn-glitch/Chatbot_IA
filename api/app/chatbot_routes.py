from fastapi import APIRouter, HTTPException, Depends
from api.schemas.schemas import PromptRequest
from api.app.user_routes import oauth2_scheme
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.environ.get("API_KEY")

client = genai.Client(api_key=gemini_api_key)

chatbot_router = APIRouter()


@chatbot_router.post("/generate_chat")
def generate_chat(
    request: PromptRequest,
    token: str = Depends(oauth2_scheme)
):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.prompt
    )

    return {"message": response.text}