from pydantic import BaseModel

class UploadModelResponse(BaseModel):
    model_id: str
    model_name: str
    created_timestamp: str
    expires_timestamp: str