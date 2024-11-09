# app/main.py
from fastapi import FastAPI
from typing import Union
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var 




app = FastAPI()
nexusDDBB = Nexus1DataBase(var.MYSQL_URL)

@app.on_event("startup")
def startup():
    try:
        nexusDDBB.init_database()   
        print("DDBB STARTED")
    except Exception as e:
        print("ERROR WHILE STARTING DDBB")
        print(str(e))




@app.get("/")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Dartañan!"}

@app.get("/prueba_manuel")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Manuel!"}