# app/endpoints/auth.py
from fastapi import APIRouter, Depends
from app.models import models
from app.controllers.auth_handler import Auth_Controller

router = APIRouter()
authController = Auth_Controller()

@router.post("/login")
async def login(credentials: models.LoginCredentials):
    return authController.login(credentials)
