from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# -----------------------------------------------
# TENANT: Model to represent a tenant
# -----------------------------------------------
class ParameterRoomBase(BaseModel):
    """
    Base model for a room parameter record.

    Attributes:
        id_room (int): Identifier of the room.
        id_parameter (int): Identifier of the parameter.
        date (datetime): Date of the parameter record.
        value (float): Value of the parameter recorded.
    """
    id_room: int
    id_parameter: int
    date: datetime
    value: float

class ParameterRoomCreate(ParameterRoomBase):
    """
    Model for creating a new room parameter record.

    Attributes:
        created_at (datetime): Timestamp indicating when the record was created.
    """
    created_at: datetime

class ParameterRoomUpdate(ParameterRoomBase):
    """
    Model for updating an existing room parameter record.

    Attributes:
        id (int): Unique identifier for the record, mandatory to ensure the correct record is updated.
    """
    id: int

class ParameterRoomDelete(BaseModel):
    """
    Model for deleting an existing room parameter record.

    Attributes:
        id (int): Unique identifier for the record, required to ensure the correct record is deleted.
    """
    id: int

class TenantBase(BaseModel):
    """
    Base model for a tenant.

    Attributes:
        id_role (int): Tenant's role id.
        id_dormitory(int): Tenant's dormitory id. 
        name (str): Tenant's first name.
        surname (str): Tenant's last name.
        age (Optional[str]): Tenant's age (optional).
        status (Optional[bool]): Tenant's status, whether active or not (optional).
        genre (Optional[str]): Tenant's genre (optional).
    """
    id_role: Optional[int]= None
    id_dormitory: Optional[int]= None
    name: str
    surname: str
    age: Optional[str] = None
    status: Optional[bool] = None
    genre: Optional[str] = None

class TenantCreate(TenantBase):
    """
    Model for creating a new tenant.

    Attributes:
        created_at (datetime): Date and time when the tenant was created.
    """
    created_at: datetime

class TenantUpdate(TenantBase):
    """
    Model for updating a tenant's information.

    Attributes:
        status (Optional[bool]): Tenant's status (optional).
        genre (Optional[str]): Tenant's genre (optional).
    """
    id : int
    status: Optional[bool] = None
    genre: Optional[str] = None

class TenantDelete(BaseModel):
    """
    Model for deleting a tenant.

    Attributes:
        id (int): ID of the tenant to be deleted.
    """
    id: int

# -----------------------------------------------
# ROLE: Model to represent a role
# -----------------------------------------------
class RoleBase(BaseModel):
    """
    Base model for a role.

    Attributes:
        name (str): Name of the role.
        description (Optional[str]): Description of the role (optional).
    """
    name: str
    description: Optional[str] = None
    id_room_relationship: Optional[int] = None

class RoleCreate(RoleBase):
    """
    Model for creating a new role.

    Attributes:
        created_at (datetime): Date and time when the role was created.
    """
    created_at: datetime

class RoleUpdate(RoleBase):
    """
    Model for updating a role.

    Attributes:
        description (Optional[str]): Description of the role (optional).
    """
    id : int
    description: Optional[str] = None

class RoleDelete(BaseModel):
    """
    Model for deleting a role.

    Attributes:
        id (int): ID of the role to be deleted.
    """
    id: int

# -----------------------------------------------
# ROOM: Model to represent a room
# -----------------------------------------------
class RoomBase(BaseModel):
    """
    Base model for a room.

    Attributes:
        name (str): Name of the room.
        description (Optional[str]): Description of the room (optional).
        capacity (Optional[int]): Maximum capacity of the room (optional).
        actual_tenant_number (Optional[int]): Current number of tenants in the room.
        availability (Optional[bool]): Availability of the room (optional).
    """
    id_shelter: int
    name: str
    description: Optional[str] = None
    capacity: Optional[int] = None
    actual_tenant_number: Optional[int] = None
    availability: Optional[bool] = None

class RoomCreate(RoomBase):
    """
    Model for creating a new room.

    Attributes:
        created_at (datetime): Date and time when the room was created.
    """
    created_at: datetime

class RoomUpdate(RoomBase):
    """
    Model for updating a room.

    Attributes:
        availability (Optional[bool]): Room's availability (optional).
        actual_tenant_number (Optional[int]): Current number of tenants in the room (optional).
    """
    id : int
    availability: Optional[bool] = None
    actual_tenant_number: Optional[int] = None

class RoomDelete(BaseModel):
    """
    Model for deleting a room.

    Attributes:
        id (int): ID of the room to be deleted.
    """
    id: int

# -----------------------------------------------
# DORMITORY: Model to represent a dormitory
# -----------------------------------------------
class DormitoryBase(BaseModel):
    """
    Base model for a dormitory.

    Attributes:
        name (str): Name of the dormitory.
        description (str): Description of the dormitory.
        capacity (Optional[int]): Maximum capacity of the dormitory (optional).
        actual_tenant_number (Optional[int]): Current number of tenants in the dormitory (optional).
        availability (Optional[bool]): Availability of the dormitory (optional).
    """
    id_shelter: int
    name: str
    description: str
    capacity: Optional[int] = None
    actual_tenant_number: Optional[int] = None
    availability: Optional[bool] = None

class DormitoryCreate(DormitoryBase):
    """
    Model for creating a new dormitory.

    Attributes:
        created_at (datetime): Date and time when the dormitory was created.
    """
    created_at: datetime

