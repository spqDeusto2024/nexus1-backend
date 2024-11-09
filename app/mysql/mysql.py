import sqlalchemy as db
from app.mysql.base import Base
from app.mysql.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect



class Nexus1DataBase():
    """
    Class used for centralizng the database creation and preparing methods.

    Attributes:
        attribute1 (engine): sqlalchemy imported module to manage remote database.
    """
    def __init__(self, url: str) -> None:
        engine = db.create_engine(url)
        self.engine = engine
        pass

    def init_database(self):
        """
        This method is used to create the database.It checks wether if
        the table administrators is created,what it would mean that all tables had been created
        before,and if it does not exists,this function creates all tables on the database.

        Parameters:
            param1 (url): URL for the location of the remote database.
            

        Returns:
            None
        """
        inspector = inspect(self.engine)
        if "administrators" not in inspector.get_table_names():
            Base.metadata.create_all(self.engine)
        else:
            print("Tables already exists")
        return
    