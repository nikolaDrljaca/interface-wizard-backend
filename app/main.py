from fastapi import FastAPI
from dependencies import get_sample_model
from dependencies import get_sample_actual
from dependencies import get_sample_labels
from PIL import Image
import numpy as np
import os
from .routers import eval_model

app = FastAPI()

app.include_router(eval_model.router)

@app.get("/")
async def root():
    # main code here
    model = get_sample_model()
    
    image_path = os.path.join("./data/test_images/item_0.jpg")
    test_image = Image.open(image_path)
    test_img_array = np.asarray(test_image)

    batch = (np.expand_dims(test_img_array, 0))
    prediction = np.argmax(model.predict(batch)[0])

    label_map = get_sample_labels()
    actuals = get_sample_actual()
    print(label_map)
    print(actuals)

    pred = label_map[f'{prediction}']

    return {"message": f"Predicted: {pred} || Actual: {actuals[0]}"}
