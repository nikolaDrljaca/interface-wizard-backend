from pydantic import BaseModel
import typing


class ModelMetadataRequest(BaseModel):
    name: str
    desc: str
    model_type: str
    in_transformer: bool
    out_transformer: bool
    expires: str
    feature_names: list[str]
    target_name: str
    message_format: str
    include_certain: bool


class PredictionRequest(BaseModel):
    features: list[typing.Any]
