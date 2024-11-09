# app/main.py
from fastapi import FastAPI
from typing import Union
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var 




app = FastAPI()
nexusDDBB = Nexus1DataBase(var.MYSQL_URL)

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




@app.get("/")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Dartañan!"}

@app.get("/prueba_manuel")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Manuel!"}