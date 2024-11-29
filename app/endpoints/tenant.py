from fastapi import APIRouter, Depends
from app.controllers.tenant_handler import Tenant_Controller
from app.auth.dependencies import get_current_user
import app.models.models as models
from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var

nexus1 = Nexus1DataBase(var.MYSQL_URL)

router = APIRouter()
tenantController = Tenant_Controller(nexus1)

@router.get("/healthz")
async def tenant_healthz(current_user: dict = Depends(get_current_user)):
    return tenantController.healthz()

@router.post('/create')
async def create_tenant(body: models.TenantCreate,current_user: dict = Depends(get_current_user)):
    return tenantController.create_tenant(body)

@router.post('/delete')
async def delete_tenant(body: models.TenantDelete,current_user: dict = Depends(get_current_user)):
    return tenantController.delete_tenant(body)
  
@router.get('/get_all')
async def get_all_tenant(current_user: dict = Depends(get_current_user)):
    return tenantController.get_all()

@router.post('/update')
async def update_tenant(body: models.TenantUpdate,current_user: dict = Depends(get_current_user)):
    return tenantController.update_tenant(body)