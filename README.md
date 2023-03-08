# ML Backend
Supporting backend app for `ml-interface-wizard` to handle business logic.


## Folder Structure
Example file structure taken from `FastAPI` docs. This project will try to follow this scheme. 

```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dir_util.py      # file containing methods to handle local filesystem storage and model loading(for now)
│   ├── processing.py    # functions to convert types (binary -> image/video/text/etc.)
│   └── routers          # 
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── model_v1.py  # v1 endpoints
│   └── models           # 
│       ├── __init__.py  # 
│       └── MetadataModels.py   # Contains metadata models for DB and request/response 
```

## How to run
**Make sure python is installed on the local machine.**
As it stands, the project should be run locally. Later, we will transition to a Docker Image for easier testing and deployment.

```
# 1. Create virtual environment
python3 -m venv env

# 2. Activate created env
source env/bin/activate # Unix
.\env\Scripts\activate # Windows

# 3. Install packages
pip install -r requirements.txt

--- OPTIONAL ---
# 4. Make sure temp data and model are present in /app/data
Download mnist_model, test_images, test_labels from GDrive
--- OPTIONAL ---

# 4. Setup MongoDB instance, make sure Docker is installed
docker compose up -d

# Controll the docker container
docker compose stop -> stop or shutdown the container, but DON'T tear it down, the data will not stay
docker compose start -> If the container is stopped, start it this way

# 5. Run the app
uvicorn app.main:app --reload
```

## Notes
Export requirements with `pip3 freeze > requirements.txt`
To connect to mongodb instance use URI structure: `mongodb://[username]:[password]@localhost:27017/[optionalDatabaseName]`

### To use Compose with env variables
- Make sure `.env` and `docker-compose.yml` are in the same directory
- Define variables inside `.env` and reference then using ${} ex. `- MONGO_INITDB_ROOT_USERNAME=${MONGODB_USERNAME}`
- Make sure `.env` is git ignored



