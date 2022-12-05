from pydantic import BaseModel


class InputDataItem(BaseModel):
    type: str
    order: int


class ModelMetadataRequest(BaseModel):
    vendor: str
    model_type: str
    expires: str
    inputs: list[InputDataItem]


class PredictionRequestItem(BaseModel):
    type: str
    value: str
    order: str


class PredictionRequest(BaseModel):
    inputs: list[PredictionRequestItem]
