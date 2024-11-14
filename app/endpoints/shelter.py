from fastapi import APIRouter, Depends
from app.controllers.shelter_handler import Shelter_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models

router = APIRouter()
shelterController = Shelter_Controller()

@router.get("/healthz")
async def shelter_healthz(current_user: dict = Depends(get_current_user)):
    return shelterController.healthz()

@router.post('/create')
async def create_shelter(body: models.ShelterCreate,current_user: dict = Depends(get_current_user)):
    return shelterController.create_shelter(body)

@router.post('/delete')
async def delete_shelter(body: models.ShelterDelete,current_user: dict = Depends(get_current_user)):
    return shelterController.delete_shelter(body)
  
@router.get('/get_all')
async def get_all_shelters(current_user: dict = Depends(get_current_user)):
    return shelterController.get_all()

@router.post('/update')
async def update_shelter(body: models.ShelterUpdate,current_user: dict = Depends(get_current_user)):
    return shelterController.update_shelter(body)