# app/main.py
from fastapi import FastAPI
from typing import Union
from app.mysql.mysql import Nexus1DataBase
from app.endpoints import shelter,dormitory,role,parameterRoom,auth,administrator,room,tenant,tenant_relationship,relationship,parameter
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.administrator_handler import Administrator_Controller
from app.controllers.parameter_handler import Parameter_Controller
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.controllers.room_handler import Room_Controller
from app.controllers.dormitory_handler import Dormitory_Controller
from app.controllers.relationship_handler import Relationship_Controller
from app.controllers.role_handler import Role_Controller
from app.controllers.shelter_handler import Shelter_Controller
from app.controllers.tenant_handler import Tenant_Controller
from app.controllers.tenant_relationship_handler import Tenant_Relationship_Controller
from app.models.models import *
import app.models.models as models
import app.utils.vars as var 







app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Origen permitido (frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)



nexusDDBB = Nexus1DataBase(var.MYSQL_URL)
nexusDDBB.init_database()
#controladores
#diccionario generador para preparar la base de datos correctamente
nexusDDBB.prepare_database()



app.include_router(shelter.router,prefix = "/shelter")
app.include_router(dormitory.router,prefix = "/dormitory")
app.include_router(role.router,prefix = "/role")
app.include_router(parameterRoom.router,prefix = "/parameter_room")
app.include_router(parameter.router,prefix = "/parameter")
app.include_router(administrator.router,prefix = "/admnistrator")
app.include_router(room.router,prefix= "/room")
app.include_router(tenant.router,prefix = "/tenant")
app.include_router(relationship.router,prefix = "/relationship")
app.include_router(tenant_relationship.router,prefix = "/tenantRelationship")
app.include_router(auth.router,prefix = "/auth")


