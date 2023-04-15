import shutil
from datetime import datetime
import os
import app.service.dir_service as dir_service


async def model_cleanup(db):
    current = datetime.now()
    timestamp = datetime.timestamp(current)
    expired = db.ml_metadata.find({
        "expires": {"$lt": timestamp}
    })
    dir = dir_service.get_models_dir()
    async for metadata in expired:
        id = str(metadata["_id"])
        path = os.path.join(dir, id)
        print(path)
        if not os.path.exists(path):
            pass
        try:
            shutil.rmtree(path)
        except:
            print(f'Failed to remove directory {dir}/{id}!')
    return
