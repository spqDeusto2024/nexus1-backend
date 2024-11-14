# app/main.py
from fastapi import FastAPI
from typing import Union
from app.controllers.shelter_handler import Shelter_Controller
from app.controllers.dormitory_handler import Dormitory_Controller
from app.controllers.role_handler import Role_Controller
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.mysql.mysql import Nexus1DataBase
from app.endpoints import shelter,dormitory,role,parameterRoom

import app.models.models as models
import app.utils.vars as var 




app = FastAPI()
nexusDDBB = Nexus1DataBase(var.MYSQL_URL)
shelterController = Shelter_Controller()
dormitoryController = Dormitory_Controller()
roleController = Role_Controller()
parameterRoomController = ParameterRoom_Controller()

app.include_router(shelter.router,prefix = "/shelter")
app.include_router(dormitory.router,prefix = "/dormitory")
app.include_router(role.router,prefix = "/role")
app.include_router(parameterRoom.router,prefix = "/parameter_room")