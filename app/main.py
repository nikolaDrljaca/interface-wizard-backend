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
    return {"message": 'Welcome to ML backend.'}
