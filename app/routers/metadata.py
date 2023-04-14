from bson import ObjectId
from fastapi.responses import JSONResponse
from fastapi import Depends, status, HTTPException
from fastapi import APIRouter
from ..dependencies import get_db
from ..models.response_models import ModelMetadataResponse
from datetime import datetime

router = APIRouter(prefix='/api/v1/metadata')


@router.get(path='/', response_model=list[str], description='Returns a list of all MODEL IDs present in the system.')
async def get_all(db=Depends(get_db)):
    all_metadata = await db.ml_metadata.find({}, {'_id': 1}).to_list(length=None)
    all_metadata = map(lambda x: str(x['_id']), all_metadata)
    return JSONResponse(content=list(all_metadata))


@router.get(path='/{model_id}', response_model=ModelMetadataResponse, description='Returns metadata information for a MODEL ID.')
async def get_by_id(model_id: str, db=Depends(get_db)):
    id = ''
    try:
        id = ObjectId(model_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Malformed model id.')
    time_format = '%d/%m/%Y-%H:%M:%S'
    model_metadata = await db.ml_metadata.find_one({'_id': id}, {'_id': 0})
    model_metadata['created'] = datetime.fromtimestamp(
        model_metadata['created']).strftime(time_format)

    model_metadata['expires'] = datetime.fromtimestamp(
        model_metadata['expires']).strftime(time_format)

    return JSONResponse(content=model_metadata)
