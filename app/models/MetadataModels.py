from typing import List
from pydantic import BaseModel


class InputDataItem(BaseModel):
    type: str
    order: int


class ModelMetadata(BaseModel):
    model_uuid: str
    vendor: str
    ext: str
    inputs: List[InputDataItem]


class ModelMetadataRequest(BaseModel):
    vendor: str
    ext: str
    inputs: List[InputDataItem]