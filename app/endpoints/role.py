from fastapi import APIRouter, Depends
from app.controllers.role_handler import Role_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models

router = APIRouter()
roleController = Role_Controller()

@router.get("/healthz")
async def role_healthz(current_user: dict = Depends(get_current_user)):
    return roleController.healthz()

@router.post('/create')
async def create_role(body: models.RoleCreate,current_user: dict = Depends(get_current_user)):
    return roleController.create_role(body)

@router.post('/delete')
async def delete_role(body: models.RoleDelete,current_user: dict = Depends(get_current_user)):
    return roleController.delete_role(body)
  
@router.get('/get_all')
async def get_all_roles(current_user: dict = Depends(get_current_user)):
    return roleController.get_all()

@router.post('/update')
async def update_role(body: models.RoleUpdate,current_user: dict = Depends(get_current_user)):
    return roleController.update_role(body)