from fastapi import FastAPI
from .routers import predictions, examples, metadata
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(predictions.router)
app.include_router(examples.router)
app.include_router(metadata.router)

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": 'Welcome to ML backend.'}
