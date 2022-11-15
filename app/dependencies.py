# Define a function to retrieve the ML model and return it
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Disable logging info coming from TF
import tensorflow as tf
import json


def get_sample_model():
    # path handling here
    model_path = os.path.join("./data/mnist_model") 
    loaded_model = tf.keras.models.load_model(model_path)
    return loaded_model


# Not handling errors here
def get_sample_labels() -> dict[str, str]:
    path = os.path.join('./data/test_labels/label_map.txt')
    data = open(path).read()
    labels_dict = json.loads(data)
    return labels_dict


def get_sample_actual() -> list[str]:
    path = os.path.join("./data/test_labels/test_labels.txt")
    out = []
    with open(path) as f:
        for line in f:
            out.append(line.replace('\n', ''))
            
    return out