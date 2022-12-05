from pydantic import BaseModel
from .RequestModels import ModelMetadataRequest, InputDataItem


class ModelMetadata(BaseModel):
    name: str
    created: float
    vendor: str
    file_ext: str
    model_type: str
    expires: float
    inputs: list[InputDataItem]

    def from_request(request: ModelMetadataRequest, full_name: str, created: float, expires: float):
        _split = full_name.split('.')

        return ModelMetadata(
            name=_split[0],
            created=created,
            vendor=request.vendor,
            file_ext=_split[-1],
            model_type=request.model_type,
            expires=expires,
            inputs=request.inputs)
