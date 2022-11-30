from fastapi import FastAPI
from .routers import model_v1

app = FastAPI()

app.include_router(model_v1.router)

@app.get("/")
async def root():
    return {"message": 'Welcome to ML backend.'}
