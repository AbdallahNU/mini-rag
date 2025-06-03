from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models.enums import RespponseSignal
import logging
import aiofiles

logger = logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, settings: Settings=Depends(get_settings)) -> dict:
    """
    Upload data to the specified project.

    Args:
        project_id (str): The ID of the project to which the data will be uploaded.
        file (UploadFile): The file to be uploaded.

    Returns:
        dict: A response message indicating the success of the upload.
    """
    
    # validate file
    data_controller = DataController()
    is_valid, message =  data_controller.validate_uploaded_file(file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": message.value}
        )
    
    # save file
    file_path = data_controller.generate_unique_filename(file.filename, project_id)

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while True:
                chunk = await file.read(settings.FILE_CHUNK_SIZE)
                if not chunk:
                    break
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Failed to upload file {file.filename} for project {project_id}: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": RespponseSignal.UPLOAD_FAILED.value }
        )
    
       
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": RespponseSignal.UPLOAD_SUCCESS.value}
    )