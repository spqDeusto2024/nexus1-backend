from fastapi import APIRouter, Depends
from app.controllers.administrator_handler import Administrator_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models
from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var

nexus1 = Nexus1DataBase(var.MYSQL_URL)
router = APIRouter()
adminController = Administrator_Controller(nexus1)

@router.get("/healthz")
async def administrator_healthz(current_user: dict = Depends(get_current_user)):
    return adminController.healthz()

#en principio no depende de autenticacion puedes crearte una cuenta reigstrar sin token
@router.post('/create')
async def create_administrator(body: models.AdministratorCreate):
    return adminController.create_administrator(body)

@router.post('/delete')
async def delete_administrator(body: models.AdministratorDelete,current_user: dict = Depends(get_current_user)):
    return adminController.delete_administrator(body)
  
@router.get('/get_all')
async def get_all_administrators(current_user: dict = Depends(get_current_user)):
    return adminController.get_all()

@router.post('/update')
async def update_administrator(body: models.AdministratorUpdate,current_user: dict = Depends(get_current_user)):
    return adminController.update_administrator(body)