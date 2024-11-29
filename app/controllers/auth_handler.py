# app/controllers/auth_handler.py
from fastapi import HTTPException, status,Depends
from app.utils.hashing import verify_password
from app.models import models
from app.models.response_models import ResponseModel
from app.controllers.administrator_handler import Administrator_Controller   # Function to get a user from the database
from app.auth.jwt_handler import create_access_token,verify_token
from typing import Annotated
from fastapi.security import  OAuth2PasswordRequestForm
from app.mysql.mysql import Nexus1DataBase
import app.utils.vars as var


class Auth_Controller:
    """
    A controller for handling authentication operations like login.

    Attributes:
        db (object): An instance of a database (e.g., Nexus1DataBase) that will be used for database operations.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Auth_Controller class.

        Parameters:
            db (object): An instance of a database (e.g., Nexus1DataBase) that will be used to create the database connection.
        """
        self.db = db

    def login(self, form_data: OAuth2PasswordRequestForm):
        """
        Authenticates a user by verifying their username and password.
        
        This method checks if the provided username exists in the database and 
        if the password matches the stored (hashed) password. If successful, 
        it generates and returns an access token for the user.
        
        Args:
            form_data (OAuth2PasswordRequestForm): The credentials provided by the user for login.

        Returns:
            dict: A dictionary containing the access token and token type if authentication is successful.

        Raises:
            HTTPException: If the credentials are invalid, an HTTP 401 Unauthorized exception is raised.
        """
        admin_controller = Administrator_Controller(self.db)  # Utiliza la base de datos pasada al constructor
        user = admin_controller.get_admin_by_username(form_data.username).data
        
        if not user:
            print(f"No admin exists with username: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        
        if not verify_password(form_data.password, user.password):
            print("Error: incorrect password")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        
        print("Token created successfully")
        token = create_access_token(data={"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
