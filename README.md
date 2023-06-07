# ML Backend

Supporting backend app for `ml-interface-wizard` to handle business logic.

## Folder Structure

This project will try to follow this scheme. Will be updated as the project evolves.
![Project directory structure.](dir_struct.png "Project directory structure.")

## How to run

**Make sure python is installed on the local machine.**
The project can be run locally, with the instructions below.
Alternatively, the project can be run in a Docker container.

```
docker push nikoladrljacaa/wizard-backend:{tagname}
-- tags available at https://hub.docker.com/repository/docker/nikoladrljacaa/wizard-backend/general
```

Finally, an image can be created locally and run:

```
docker build -t <image_name> .
docker run <image_name> -p 8000:8000
```

### Clone and Run locally

```
# 1. Create virtual environment
python3 -m venv env

# 2. Activate created env
source env/bin/activate # Unix
.\env\Scripts\activate # Windows

# 3. Install packages
pip install -r requirements.txt

# 5. IMPORTANT - Create `.env` file in the same directory as `docker-compose.yml`
This will be used to setup the MongoDB instance. The following keys need to be present.
Define values as desired or leave listed defaults.
DB_USER=test
DB_PASS=test1234
DB_HOST=localhost
DB_PORT=27017

# 4. Setup MongoDB instance, make sure Docker is installed
docker compose up -d

# Controll the docker container
docker compose stop -> stop or shutdown the container, but DON'T tear it down, the data will not stay
docker compose start -> If the container is stopped, start it this way

# 5. Run the app
uvicorn app.main:app --reload
```

## Documentation

`openapi.json` documentation is available at `<localhost>/docs`.
A brief overview of the endpoints can be viewed there.

For the prediction WebSocket, the following apply:

- endpoint: `/api/v1/predict/ws/[model_id]`
- accepts JSON body:

```
{
    "features": []
}
```

- Returns the response from the model or the output transformer, if present.

## Notes

Export requirements with `pip3 freeze > requirements.txt`
To connect to mongodb instance use URI structure: `mongodb://[username]:[password]@localhost:27017/[optionalDatabaseName]`

### To use Compose with env variables

- Make sure `.env` and `docker-compose.yml` are in the same directory
- Define variables inside `.env` and reference then using ${} ex. `- MONGO_INITDB_ROOT_USERNAME=${MONGODB_USERNAME}`
- Make sure `.env` is git ignored
