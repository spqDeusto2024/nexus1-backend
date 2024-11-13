# app/main.py
from fastapi import FastAPI
from typing import Union
from app.controllers.shelter_handler import Shelter_Controller
from app.controllers.dormitory_handler import Dormitory_Controller
from app.controllers.role_handler import Role_Controller
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.mysql.mysql import Nexus1DataBase

import app.models.models as models
import app.utils.vars as var 




app = FastAPI()
nexusDDBB = Nexus1DataBase(var.MYSQL_URL)
shelterController = Shelter_Controller()
dormitoryController = Dormitory_Controller()
RoleController = Role_Controller()
ParameterRoomController = ParameterRoom_Controller()

@app.on_event("startup")
def startup():
    """
    This route gets called when firts GET is realized from the browser.
    It prepares the databse creating all models defined in the project.
    If some exception is catched it is pritned on terminal,if is not
    prints on terminal that databse has succesfully launched.

    Parameters:
        None

    Returns:
        None
    """
    try:
        nexusDDBB.init_database()   
        print("DDBB STARTED")
    except Exception as e:
        print("ERROR WHILE STARTING DDBB")
        print(str(e))




# @app.get("/") 
# def read_root():
#     # GENERATE CHANGES HERE TO PROVE SYNC STAGE
#     return {"message": "Hello, Dartañan!"}

# @app.get("/prueba_manuel")
# def read_root():
#     # GENERATE CHANGES HERE TO PROVE SYNC STAGE
#     return {"message": "Hello, Manuel!"}


@app.get('/shelter/healthz')
async def shelter_healthz():
  return shelterController.healthz()

@app.post('/shelter/create')
async def create_shelter(body: models.ShelterCreate):
  return shelterController.create_shelter(body)

@app.post('/shelter/delete')
async def delete_shelter(body: models.ShelterDelete):
  return shelterController.delete_shelter(body)
  
@app.get('/shelter/get_all')
async def get_all_shelters():
  return shelterController.get_all()

@app.post('/shelter/update')
async def update_shelter(body: models.ShelterUpdate):
  return shelterController.update_shelter(body)


@app.get('/dormitory/healthz')
async def dormitory_healthz():
  return dormitoryController.healthz()

@app.post('/dormitory/create')
async def create_dormitory(body: models.DormitoryCreate):
  return dormitoryController.create_dormitory(body)

@app.post('/dormitory/delete')
async def delete_dormitory(body: models.DormitoryDelete):
  return dormitoryController.delete_dormitory(body)
  
@app.get('/dormitory/get_all')
async def get_all_dormitory():
  return dormitoryController.get_all()

@app.post('/dormitory/update')
async def update_dormitory(body: models.DormitoryUpdate):
  return dormitoryController.update_dormitory(body)


@app.get('/Role/healthz')
async def Role_healthz():
  return RoleController.healthz()

@app.post('/Role/create')
async def create_role(body: models.RoleCreate):
  return RoleController.create_role(body)

@app.post('/Role/delete')
async def delete_roles(body: models.RoleDelete):
  return RoleController.delete_Role(body)
  
@app.get('/Role/get_all')
async def get_all_roles():
  return RoleController.get_all()

@app.post('/Role/update')
async def update_role(body: models.RoleUpdate):
  return RoleController.update_Role(body)



@app.get('/ParameterRoom/healthz')
async def ParameterRoom_healthz():
  return ParameterRoomController.healthz()

@app.post('/ParameterRoom/create')
async def create_parameterRoom(body: models.ParameterRoomCreate):
  return ParameterRoomController.create_parameterRoom(body)

@app.post('/ParameterRoom/delete')
async def delete_parameterRoom(body: models.ParameterRoomDelete):
  return ParameterRoomController.delete_ParameterRoom(body)
  
@app.get('/ParameterRoom/get_all')
async def get_all_parameterRoom():
  return ParameterRoomController.get_all()

@app.post('/ParameterRoom/update')
async def update_parameterRoom(body: models.ParameterRoomUpdate):
  return ParameterRoomController.update_ParameterRoom(body)