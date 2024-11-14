from fastapi import APIRouter, Depends
from app.controllers.dormitory_handler import Dormitory_Controller
import app.models.models as models

router = APIRouter()
dormitoryController = Dormitory_Controller()

@router.get("/healthz")
async def dormitory_healthz():
    return dormitoryController.healthz()

@router.post('/create')
async def create_dormitory(body: models.DormitoryCreate):
    return dormitoryController.create_dormitory(body)

@router.post('/delete')
async def delete_dormitory(body: models.DormitoryCreate):
    return dormitoryController.delete_dormitory(body)
  
@router.get('/get_all')
async def get_all_dormitory():
    return dormitoryController.get_all()

@router.post('/update')
async def update_dormitory(body: models.DormitoryUpdate):
    return dormitoryController.update_dormitory(body)