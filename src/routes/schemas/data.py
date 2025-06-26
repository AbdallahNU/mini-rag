from pydantic import BaseModel
from typing import Optional

class DataSchema(BaseModel):
    """
    Schema for data validation.
    """
    file_id: str
    chunk_size: Optional[int] = 100
    chunk_overlap: Optional[int] = 10
    do_reset: Optional[int] = 0
