from enum  import Enum

class RespponseSignal(Enum):
    SUCCESS = "success"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_NOT_FOUND = "file_not_found"
    PROJECT_NOT_FOUND = "project_not_found"
    UPLOAD_FAILED = "upload_failed"
    UPLOAD_SUCCESS = "file_upload_success"