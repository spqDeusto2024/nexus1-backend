# app/main.py
from fastapi import FastAPI
from typing import Union
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var 
import app.models.models.as modelos


def iniciarBBDD() -> None:
    nexusDDBB = Nexus1DataBase(var.MYSQL_URL)
    nexusDDBB.init_database()
    print("llamado initialize")
    return 


app = FastAPI()
iniciarBBDD()


@app.get("/")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    print("pepero")
    return {"message": "Hello, Dartañan!"}

@app.get("/prueba_manuel")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Manuel!"}