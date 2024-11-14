from passlib.context import CryptContext

# Set up the password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a plain password for secure storage.

    Parameters:
        password (str): The plain password to be hashed.

    Returns:
        str: The hashed version of the input password.
    """
    # Hash the password using bcrypt (configured in the pwd_context) and return the hashed value
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that a plain password matches its hashed counterpart.

    Parameters:
        plain_password (str): The plain password input from the user.
        hashed_password (str): The hashed password stored in the database.

    Returns:
        bool: True if the plain password matches the hashed password; False otherwise.
    """
    # Compare the plain password with the hashed password using bcrypt
    return pwd_context.verify(plain_password, hashed_password)
