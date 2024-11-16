from fastapi import APIRouter, Depends
from app.controllers.tenant_relationship_handler import Tenant_Relationship_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models

router = APIRouter()
tenantRelationshipController = Tenant_Relationship_Controller()

@router.get("/healthz")
async def tenant_relationship_healthz(current_user: dict = Depends(get_current_user)):
    return tenantRelationshipController.healthz()

@router.post('/create')
async def create_tenant_relationship(body: models.TenantRelationshipCreate,current_user: dict = Depends(get_current_user)):
    return tenantRelationshipController.create_tenant_relationship(body)

@router.post('/delete')
async def delete_tenantRelationship(body: models.TenantRelationshipDelete,current_user: dict = Depends(get_current_user)):
    return tenantRelationshipController.delete_tenantRelationship(body)
  
@router.get('/get_all')
async def get_all_tenantRelationship(current_user: dict = Depends(get_current_user)):
    return tenantRelationshipController.get_all()

@router.post('/update')
async def update_tenantRelationship(body: models.DormitoryUpdate,current_user: dict = Depends(get_current_user)):
    return tenantRelationshipController.update_tenantRelationship(body)