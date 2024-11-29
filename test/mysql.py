import sqlalchemy as db
# from base import Base
from app.mysql.models import *
from app.mysql.base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base



class TestDataBase():
    """
    Class used for centralizng the database creation and preparing methods.

    Attributes:
        attribute1 (engine): sqlalchemy imported module to manage remote database.
    """
    def __init__(self, url: str) -> None:
        try:
            engine = db.create_engine(url)
            self.engine = engine
            self.Session = sessionmaker(bind=self.engine)
            pass
        except Exception as e:
            raise e
        print("Init realizado correctamente")
    
  

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
        try:
            inspector = inspect(self.engine)
            # Drop all existing tables
            Base.metadata.drop_all(self.engine)
            print("Dropped all existing tables.")

            # Create all tables
            Base.metadata.create_all(self.engine)
            print("Created tables on the database.")
        
            return
        except Exception as e:
            raise e
    def get_session(self):
        """
        Method to get database connection session
        """
        return self.Session()
        

