from pydantic import BaseModel

class UploadModelResponse(BaseModel):
    model_id: str
    model_name: str
    created_timestamp: str
    expires_timestamp: str


class ModelMetadataResponse(BaseModel):
    name: str
    desc: str
    model_type: str
    in_tsf: str
    out_tsf: str
    created: str
    expires: str
    feature_names: list[str]
    target_name: str


class PredictionResponse(BaseModel):
    result: str