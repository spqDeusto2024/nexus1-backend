# app/endpoints/auth.py
from fastapi import APIRouter, Depends
from app.models import models
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.auth_handler import Auth_Controller
from typing import Annotated


router = APIRouter()
authController = Auth_Controller()


@router.post("/login",include_in_schema=False)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return authController.login(form_data)
