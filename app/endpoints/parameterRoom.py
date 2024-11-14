from fastapi import APIRouter, Depends
from app.controllers.parameter_room_handler import ParameterRoom_Controller
import app.models.models as models

router = APIRouter()
parameterRoomController = ParameterRoom_Controller()

@router.get("/healthz")
async def parameterRoom_healthz():
    return parameterRoomController.healthz()

@router.post('/create')
async def create_parameterRoom(body: models.ParameterRoomCreate):
    return parameterRoomController.create_parameterRoom(body)

@router.post('/delete')
async def delete_parameterRoom(body: models.ParameterRoomDelete):
    return parameterRoomController.delete_ParameterRoom(body)
  
@router.get('/get_all')
async def get_all_parameterRoom():
    return parameterRoomController.get_all()

@router.post('/update')
async def update_parameterRoom(body: models.ParameterRoomUpdate):
    return parameterRoomController.update_parameterRoom(body)