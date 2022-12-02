from fastapi import APIRouter, WebSocket, WebSocketException
from fastapi import UploadFile, Form, Depends, status
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId
from datetime import datetime
import aiofiles
import numpy as np
from ..dir_util import create_curr_model_dir
from ..dir_util import load_tf_model
from ..models.MetadataModels import ModelMetadata
from ..models.MetadataModels import ModelMetadataRequest
from ..models.ResponseModels import UploadModelResponse
from ..processing import b64image_to_ndarray
from ..dependencies import get_db


router = APIRouter(
    prefix='/v1'
)


@router.post('/model/upload', response_description="Uploaded model ID and timestamps.", response_model=UploadModelResponse)
async def accept_ml_model(model_file: UploadFile, metadata_request: str = Form(), db=Depends(get_db)):
    # Parse the request
    request = ModelMetadataRequest.parse_raw(metadata_request)

    # Create the ID, timestamp and expiry timestamp
    created_timestamp = datetime.timestamp(datetime.now())
    exp = datetime.timestamp(datetime.strptime(
        request.expires, "%d-%m-%Y %H:%M:%S"))

    # Create model metadata, save under root/models/[id]/metadata.json -> for now
    metadata = ModelMetadata.from_request(
        request, full_name=model_file.filename, created=created_timestamp, expires=exp)

    # Save to DB
    new_metadata = await db.ml_metadata.insert_one(metadata.dict())
    model_id = str(new_metadata.inserted_id)

    # Save the model under path root/models/[id]/[filename].[ext]
    curr_model_dir = create_curr_model_dir(str(model_id))
    fext = model_file.filename.split('.')[-1]
    async with aiofiles.open(f'{curr_model_dir}/ml_m.{fext}', 'wb') as temp:
        while content := await model_file.read(1024):
            await temp.write(content)

    # Return model name, ID and expiry date
    response = UploadModelResponse(model_id=model_id, model_name=model_file.filename, created_timestamp=str(
        created_timestamp), expires_timestamp=str(created_timestamp))

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response.dict())


@router.websocket('/model/predict/ws')
async def predict(websocket: WebSocket, model_id: str, db=Depends(get_db)):
    if len(model_id) != 24:
        raise WebSocketException(code=status.WS_1011_INTERNAL_ERROR)

    metadata = await db.ml_metadata.find_one({"_id": ObjectId(model_id)})
    if metadata is None:
       raise WebSocketException(code=status.WS_1011_INTERNAL_ERROR, reason="Model with specified ID does not exist.")

    # Load the model by using appropriate vendor, metadata.vendor
    ml_model = load_tf_model(model_id, metadata.ext)

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
