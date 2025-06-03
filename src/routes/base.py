from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings


base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome(settings=Depends(get_settings)) -> dict:
    """
    Welcome endpoint for the Mini RAG API.
    Returns:
        dict: A welcome message with application name and version.
    """

    app_name = settings.APP_NAME
    app_version = settings.APP_VERSION

    return {"message": "Welcome to the Mini RAG API!", "app_name": app_name, "app_version": app_version}