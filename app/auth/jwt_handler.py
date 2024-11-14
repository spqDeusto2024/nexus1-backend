import jwt
from datetime import datetime, timedelta
from app.utils.vars import TOKEN_AUTH_SECRET_KEY

SECRET_KEY = TOKEN_AUTH_SECRET_KEY  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    """
    Generates a JSON Web Token (JWT) with an expiration time.

    Parameters:
        data (dict): A dictionary of data to include in the token payload.

    Returns:
        str: A JWT token encoded with the specified data and expiration time.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    """
    Verifies the validity of a JWT token, returning the decoded payload if valid.

    Parameters:
        token (str): The JWT token to be verified.

    Returns:
        dict or None: Decoded token data if the token is valid; None if expired or invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
