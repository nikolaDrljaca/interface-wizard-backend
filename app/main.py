from fastapi import FastAPI
from .routers import model

app = FastAPI()

app.include_router(model.router)

@app.get("/")
async def root():
    return {"message": 'Welcome to ML backend.'}
