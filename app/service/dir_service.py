import joblib
import aiofiles
from fastapi import UploadFile, HTTPException, status
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import tensorflow as tf


MODELS_DIR = './temp/ml_models'


def get_models_dir():
    data_dir = os.path.join(os.getcwd(), MODELS_DIR)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    return data_dir


def create_curr_model_dir(model_uuid: str):
    temp = os.path.join(get_models_dir(), model_uuid)
    if not os.path.exists(temp):
        os.mkdir(temp)
    return temp


def load_model(model_id: str):
    path = os.path.join(get_models_dir(), model_id)
    if not os.path.exists(path):
        return
    model = joblib.load(f'{path}/ml_m.pkl')
    return model


def load_in_tsf(model_id: str):
    path = os.path.join(get_models_dir(), model_id)
    if not os.path.exists(path):
        return
    in_tsf = joblib.load(f'{path}/in_tsf.pkl')
    return in_tsf


def load_out_tsf(model_id: str):
    path = os.path.join(get_models_dir(), model_id)
    if not os.path.exists(path):
        return
    out_tsf = joblib.load(f'{path}/out_tsf.pkl')
    return out_tsf


async def store_model(
        model_id: str,
        model_file: UploadFile,
        in_tsf: UploadFile | None = None,
        out_tsf: UploadFile | None = None):

    curr_model_dir = create_curr_model_dir(str(model_id))
    fext = model_file.filename.split('.')[-1]

    if fext not in {"pkl", "pickle"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Submitted file is not a .pkl file.")

    # Save the model under path root/models/[id]/ml_m.{fext}
    async with aiofiles.open(f'{curr_model_dir}/ml_m.pkl', 'wb') as temp:
        while content := await model_file.read(1024):
            await temp.write(content)

    if in_tsf is not None:
        async with aiofiles.open(f'{curr_model_dir}/in_tsf.pkl', 'wb') as temp:
            while content := await in_tsf.read(1024):
                await temp.write(content)

    if out_tsf is not None:
        async with aiofiles.open(f'{curr_model_dir}/out_tsf.pkl', 'wb') as temp:
            while content := await out_tsf.read(1024):
                await temp.write(content)

    return
