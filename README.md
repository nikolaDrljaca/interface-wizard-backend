# ML Backend
Supporting backend app for `ml-interface-wizard` to handle business logic.

## Todo

- [ ] Figure out and document development process. FIRST!

- [ ] Create `/pred_model` route for ML model handling (should have request body params or query params to suggest model type. Optionally handle this in function itself.)
- [ ] `/make` GET to get the prediction (*as extension to pred_model*) (throw exceptions in response if model/data is not present for session.)
- [ ] `/pred_model` POST to post the model
- [ ] `/pred_model/data` POST the data that will be used to eval

## Folder Structure
Example file structure taken from `FastAPI` docs. This project will try to follow this scheme. 

```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
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

# 4. Make sure temp data and model are present in /app/data
Download mnist_model, test_images, test_labels from GDrive

# 4. Run the app
cd app
uvicorn main:app --reload

```

## Notes

- If the React app can't accept whole folders, we might need a more elaborate solution for `SavedModel` types. Meaning, we might need a form that accepts all the different files of a `SavedModel` and then we can construct the proper file structure in the backend.
- `.hdf5` is a single-file type so there is no problems here.