from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt_handler import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Short description of the function.

    Parameters:
        token (str): Passed otken from the user sesion.

    Returns:
        payload: Return user decoded data.
    """
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload  
