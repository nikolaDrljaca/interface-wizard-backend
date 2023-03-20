from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import json
from ..models.metadata_models import ModelMetadataRequest

router = APIRouter(prefix='/api/v1/examples')

@router.get(path="/",description="Returns an example of a complete model metadata JSON object.")
async def get_metadata_example():
    raw = """
    {
        "name": "diabetes_model",
        "desc": "Estimates if a patient has diabetes based on certain parameters.",
        "in_transformer": true,
        "out_transformer": true,
        "model_type": "binary",
        "expires": "13-02-2023 14:42:36",
        "feature_names": [
            "Pregnancies",
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Age"
        ],
        "target_name": "Has Diabetes"
    }
    """
    parsed = ModelMetadataRequest.parse_raw(raw)
    return JSONResponse(status_code=status.HTTP_200_OK, content=parsed.dict())


@router.get(path='/struct', description="Returns a general structure for the model metadata JSON object.")
async def get_metadata_struct():
    raw = """
    {
        "name": "Model name if any.",
        "desc": "Model description if any.",
        "in_transformer": "true | false - Is a transformer present",
        "out_transformer": "true | false - Is an output transformer present",
        "model_type": "binary-class | multi-class | regression",
        "expires": "Indicates expiry. After this time the model will NOT be available.",
        "feature_names": [
            "List of feature names"
        ],
        "target_name": "Description for the target "
    }
    """
    return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(raw))
