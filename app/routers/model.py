from fastapi import APIRouter, WebSocket
from fastapi import UploadFile, Form
import uuid
from datetime import datetime
import aiofiles
import numpy as np
from ..dir_util import create_curr_model_dir
from ..dir_util import load_tf_model
from ..models.MetadataModels import ModelMetadata
from ..models.MetadataModels import ModelMetadataRequest
from ..processing import b64image_to_ndarray


router = APIRouter(
    prefix='/model'
)


@router.post('/upload')
async def accept_ml_model(model_file: UploadFile, metadata: str = Form(), exp_date: str = Form()):
    # Create the UUID, timestamp and expiry timestamp
    model_uuid = uuid.uuid1()
    created_timestamp = datetime.timestamp(datetime.now()) #Unix timestamp
    exp = datetime.timestamp(datetime.strptime(exp_date, "%d-%m-%Y %H:%M:%S"))

    # Create model metadata, save under root/models/[uuid]/metadata.json -> for now
    request = ModelMetadataRequest.parse_raw(metadata)
    m_data = ModelMetadata(model_uuid=str(model_uuid), vendor=request.vendor, inputs=request.inputs, ext=request.ext)

    curr_model_dir = create_curr_model_dir(str(model_uuid))
    async with aiofiles.open(f'{curr_model_dir}/metadata.json', 'w') as temp:
        await temp.write(m_data.json())

    # Save the model under path root/models/[uuid]/[filename].[ext]
    fext = model_file.filename.split('.')[-1]
    async with aiofiles.open(f'{curr_model_dir}/ml_m.{fext}', 'wb') as temp:
        while content := await model_file.read(1024):
            await temp.write(content)


    # Create DB entry with UUID, timestamp and expiry

    # Return model name, UUID and expiry date
    return {
        "model_uuid": str(model_uuid),
        "model_name": model_file.filename,
        "created_timestamp": str(created_timestamp),
        "expiration_timestamp": str(exp),
    }


# In case metadata needs to be changed, user error -> Provided wrong metadata
@router.post('/metadata/{model_uuid}')
async def accept_metadata(request: ModelMetadataRequest, model_uuid: str):
    metadata = ModelMetadata()
    return


@router.websocket('/predict/ws')
async def predict(websocket: WebSocket, model_uuid: str):
    # Check for model existance by UUID, raise HTTP error if not found

    # Load the model by using appropriate vendor
    ml_model = load_tf_model(model_uuid)
    # Open the websocket connection
    await websocket.accept()
    while True:
        # Receive data as bytes and cast to appropriate type
        # For images, they need to be base64 decoded
        # Make prediction
        # Respond with outcome
        data = await websocket.receive_text()
        image = b64image_to_ndarray(data)
        image = (np.expand_dims(image, 0))
        prediction = ml_model.predict(image)
        print(prediction)
        await websocket.send_text(f'{np.argmax(prediction[0])}')

    return