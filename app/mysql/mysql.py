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
        self.Session = sessionmaker(bind=self.engine)
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
        try:
            inspector = inspect(self.engine)
            if "administrators" not in inspector.get_table_names():
                Base.metadata.create_all(self.engine)
                print("tables created on nexus")
            else:
                print("Tables already exists")
            return
        except Exception as e:
            raise e

    
    def prepare_database(self):
        """
        Garantiza que todas las tablas tengan al menos un registro.

        Args:
            session: Sesión de SQLAlchemy para interactuar con la base de datos.
        """
        
        session = self.Session()
        # Verificar e insertar en la tabla Shelter
        if not session.query(Shelter).first():
            shelter = Shelter(name="Default Shelter", description="This is the default shelter.")
            session.add(shelter)
            session.commit()  # Necesario para generar el ID y usarlo en las dependencias

        # Verificar e insertar en la tabla Room
        if not session.query(Room).first():
            shelter_id = session.query(Shelter.id).first()[0]  # Recuperar el ID del shelter
            room = Room(
                name="Default Room",
                description="This is the default room.",
                id_shelter=shelter_id,
                capacity=10,
                actual_tenant_number=0,
                availability=True
            )
            session.add(room)
            session.commit()

        # Verificar e insertar en la tabla Role
        if not session.query(Role).first():
            role = Role(
                name="Default Role",
                description="This is the default role.",
                id_room_relationship=session.query(Room.id).first()[0]
            )
            session.add(role)
            session.commit()

        # Verificar e insertar en la tabla Dormitory
        if not session.query(Dormitory).first():
            dormitory = Dormitory(
                name="Default Dormitory",
                description="This is the default dormitory.",
                id_shelter=session.query(Shelter.id).first()[0],
                capacity=20,
                actual_tenant_number=0,
                availability=True
            )
            session.add(dormitory)
            session.commit()

        # Verificar e insertar en la tabla Tenant
        if not session.query(Tenant).first():
            tenant = Tenant(
                name="Default Tenant",
                surname="Default Surname",
                age="25",
                status=True,
                genre="Non-binary",
                id_role=session.query(Role.id).first()[0],
                id_dormitory=session.query(Dormitory.id).first()[0]
            )
            session.add(tenant)
            session.commit()

        # Verificar e insertar en la tabla Relationship
        if not session.query(Relationship).first():
            relationship = Relationship(
                name="Default Relationship",
                description="This is the default relationship."
            )
            session.add(relationship)
            session.commit()

        # Verificar e insertar en la tabla Parameter
        if not session.query(Parameter).first():
            parameter = Parameter(
                name="Default Parameter",
                description="This is the default parameter.",
                max_value=100.0,
                min_value=0.0
            )
            session.add(parameter)
            session.commit()

        # Verificar e insertar en la tabla ParameterRoom
        if not session.query(ParameterRoom).first():
            parameter_room = ParameterRoom(
                id_room=session.query(Room.id).first()[0],
                id_parameter=session.query(Parameter.id).first()[0],
                date=func.now(),
                value=50.0
            )
            session.add(parameter_room)
            session.commit()

        # Verificar e insertar en la tabla TenantRelationship
        if not session.query(TenantRelationship).first():
            tenant_relationship = TenantRelationship(
                id_tenant_1=session.query(Tenant.id).first()[0],
                id_tenant_2=session.query(Tenant.id).first()[0],  # Puedes crear un segundo tenant si prefieres
                id_relationship=session.query(Relationship.id).first()[0]
            )
            session.add(tenant_relationship)
            session.commit()

        print("Database preparation complete: all tables have at least one record.")

