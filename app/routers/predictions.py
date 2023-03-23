from fastapi import APIRouter, WebSocket, WebSocketException, HTTPException
from fastapi import UploadFile, Form, Depends, status
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from ..service.dir_service import store_model, load_model, load_out_tsf, load_in_tsf
from ..models.metadata_models import ModelMetadata, Prediction
from ..models.metadata_models import ModelMetadataRequest
from ..models.response_models import UploadModelResponse
from ..dependencies import get_db


router = APIRouter(
    prefix='/api/v1'
)


@router.post(
    '/upload',
    response_description="Uploaded model ID and timestamps.",
    response_model=UploadModelResponse,
    description="Accepts a pkl model file with transformers and metadata. Files are persisted.")
async def accept_ml_model(
        model_file: UploadFile,
        in_tsf: UploadFile | None = None,
        out_tsf: UploadFile | None = None,
        metadata_request: str = Form(),
        db=Depends(get_db)):
    # Parse the request
    request = ModelMetadataRequest.parse_raw(metadata_request)

    # Create the ID, timestamp and expiry timestamp
    created_at = datetime.today()
    # User submitted expiry date is ignored for now.
    expires_at = created_at + timedelta(1)
    created_timestamp = datetime.timestamp(created_at)
    exp_timestamp = datetime.timestamp(expires_at)

    # Create model metadata
    metadata = ModelMetadata.from_request(
        request, full_name=model_file.filename, created=created_timestamp, expires=exp_timestamp)

    # Save to DB
    new_metadata = await db.ml_metadata.insert_one(metadata.dict())
    model_id = str(new_metadata.inserted_id)

    # Save the model under path root/models/[id]/[filename].[ext]
    await store_model(model_id, model_file, in_tsf, out_tsf)

    # Return model name, ID and expiry date
    response = UploadModelResponse(model_id=model_id, model_name=model_file.filename, created_timestamp=str(
        created_at), expires_timestamp=str(expires_at))

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response.dict())


@router.websocket('/predict/ws')
async def predict(websocket: WebSocket, model_id: str, db=Depends(get_db)):
    if len(model_id) != 24:
        raise WebSocketException(code=status.WS_1011_INTERNAL_ERROR)

    metadata = await db.ml_metadata.find_one({"_id": ObjectId(model_id)})
    if metadata is None:
        raise WebSocketException(
            code=status.WS_1011_INTERNAL_ERROR, reason="Model with specified ID does not exist.")

    # Load the model
    ml_model = load_model(model_id)
    in_tsf = load_in_tsf(model_id) if metadata['in_transformer'] else None
    out_tsf = load_out_tsf(model_id) if metadata['out_transformer'] else None

    # Open the websocket connection
    await websocket.accept()
    while True:
        timestamp = datetime.today()
        raw = await websocket.receive_json()
        features = raw['features']

        if in_tsf is not None:
            try:
                features = in_tsf.transform(features)
            except ValueError:
                features = in_tsf.transform([features])

        target = ml_model.predict(features)

        if out_tsf is not None:
            target = out_tsf(target)

        prediction = Prediction(features=raw['features'], target=target,
                                model_id=str(metadata['_id']), model_name=metadata['name'], timestamp=str(timestamp))

        await db.predictions.insert_one(prediction.dict())

        await websocket.send_text(f'{target}')

    return


@router.get(path='/', response_model=list[Prediction], description='Returns a list of predictions made by a model with the given id.')
async def get_prediction(model_id: str, db=Depends(get_db)):
    if len(model_id) != 24:
        raise HTTPException(
            status_code=400, detail=f"Malformed model id: {model_id}.")

    predictions = await db.predictions.find({'model_id': model_id}, {'_id': 0}).to_list(length=None)

    return JSONResponse(content=predictions)
