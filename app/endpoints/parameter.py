from fastapi import APIRouter, Depends
from app.controllers.parameter_handler import Parameter_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models

router = APIRouter()
parameterController = Parameter_Controller()

@router.get("/healthz")
async def parameter_healthz(current_user: dict = Depends(get_current_user)):
    return parameterController.healthz()

@router.post('/create')
async def create_parameter(body: models.ParameterCreate,current_user: dict = Depends(get_current_user)):
    return parameterController.create_parameter(body)

@router.post('/delete')
async def delete_parameter(body: models.ParameterDelete,current_user: dict = Depends(get_current_user)):
    return parameterController.delete_Parameter(body)
  
@router.get('/get_all')
async def get_all_parameter(current_user: dict = Depends(get_current_user)):
    return parameterController.get_all()

@router.post('/update')
async def update_parameter(body: models.ParameterUpdate,current_user: dict = Depends(get_current_user)):
    return parameterController.update_parameter(body)