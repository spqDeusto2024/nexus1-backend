# app/main.py
from fastapi import FastAPI
from typing import Union
from app.mysql.mysql import Nexus1DataBase
from app.endpoints import shelter,dormitory,role,parameterRoom,auth

import app.models.models as models
import app.utils.vars as var 




app = FastAPI()
nexusDDBB = Nexus1DataBase(var.MYSQL_URL)

app.include_router(shelter.router,prefix = "/shelter")
app.include_router(dormitory.router,prefix = "/dormitory")
app.include_router(role.router,prefix = "/role")
app.include_router(parameterRoom.router,prefix = "/parameter_room")
app.include_router(auth.router,prefix = "/auth")
