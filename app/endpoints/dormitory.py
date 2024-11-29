from fastapi import APIRouter, Depends
from app.controllers.dormitory_handler import Dormitory_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models
from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var

nexus1 = Nexus1DataBase(var.MYSQL_URL)

router = APIRouter()
dormitoryController = Dormitory_Controller(nexus1)

@router.get("/healthz")
async def dormitory_healthz(current_user: dict = Depends(get_current_user)):
    return dormitoryController.healthz()

@router.post('/create')
async def create_dormitory(body: models.DormitoryCreate,current_user: dict = Depends(get_current_user)):
    return dormitoryController.create_dormitory(body)

@router.post('/delete')
async def delete_dormitory(body: models.DormitoryDelete,current_user: dict = Depends(get_current_user)):
    return dormitoryController.delete_dormitory(body)
  
@router.get('/get_all')
async def get_all_dormitory(current_user: dict = Depends(get_current_user)):
    return dormitoryController.get_all()

@router.post('/update')
async def update_dormitory(body: models.DormitoryUpdate,current_user: dict = Depends(get_current_user)):
    return dormitoryController.update_dormitory(body)