class DormitoryUpdate(DormitoryBase):
    """
    Model for updating a dormitory.

    Attributes:
        availability (Optional[bool]): Dormitory's availability (optional).
        actual_tenant_number (Optional[int]): Current number of tenants in the dormitory (optional).
    """
    id : int
    availability: Optional[bool] = None
    actual_tenant_number: Optional[int] = None

class DormitoryDelete(BaseModel):
    """
    Model for deleting a dormitory.

    Attributes:
        id (int): ID of the dormitory to be deleted.
    """
    id: int

# -----------------------------------------------
# ADMINISTRATOR: Model to represent an administrator
# -----------------------------------------------
class AdministratorBase(BaseModel):
    """
    Base model for an administrator.

    Attributes:
        username (str): Administrator's username.
        password (str): Administrator's password.
    """
    username: str
    password: str

class AdministratorCreate(AdministratorBase):
    """
    Model for creating a new administrator.

    Attributes:
        created_at (datetime): Date and time when the administrator was created.
    """
    created_at: datetime

class AdministratorUpdate(AdministratorBase):
    """
    Model for updating an administrator's details.

    Attributes:
        password (Optional[str]): Administrator's password (optional).
    """
    id : int
    password: Optional[str] = None

class AdministratorDelete(BaseModel):
    """
    Model for deleting an administrator.

    Attributes:
        id (int): ID of the administrator to be deleted.
    """
    id: int

# -----------------------------------------------
# PARAMETER: Model to represent a parameter
# -----------------------------------------------
class ParameterBase(BaseModel):
    """
    Base model for a parameter.

    Attributes:
        name (str): Name of the parameter.
        description (str): Description of the parameter.
    """
    name: str
    description: str

class ParameterCreate(ParameterBase):
    """
    Model for creating a new parameter.

    Attributes:
        created_at (datetime): Date and time when the parameter was created.
    """
    created_at: datetime

class ParameterUpdate(ParameterBase):
    """
    Model for updating a parameter.

    Attributes:
        description (Optional[str]): Description of the parameter (optional).
    """
    id : int
    description: Optional[str] = None

class ParameterDelete(BaseModel):
    """
    Model for deleting a parameter.

    Attributes:
        id (int): ID of the parameter to be deleted.
    """
    id: int

# -----------------------------------------------
# SHELTER: Model to represent a shelter
# -----------------------------------------------
class ShelterBase(BaseModel):
    """
    Base model for a shelter.

    Attributes:
        name (str): Name of the shelter.
        description (str): Description of the shelter.
    """
    name: str
    description: str

class ShelterCreate(ShelterBase):
    """
    Model for creating a new shelter.

    Attributes:
        created_at (datetime): Date and time when the shelter was created.
    """
    created_at: datetime

class ShelterUpdate(ShelterBase):
    """
    Model for updating a shelter.

    Attributes:
        description (Optional[str]): Description of the shelter (optional).
    """
    id: int
    description: Optional[str] = None

class ShelterDelete(BaseModel):
    """
    Model for deleting a shelter.

    Attributes:
        id (int): ID of the shelter to be deleted.
    """
    id: int

# -----------------------------------------------
# RELATIONSHIP TYPES: Model to represent a relationship type
# -----------------------------------------------
class RelationshipBase(BaseModel):
    """
    Base model for a relationship type.

    Attributes:
        name (str): Name of the relationship.
        description (str): Description of the relationship.
    """
    id : int
    name: str
    description: str

class RelationshipCreate(RelationshipBase):
    """
    Model for creating a new relationship type.

    Attributes:
        created_at (datetime): Date and time when the relationship type was created.
    """
    created_at: datetime

class RelationshipUpdate(RelationshipBase):
    """
    Model for updating a relationship type.

    Attributes:
        description (Optional[str]): Description of the relationship type (optional).
    """
    id : int
    description: Optional[str] = None

class RelationshipDelete(BaseModel):
    """
    Model for deleting a relationship type.

    Attributes:
        id (int): ID of the relationship type to be deleted.
    """
    id: int

# -----------------------------------------------
# TENANT RELATIONSHIP: Model to represent the relationship between tenants
# -----------------------------------------------
class TenantRelationshipBase(BaseModel):
    """
    Base model for the relationship between two tenants.

    Attributes:
        id_tenant_1 (int): ID of the first tenant.
        id_tenant_2 (int): ID of the second tenant.
        id_relationship (int): ID of the relationship type between the two tenants.
    """
    id_tenant_1: int
    id_tenant_2: int
    id_relationship: int

class TenantRelationshipCreate(TenantRelationshipBase):
    """
    Model for creating a new tenant relationship.

    Attributes:
        created_at (datetime):  Date and time when the tenant relationship type was created.
    """
    created_at: datetime

class TenantRelationshipUpdate(TenantRelationshipBase):
    """
    Model for updating an existing tenant relationship.

    Attributes:
        id_relationship (Optional[int]): Optional attribute to update the relationship type between the two tenants.
    """
    id_tenant_relationship: int
    id_relationship: Optional[int] = None


class TenantRelationshipDelete(BaseModel):
    """
    Model for deleting a specific tenant relationship.

    Attributes:
        id_tenant_relationship (int): The ID of the tenant relationship to be deleted.
    """
    id_tenant_relationship: int

# -----------------------------------------------
# LOGIN: Model to encapsulate needed data on a login authentication process
# -----------------------------------------------
class LoginCredentials(BaseModel):
    username: str
    password: str
