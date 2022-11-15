from fastapi import APIRouter, HTTPException

router  = APIRouter(
    prefix='/eval_model'
)

'''
Predicated on a session.
1. accept_model is first, assigns ID and creates session
We might need permanent storage to keep track of sessions.
2. accept_data second, append and store all needed data 
temporarily
3. make_prediction last, use all of the above. Determine model
type, load data and respond with prediction. 
'''



@router.post('/pred_model')
async def accept_model():
    '''
    Accept the model file/folder and determine the extension
    to work with the model.
    '''
    
    return


@router.post('/pred_model/data')
async def accept_data():
    '''
    This will require a standardized JSON format to cover
    cases of differing input data.
    '''
    return


@router.get('/make')
async def make_prediction():
    return
