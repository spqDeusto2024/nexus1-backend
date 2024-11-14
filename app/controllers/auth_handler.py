# app/controllers/auth_handler.py
from fastapi import HTTPException, status
from app.utils.auth import authenticate_user, create_access_token, verify_password
from app.models import models
from app.db import get_user_by_username  # Function to get a user from the database

class Auth_Controller:
    """
    A controller for handling authentication operations like login.

    Attributes:
        None
    
    Methods:
        login(credentials: models.LoginCredentials): Authenticates the user by checking the provided credentials.
    """
    
    def __init__(self):
        pass

    def login(self, credentials: models.LoginCredentials):
        """
        Authenticates a user by verifying their username and password.
        
        This method checks if the provided username exists in the database and 
        if the password matches the stored (hashed) password. If successful, 
        it generates and returns an access token for the user.
        
        Args:
            credentials (models.LoginCredentials): The credentials provided by the user for login.

        Returns:
            dict: A dictionary containing the access token and token type if authentication is successful.

        Raises:
            HTTPException: If the credentials are invalid, an HTTP 401 Unauthorized exception is raised.
        """
        
        user = get_user_by_username(credentials.username)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",  # Invalid username
            )
        
        if not verify_password(credentials.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",  # Invalid password
            )    
        token = create_access_token(data={"sub": user.username})   
        return {"access_token": token, "token_type": "bearer"}
