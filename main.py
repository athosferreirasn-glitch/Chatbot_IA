from fastapi import FastAPI
from api.app.user_routes import user_router
from api.app.chatbot_routes import chatbot_router


app = FastAPI()

app.include_router(router=user_router)
app.include_router(router=chatbot_router)