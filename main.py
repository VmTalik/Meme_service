from fastapi import FastAPI
from api import service_router

app = FastAPI()
app.include_router(service_router)
