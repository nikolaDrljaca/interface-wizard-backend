from fastapi import FastAPI
from .routers import predictions, examples, metadata

app = FastAPI()

app.include_router(predictions.router)
app.include_router(examples.router)
app.include_router(metadata.router)


@app.get("/")
async def root():
    return {"message": 'Welcome to ML backend.'}
