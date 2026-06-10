from fastapi import FastAPI
from api.app.routes import router
from google import genai


app = FastAPI()

app.include_router(router=router)

