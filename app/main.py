# app/main.py
from fastapi import FastAPI
from typing import Union
from app.mysql.mysql import Nexus1DataBase
from app.endpoints import shelter,dormitory,role,parameterRoom,auth,administrator,room,tenant,tenant_relationship,relationship,parameter

import app.models.models as models
import app.utils.vars as var 







app = FastAPI()
nexusDDBB = Nexus1DataBase(var.MYSQL_URL)

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


