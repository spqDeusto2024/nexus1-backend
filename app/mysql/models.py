from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.mysql.base import Base  # asumiendo que tienes una clase base de SQLAlchemy

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_role = Column(Integer, ForeignKey("roles.id"))
    id_dormitory = Column(Integer, ForeignKey("dormitories.id"))
    name = Column(Text, unique=True)
    surname = Column(Text, unique=True)
    age = Column(Text)
    status = Column(Boolean)
    genre = Column(Text)
    created_at = Column(DateTime)

    role = relationship("Role", back_populates="tenants")
    dormitory = relationship("Dormitory", back_populates="tenants")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    description = Column(Integer, unique=True)
    id_room_relationship = Column(Integer, ForeignKey("rooms.id"))
    created_at = Column(DateTime)

    tenants = relationship("Tenant", back_populates="role")
    room_relationship = relationship("Room", back_populates="roles")

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_shelter = Column(Integer, ForeignKey("shelters.id"))
    name = Column(Text, unique=True)
    description = Column(Text)
    capacity = Column(Integer)
    actual_tenant_number = Column(Integer)
    availability = Column(Boolean)
    created_at = Column(DateTime)

    shelter = relationship("Shelter", back_populates="rooms")
    roles = relationship("Role", back_populates="room_relationship")
    parameters = relationship("ParameterRoom", back_populates="room")

class Dormitory(Base):
    __tablename__ = "dormitories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_shelter = Column(Integer, ForeignKey("shelters.id"))
    name = Column(Text, unique=True)
    description = Column(Text, unique=True)
    capacity = Column(Integer)
    actual_tenant_number = Column(Integer)
    availability = Column(Boolean)
    created_at = Column(DateTime)

    shelter = relationship("Shelter", back_populates="dormitories")
    tenants = relationship("Tenant", back_populates="dormitory")

class Administrator(Base):
    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text, unique=True)
    password = Column(Text)
    created_at = Column(DateTime)

class ParameterRoom(Base):
    __tablename__ = "parameter_rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_room = Column(Integer, ForeignKey("rooms.id"))
    id_parameter = Column(Integer, ForeignKey("parameters.id"))
    date = Column(DateTime)
    value = Column(Float)
    created_at = Column(DateTime)

    room = relationship("Room", back_populates="parameters")
    parameter = relationship("Parameter", back_populates="parameter_rooms")

class Parameter(Base):
    __tablename__ = "parameters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    description = Column(Text, unique=True)
    created_at = Column(DateTime)

    parameter_rooms = relationship("ParameterRoom", back_populates="parameter")

class Shelter(Base):
    __tablename__ = "shelters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    description = Column(Text, unique=True)
    created_at = Column(DateTime)

    rooms = relationship("Room", back_populates="shelter")
    dormitories = relationship("Dormitory", back_populates="shelter")

class Relationship(Base):
    __tablename__ = "relationships"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    description = Column(Text, unique=True)
    created_at = Column(DateTime)

class TenantRelationship(Base):
    __tablename__ = "tenant_relationships"
    id_tenant_relationship = Column(Integer, primary_key=True, autoincrement=True)
    id_tenant_1 = Column(Integer, ForeignKey("tenants.id"))
    id_tenant_2 = Column(Integer, ForeignKey("tenants.id"))
    id_relationship = Column(Integer, ForeignKey("relationships.id"))
    created_at = Column(DateTime)
