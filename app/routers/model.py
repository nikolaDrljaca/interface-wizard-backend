from fastapi import APIRouter
from fastapi import UploadFile, Form
import uuid
from datetime import datetime
import aiofiles
from ..dir_util import create_curr_model_dir


router = APIRouter(
    prefix='/model'
)


@router.post('/upload')
async def accept_file(file: UploadFile, exp_date: str = Form()):
    # Create the UUID, timestamp and expiry timestamp
    model_uuid = uuid.uuid1()
    created_timestamp = datetime.timestamp(datetime.now()) #Unix timestamp
    exp = datetime.timestamp(datetime.strptime(exp_date, "%d-%m-%Y %H:%M:%S"))

    # Save the model under path root/models/[uuid]/[filename].[ext]
    curr_model_dir = create_curr_model_dir(str(model_uuid))
    async with aiofiles.open(f'{curr_model_dir}/{file.filename}', 'wb') as temp:
        while content := await file.read(1024):
            await temp.write(content)


    # Create DB entry with UUID, timestamp and expiry

    # Return model name, UUID and expiry date
    return {
        "model_uuid": str(model_uuid),
        "model_name": file.filename,
        "created_timestamp": str(created_timestamp),
        "expiration_timestamp": str(exp),
    }

