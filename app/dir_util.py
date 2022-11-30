import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

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


def load_tf_model(model_uuid: str, ext: str=""):
    path = os.path.join(get_models_dir(), model_uuid)
    if not os.path.exists(path):
        return

    model = tf.keras.models.load_model(f'{path}/ml_m.h5')
    return model