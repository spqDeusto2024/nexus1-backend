from fastapi import APIRouter, Depends
from app.controllers.relationship_handler import Relationship_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models

router = APIRouter()
relationshipController = Relationship_Controller()

@router.get("/healthz")
async def relationship_healthz(current_user: dict = Depends(get_current_user)):
    return relationshipController.healthz()

@router.post('/create')
async def create_relationship(body: models.RelationshipCreate,current_user: dict = Depends(get_current_user)):
    return relationshipController.create_relationship(body)

@router.post('/delete')
async def delete_relationship(body: models.RelationshipDelete,current_user: dict = Depends(get_current_user)):
    return relationshipController.delete_relationship(body)
  
@router.get('/get_all')
async def get_all_relationship(current_user: dict = Depends(get_current_user)):
    return relationshipController.get_all()

@router.post('/update')
async def update_relationship(body: models.RelationshipUpdate,current_user: dict = Depends(get_current_user)):
    return relationshipController.update_relationship(body)