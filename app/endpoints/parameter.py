from fastapi import APIRouter, Depends
from app.controllers.parameter_handler import Parameter_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models


from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var

nexus1 = Nexus1DataBase(var.MYSQL_URL)
router = APIRouter()
parameterController = Parameter_Controller(nexus1)

@router.get("/healthz")
async def parameter_healthz(current_user: dict = Depends(get_current_user)):
    return parameterController.healthz()

@router.post('/create')
async def create_parameter(body: models.ParameterCreate,current_user: dict = Depends(get_current_user)):
    return parameterController.create_parameter(body)

@router.post('/delete')
async def delete_parameter(body: models.ParameterDelete,current_user: dict = Depends(get_current_user)):
    return parameterController.delete_parameter(body)
  
@router.get('/get_all')
async def get_all_parameter(current_user: dict = Depends(get_current_user)):
    return parameterController.get_all()

@router.post('/update')
async def update_parameter(body: models.ParameterUpdate,current_user: dict = Depends(get_current_user)):
    return parameterController.update_parameter(body)