from BaseController import BaseController
from ProjectController import ProjectController
from models.enums import ProcessEnum
from langchain.document_loaders import TextLoader, PyPDFLoader
import os

class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id)

    def get_file_extension(self, file_name: str) -> str:
        """
        Get the file extension from the file name.

        Args:
            file_name (str): The name of the file.

        Returns:
            str: The file extension.
        """
        return os.path.splitext(file_name)[-1]

    def get_file_loader(self, file_name: str):
        """
        Get the appropriate file loader based on the file extension.

        Args:
            file_name (str): The name of the file.

        Returns:
            DocumentLoader: The appropriate document loader for the file type.
        """
        extension = self.get_file_extension(file_name).lower()
        process_enum = ProcessEnum()

        if extension == process_enum.TXT:
            return TextLoader(os.path.join(self.project_path, file_name))
        elif extension == process_enum.PDF:
            return PyPDFLoader(os.path.join(self.project_path, file_name))
        else:
            raise ValueError(f"{ProcessEnum.UNSUPPORTED}: {extension}")