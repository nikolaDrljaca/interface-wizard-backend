from PIL import Image
import base64
import numpy as np
import io


def b64image_to_ndarray(image: str) -> np.ndarray:
    decoded = base64.b64decode(image)
    temp_file = io.BytesIO(decoded)
    im_array = np.asarray(Image.open(temp_file))
    return im_array
