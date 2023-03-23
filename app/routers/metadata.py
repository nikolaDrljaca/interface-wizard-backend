
from fastapi.responses import JSONResponse
from fastapi import Depends, status
from fastapi import APIRouter
from ..dependencies import get_db


router = APIRouter(prefix='/api/v1/metadata')


@router.get(path='/', response_model=list[str], description='Returns a list of all MODEL IDs present in the system.')
async def get_all(db=Depends(get_db)):
    all_metadata = await db.ml_metadata.find({},{'_id': 1}).to_list(length=None)
    all_metadata = map(lambda x: str(x['_id']), all_metadata)
    return JSONResponse(content=list(all_metadata))
