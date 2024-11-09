import os

MYSQL_URL: str = os.getenv("MYSQL_URL") if os.getenv("MYSQL_URL") != None  else "mysql://nexus1-admin:nexus1-password@0.0.0.0:3306/fastapi"