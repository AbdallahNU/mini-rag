from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter()

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME", "Mini RAG")
    app_version = os.getenv("APP_VERSION", "1.0.0")
    return {"message": "Welcome to the Mini RAG API!", "app_name": app_name, "app_version": app_version}