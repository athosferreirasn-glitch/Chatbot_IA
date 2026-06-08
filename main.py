from fastapi import FastAPI
from app.api.routes import router
from google import genai


app = FastAPI()

app.include_router(router=router)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)