## General TODO's - as of March 2023
- [x] Upload model response should return a formatted date. 
- [x] Consistent file naming.
- [x] Route structure - drop the 'model' part, unnecessary.
- [x] Check that uploaded files are pickles -> (Error handling)[https://fastapi.tiangolo.com/tutorial/handling-errors/]
- [x] Repository cleanup for a concise v1 version, v1 in reference to the metadata file.
- [ ] Endpoint for metadata structure and example metadata object. (JSON)
- [x] Rename processing to services and make appropriate changes inside.
- [x] Move directory utils to services. 

## Features moving forward
- [ ] Predictions are saved to DB.
- [ ] Endpoints for previous prediction retrieval.
- [ ] Endpoints for Model Metadata retrieval. 
- [ ] Service for outdated model cleanup. 
- [ ] Deployment strategies - `.env` and `Dockerfile` files.
- [ ] Deployment strategies - containerizing and running.
- [ ] Logging implementation. 
- [ ] Documentation.