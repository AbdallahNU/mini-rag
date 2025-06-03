from controllers.BaseController import BaseController
from fastapi import UploadFile
from models.enums import RespponseSignal
import os


class ProjectController(BaseController):
    """Controller for managing project operations."""
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str) -> str:
        """Get the path of the project directory."""
        project_dir = os.path.join(self.files_path, project_id)

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
            
        return project_dir