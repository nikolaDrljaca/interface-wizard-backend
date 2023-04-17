## General TODO's - as of March 2023

- [x] Upload model response should return a formatted date.
- [x] Consistent file naming.
- [x] Route structure - drop the 'model' part, unnecessary.
- [x] Check that uploaded files are pickles -> (Error handling)[https://fastapi.tiangolo.com/tutorial/handling-errors/]
- [x] Repository cleanup for a concise v1 version, v1 in reference to the metadata file.
- [x] Endpoint for metadata structure and example metadata object. (JSON)
- [x] Rename processing to services and make appropriate changes inside.
- [x] Move directory utils to services.

## Features moving forward

- [x] Predictions are saved to DB.
- [x] Endpoints for previous prediction retrieval.
- [x] Endpoints for Model Metadata retrieval.
- [ ] Service for outdated model cleanup.
- [x] Deployment strategies - `.env` and `Dockerfile` files.
- [ ] Deployment strategies - containerizing and running.
- [ ] Logging implementation.
- [ ] Documentation.

## DEL1

- [x] Basic workflow for predictions
- [x] Data persistence for metadata
- [x] Data persistence for predictions

# DEL2

- [x] Endpoints for metadata retrieval
- [x] Finished prediction workflow
- [x] Enpoints for prediction retrieval

# DEL3

- [ ] Finished enpoints
- [ ] Outdated model cleanup service

# DEL4

- [ ] Finished workflows
- [ ] Finished cleanup service
- [ ] Revisions
