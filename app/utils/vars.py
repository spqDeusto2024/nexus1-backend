import os

MYSQL_URL: str = os.getenv("MYSQL_URL") if os.getenv("MYSQL_URL") is not None else "mysql://nexus1-admin:nexus1-password@0.0.0.0:3306/fastapi"
TOKEN_AUTH_SECRET_KEY: str = os.getenv("TOKEN_AUTH_SECRET_KEY", "MANUELESUNANIMAL_G_G_G_11")
MYSQL_URL_TEST : str = "mysql://test:test@test-database:3306/test"