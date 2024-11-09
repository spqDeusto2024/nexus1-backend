import sqlalchemy as db
from app.mysql.base import Base
from app.mysql.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect



class Nexus1DataBase():
  
  def __init__(self, url: str) -> None:
    engine = db.create_engine(url)
    self.engine = engine
    pass

  def init_database(self):
    """
    creates tables in database
    """
    inspector = inspect(self.engine)
    if "administrators" not in inspector.get_table_names():
        Base.metadata.create_all(self.engine)
    else:
        print("Tables already exists")
    return
    