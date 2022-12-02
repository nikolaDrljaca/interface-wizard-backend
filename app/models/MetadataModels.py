from typing import List
from pydantic import BaseModel


class InputDataItem(BaseModel):
    type: str
    order: int


class ModelMetadataRequest(BaseModel):
    vendor: str
    model_type: str
    expires: str
    inputs: List[InputDataItem]


class InputItemRequest(BaseModel):
    type: str
    order: int
    name: str
    desc: str


class ModelMetadata(BaseModel):
    name: str
    #model_uuid: str
    created: float
    vendor: str
    file_ext: str
    model_type: str
    expires: float
    inputs: List[InputDataItem]

    def from_request(request: ModelMetadataRequest, full_name: str, created: float, expires: float):
        _split = full_name.split('.')

        return ModelMetadata(
            name=_split[0],
            #model_uuid=uuid,
            created=created,
            vendor=request.vendor,
            file_ext=_split[-1],
            model_type=request.model_type,
            expires=expires,
            inputs=request.inputs)
