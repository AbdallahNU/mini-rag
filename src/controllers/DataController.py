from controllers.BaseController import BaseController
from controllers.ProjectController import ProjectController
from fastapi import UploadFile
from models.enums import RespponseSignal
import os


class DataController(BaseController):
    """Controller for managing data operations."""
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile):
        """
        Validates the uploaded file.
        This method can be extended to include specific validation logic.
        """
        
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False, RespponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.settings.FILE_MAX_SIZE * 1024 * 1024:  # Convert MB to bytes
            return False, RespponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, RespponseSignal.SUCCESS.value
    
    def generate_unique_filename(self, original_file_name: str, project_id: str) -> str:
        
        random_string = self.generate_random_string(10)
        project_path = ProjectController().get_project_path(project_id)

        cleaned_file_name = self.get_cleaned_file_name(original_file_name)

        unique_file_name = f"{random_string}_{cleaned_file_name}"
        return os.path.join(project_path, unique_file_name)

    def get_cleaned_file_name(self, file_name: str) -> str:
        """
        Cleans the file name by removing special characters and spaces.
        """
        cleaned_name = ''.join(e for e in file_name if e.isalnum() or e in (' ', '.', '_')).strip()
        return cleaned_name.replace(' ', '_')

        
    
