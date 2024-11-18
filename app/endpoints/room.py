from fastapi import APIRouter, Depends
from app.controllers.room_handler import Room_Controller
from app.auth.dependencies import get_current_user

import app.models.models as models

router = APIRouter()
roomController = Room_Controller()

@router.get("/healthz")
async def room_healthz(current_user: dict = Depends(get_current_user)):
    return roomController.healthz()

@router.post('/create')
async def create_room(body: models.RoomCreate,current_user: dict = Depends(get_current_user)):
    return roomController.create_room(body)

@router.post('/delete')
async def delete_room(body: models.RoomDelete,current_user: dict = Depends(get_current_user)):
    return roomController.delete_room(body)
  
@router.get('/get_all')
async def get_all_room(current_user: dict = Depends(get_current_user)):
    return roomController.get_all()

@router.post('/update')
async def update_room(body: models.RoomUpdate,current_user: dict = Depends(get_current_user)):
    return roomController.update_room(body)