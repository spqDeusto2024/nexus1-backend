import pytest
from sqlalchemy.orm import Session
from app.models.models import *  # Tus modelos Pydantic
from app.controllers.auth_handler import Auth_Controller
from app.controllers.administrator_handler import Administrator_Controller
from mysql import TestDataBase  # Tu clase para la base de datos
from sqlalchemy import create_engine
import app.mysql.models as mysql_models  # El modelo SQLAlchemy de Shelter, que usas en la base de datos
import app.utils.vars as var
from datetime import datetime
from app.models.response_models import ResponseModel
from app.auth.jwt_handler import create_access_token
from fastapi import HTTPException
from app.utils.hashing import hash_password
from app.auth.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


def test_login_success():
    db = TestDataBase("mysql://test:test@test-database:3306/test")

    admin_controller = Administrator_Controller(db)
    request = AdministratorCreate(username = "tumadre",password ="kula",created_at = datetime.now())
    response = admin_controller.create_administrator(request)
    print(response)


    auth_controller = Auth_Controller(db)

    form_data = OAuth2PasswordRequestForm(
        username="tumadre",
        password="kula",
        scope=""
    )
    response = auth_controller.login(form_data)
    assert response["token_type"] == "bearer"
    assert "access_token" in response

   

# def test_login_invalid_username():
#     db = TestDataBase("mysql://test:test@test-database:3306/test")
#     admin_controller = Administrator_Controller(db)
#     request = AdministratorCreate(username = "tumadre",password ="kula",created_at = datetime.now())
#     admin_controller.create_administrator(request)

#     auth_controller = Auth_Controller(db)
#     form_data = OAuth2PasswordRequestForm(
#         username="non_existent_user",
#         password="kula",
#         scope=""
#     )

#     try:
#         auth_controller.login(form_data)
#         assert False, "Se esperaba una excepción HTTPException"
#     except HTTPException as e:
#         assert e.status_code == 401
#         assert e.detail == "Invalid username or password"

# def test_login_invalid_password():
#     db = TestDataBase("mysql://test:test@test-database:3306/test")
#     admin_controller = Administrator_Controller(db)
#     request = AdministratorCreate(username = "tumadre",password ="kula",created_at = datetime.now())
#     admin_controller.create_administrator(request)

#     auth_controller = Auth_Controller(db)

#     form_data = OAuth2PasswordRequestForm(
#         username="tumadre",
#         password="pepe",
#         scope=""
#     )

#     try:
#         auth_controller.login(form_data)
#         assert False, "Se esperaba una excepción HTTPException"
#     except HTTPException as e:
#         assert e.status_code == 401
#         assert e.detail == "Invalid username or password"
