import os

MODELS_DIR = 'models'

def get_models_dir():
    data_dir = os.path.join(os.getcwd(), MODELS_DIR)
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    return data_dir


def create_curr_model_dir(model_uuid: str):
    temp = os.path.join(get_models_dir(), model_uuid)
    if not os.path.exists(temp):
        os.mkdir(temp)
    return temp