# app/endpoints/auth.py
from fastapi import APIRouter, Depends
from app.models import models
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.auth_handler import Auth_Controller
from typing import Annotated
from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var

nexus1 = Nexus1DataBase(var.MYSQL_URL)


router = APIRouter()
authController = Auth_Controller(nexus1)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return authController.login(form_data)
