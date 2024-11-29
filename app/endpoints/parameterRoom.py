from fastapi import APIRouter, Depends
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models

from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var

nexus1 = Nexus1DataBase(var.MYSQL_URL)

router = APIRouter()
parameterRoomController = ParameterRoom_Controller(nexus1)

@router.get("/healthz")
async def parameterRoom_healthz(current_user: dict = Depends(get_current_user)):
    return parameterRoomController.healthz()

@router.post('/create')
async def create_parameterRoom(body: models.ParameterRoomCreate,current_user: dict = Depends(get_current_user)):
    return parameterRoomController.create_parameterRoom(body)

@router.post('/delete')
async def delete_parameterRoom(body: models.ParameterRoomDelete,current_user: dict = Depends(get_current_user)):
    return parameterRoomController.delete_ParameterRoom(body)
  
@router.get('/get_all')
async def get_all_parameterRoom(current_user: dict = Depends(get_current_user)):
    return parameterRoomController.get_all()

@router.post('/update')
async def update_parameterRoom(body: models.ParameterRoomUpdate,current_user: dict = Depends(get_current_user)):
    return parameterRoomController.update_parameterRoom(body)