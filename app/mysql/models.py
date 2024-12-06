from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.mysql.base import Base
from sqlalchemy.sql import func

class Tenant(Base):
    """
    Represents a tenant in the system.

    Attributes:
        id (int): The unique identifier of the tenant.
        id_role (int): The role identifier of the tenant (ForeignKey).
        id_dormitory (int): The dormitory identifier where the tenant stays (ForeignKey).
        name (str): The name of the tenant.
        surname (str): The surname of the tenant.
        age (str): The age of the tenant.
        status (bool): The current status of the tenant (active/inactive).
        genre (str): The genre of the tenant.
        created_at (DateTime): The timestamp when the tenant record was created.
    """

    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_role = Column(Integer, ForeignKey("roles.id"), nullable=True)
    id_dormitory = Column(Integer, ForeignKey("dormitories.id"), nullable=True)
    name = Column(String(255), unique=True, nullable=False)
    surname = Column(String(255), unique=True, nullable=False)
    age = Column(String(50), nullable=True)
    status = Column(Boolean, nullable=True)
    genre = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False,default=func.now())


    role = relationship("Role", back_populates="tenants")
    dormitory = relationship("Dormitory", back_populates="tenants")


class Role(Base):
    """
    Represents a role in the system.

    Attributes:
        id (int): The unique identifier of the role.
        name (str): The name of the role.
        description (str): A description of the role.
        id_room_relationship (int): The room identifier associated with this role (ForeignKey).
        created_at (DateTime): The timestamp when the role record was created.
    """
    
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=True)
    id_room_relationship = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    created_at = Column(DateTime, nullable=False,default=func.now())

    tenants = relationship("Tenant", back_populates="role")
    room_relationship = relationship("Room", back_populates="roles")


class Room(Base):
    """
    Represents a room in the shelter system.

    Attributes:
        id (int): The unique identifier of the room.
        id_shelter (int): The shelter identifier the room belongs to (ForeignKey).
        name (str): The name of the room.
        description (str): The description of the room.
        capacity (int): The capacity of the room.
        actual_tenant_number (int): The current number of tenants in the room.
        availability (bool): The availability status of the room.
        created_at (DateTime): The timestamp when the room record was created.
    """

    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_shelter = Column(Integer, ForeignKey("shelters.id"), nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    capacity = Column(Integer, nullable=True)
    actual_tenant_number = Column(Integer, nullable=True)
    availability = Column(Boolean, nullable=True)
    created_at = Column(DateTime, nullable=False,default=func.now())

    shelter = relationship("Shelter", back_populates="rooms")
    roles = relationship("Role", back_populates="room_relationship")
    parameters = relationship("ParameterRoom", back_populates="room")


class Dormitory(Base):
    """
    Represents a dormitory in the shelter system.

    Attributes:
        id (int): The unique identifier of the dormitory.
        id_shelter (int): The shelter identifier the dormitory belongs to (ForeignKey).
        name (str): The name of the dormitory.
        description (str): The description of the dormitory.
        capacity (int): The capacity of the dormitory.
        actual_tenant_number (int): The current number of tenants in the dormitory.
        availability (bool): The availability status of the dormitory.
        created_at (DateTime): The timestamp when the dormitory record was created.
    """

    __tablename__ = "dormitories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_shelter = Column(Integer, ForeignKey("shelters.id"), nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    capacity = Column(Integer, nullable=True)
    actual_tenant_number = Column(Integer, nullable=True)
    availability = Column(Boolean, nullable=True)
    created_at = Column(DateTime, nullable=False,default=func.now())

    shelter = relationship("Shelter", back_populates="dormitories")
    tenants = relationship("Tenant", back_populates="dormitory")


class Administrator(Base):
    """
    Represents an administrator in the system.

    Attributes:
        id (int): The unique identifier of the administrator.
        username (str): The username of the administrator.
        password (str): The password for the administrator account.
        created_at (DateTime): The timestamp when the administrator account was created.
    """

    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())


class ParameterRoom(Base):
    """
    Represents the relationship between a room and a parameter in the system.

    Attributes:
        id (int): The unique identifier of the parameter relationship.
        id_room (int): The room identifier associated with this parameter (ForeignKey).
        id_parameter (int): The parameter identifier associated with this room (ForeignKey).
        date (DateTime): The date the parameter value was recorded.
        value (float): The value of the parameter for the room.
        created_at (DateTime): The timestamp when the parameter value was recorded.
    """

    __tablename__ = "parameter_rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_room = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    id_parameter = Column(Integer, ForeignKey("parameters.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())

    room = relationship("Room", back_populates="parameters")
    parameter = relationship("Parameter", back_populates="parameter_rooms")


class Parameter(Base):
    """
    Represents a parameter in the system.

    Attributes:
        id (int): The unique identifier of the parameter.
        name (str): The name of the parameter.
        description (str): A description of the parameter.
        max_value (float): The maximum value of the parameter for the room.
        min_value (float): The minimum value of the parameter for the room.
        created_at (DateTime): The timestamp when the parameter record was created.
    """

    __tablename__ = "parameters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    max_value = Column(Float, nullable=False)
    min_value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())

    parameter_rooms = relationship("ParameterRoom", back_populates="parameter")


class Shelter(Base):
    """
    Represents a shelter in the system.

    Attributes:
        id (int): The unique identifier of the shelter.
        name (str): The name of the shelter.
        description (str): The description of the shelter.
        created_at (DateTime): The timestamp when the shelter record was created.
    """

    __tablename__ = "shelters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())

    rooms = relationship("Room", back_populates="shelter")
    dormitories = relationship("Dormitory", back_populates="shelter")


class Relationship(Base):
    """
    Represents a relationship between tenants in the system.

    Attributes:
        id (int): The unique identifier of the relationship.
        name (str): The name of the relationship.
        description (str): A description of the relationship.
        created_at (DateTime): The timestamp when the relationship record was created.
    """

    __tablename__ = "relationships"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())


class TenantRelationship(Base):
    """
    Represents a relationship between two tenants.

    Attributes:
        id_tenant_relationship (int): The unique identifier of the tenant relationship.
        id_tenant_1 (int): The first tenant involved in the relationship (ForeignKey).
        id_tenant_2 (int): The second tenant involved in the relationship (ForeignKey).
        id_relationship (int): The relationship type identifier (ForeignKey).
        created_at (DateTime): The timestamp when the tenant relationship was created.
    """
    
    __tablename__ = "tenant_relationships"
    id_tenant_relationship = Column(Integer, primary_key=True, autoincrement=True)
    id_tenant_1 = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    id_tenant_2 = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    id_relationship = Column(Integer, ForeignKey("relationships.id"), nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())
