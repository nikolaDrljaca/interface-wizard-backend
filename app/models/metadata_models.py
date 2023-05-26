from pydantic import BaseModel
from typing import Any
from .request_models import ModelMetadataRequest


class ModelMetadata(BaseModel):
    name: str
    desc: str
    model_type: str
    in_transformer: bool
    out_transformer: bool
    created: float
    expires: float
    feature_names: list[str]
    target_name: str
    message_format: str
    include_certain: bool

    @staticmethod
    def from_request(request: ModelMetadataRequest, full_name: str, created: float, expires: float):
        return ModelMetadata(
            name=full_name,
            desc=request.desc,
            model_type=request.model_type,
            in_transformer=request.in_transformer,
            out_transformer=request.out_transformer,
            created=created,
            expires=expires,
            message_format=request.message_format,
            include_certain=request.include_certain,
            feature_names=request.feature_names,
            target_name=request.target_name)


class Prediction(BaseModel):
    features: list[Any]
    target: Any
    model_id: str
    model_name: str
    timestamp: str
