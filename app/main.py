from fastapi import FastAPI
from contextlib import asynccontextmanager
from .service import cleanup
from .routers import predictions, examples, metadata
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from .dependencies import get_db_sync


async def cleanup_task(db):
    while True:
        print('executing cleanup in the background')
        await cleanup.model_cleanup(db)
        await asyncio.sleep(60 * 60)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Code
    client = get_db_sync()
    db = client.interface_wizard
    print("Lifespan startup invoked.")
    asyncio.create_task(cleanup_task(db))
    yield
    # Shudown code
    client.close()
    print("Lifespan shutdown invoked.")


app = FastAPI(lifespan=lifespan)

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
