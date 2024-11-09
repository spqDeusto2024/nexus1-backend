from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.mysql.base import Base  # Asumimos que tienes una clase base de SQLAlchemy

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_role = Column(Integer, ForeignKey("roles.id"), nullable=True)
    id_dormitory = Column(Integer, ForeignKey("dormitories.id"), nullable=True)
    name = Column(String(255), unique=True, nullable=False)
    surname = Column(String(255), unique=True, nullable=False)
    age = Column(String(50), nullable=True)
    status = Column(Boolean, nullable=True)
    genre = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False)

    role = relationship("Role", back_populates="tenants")
    dormitory = relationship("Dormitory", back_populates="tenants")


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=True)
    id_room_relationship = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    created_at = Column(DateTime, nullable=False)

    tenants = relationship("Tenant", back_populates="role")
    room_relationship = relationship("Room", back_populates="roles")


class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_shelter = Column(Integer, ForeignKey("shelters.id"), nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    capacity = Column(Integer, nullable=True)
    actual_tenant_number = Column(Integer, nullable=True)
    availability = Column(Boolean, nullable=True)
    created_at = Column(DateTime, nullable=False)

    shelter = relationship("Shelter", back_populates="rooms")
    roles = relationship("Role", back_populates="room_relationship")
    parameters = relationship("ParameterRoom", back_populates="room")


class Dormitory(Base):
    __tablename__ = "dormitories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_shelter = Column(Integer, ForeignKey("shelters.id"), nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    capacity = Column(Integer, nullable=True)
    actual_tenant_number = Column(Integer, nullable=True)
    availability = Column(Boolean, nullable=True)
    created_at = Column(DateTime, nullable=False)

    shelter = relationship("Shelter", back_populates="dormitories")
    tenants = relationship("Tenant", back_populates="dormitory")


class Administrator(Base):
    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)


class ParameterRoom(Base):
    __tablename__ = "parameter_rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_room = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    id_parameter = Column(Integer, ForeignKey("parameters.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

    room = relationship("Room", back_populates="parameters")
    parameter = relationship("Parameter", back_populates="parameter_rooms")


class Parameter(Base):
    __tablename__ = "parameters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)

    parameter_rooms = relationship("ParameterRoom", back_populates="parameter")


class Shelter(Base):
    __tablename__ = "shelters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)

    rooms = relationship("Room", back_populates="shelter")
    dormitories = relationship("Dormitory", back_populates="shelter")


class Relationship(Base):
    __tablename__ = "relationships"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)


class TenantRelationship(Base):
    __tablename__ = "tenant_relationships"
    id_tenant_relationship = Column(Integer, primary_key=True, autoincrement=True)
    id_tenant_1 = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    id_tenant_2 = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    id_relationship = Column(Integer, ForeignKey("relationships.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)
