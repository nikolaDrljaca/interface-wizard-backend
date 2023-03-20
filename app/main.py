from fastapi import FastAPI
from .routers import predictions

app = FastAPI()

app.include_router(predictions.router)

@app.get("/")
async def root():
    return {"message": 'Welcome to ML backend.'}
