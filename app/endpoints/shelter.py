from fastapi import APIRouter, Depends
from app.controllers.shelter_handler import Shelter_Controller
import app.models.models as models

router = APIRouter()
shelterController = Shelter_Controller()

@router.get("/healthz")
async def shelter_healthz():
    return shelterController.healthz()

@router.post('/create')
async def create_shelter(body: models.ShelterCreate):
    return shelterController.create_shelter(body)

@router.post('/delete')
async def delete_shelter(body: models.ShelterDelete):
    return shelterController.delete_shelter(body)
  
@router.get('/get_all')
async def get_all_shelters():
    return shelterController.get_all()

@router.post('/update')
async def update_shelter(body: models.ShelterUpdate):
    return shelterController.update_shelter(body)