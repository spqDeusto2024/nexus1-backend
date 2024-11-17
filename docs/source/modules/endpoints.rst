Endpoints Module
=================

The `endpoints` module contains various API endpoint files. These endpoints are responsible for handling different HTTP requests, interacting with the database, and returning appropriate responses. Each file corresponds to a resource or group of resources in the application.

Files in the `endpoints` module:
---------------------------------

- `administrator.py`: Contains the API endpoints for administrator-related actions.
- `auth.py`: Handles authentication-related API endpoints, such as login and token management.
- `dormitory.py`: Contains endpoints related to dormitory management.
- `parameter.py`: Provides endpoints for managing parameters in the application.
- `parameterRoom.py`: Includes endpoints related to room parameters.
- `relationship.py`: Handles endpoints for managing relationships between entities.
- `role.py`: Contains role management-related endpoints.
- `room.py`: Includes endpoints for room management in the application.
- `shelter.py`: Provides endpoints for managing shelters.
- `tenant.py`: Handles endpoints for tenant management.
- `tenant_relationship.py`: Contains endpoints related to tenant relationships.

Description:
------------
Each of these files defines endpoints for specific resources or functionalities, helping to manage data and interact with clients through HTTP requests.

==========================
Administrator Endpoints
==========================

- **`administrator.py`**: Manages administrator-related API requests such as creating, updating, and deleting administrators.

==========================
Authentication Endpoints
==========================

- **`auth.py`**: Handles user authentication, including login and generating JWT tokens.

==========================
Dormitory Endpoints
==========================

- **`dormitory.py`**: Manages dormitory-related actions such as creating, listing, and modifying dormitory data.

==========================
Parameter Endpoints
==========================

- **`parameter.py`**: Provides endpoints to manage various application parameters.

==========================
Room Parameter Endpoints
==========================

- **`parameterRoom.py`**: Handles endpoints for room-specific parameters, like configuration and settings.

==========================
Relationship Endpoints
==========================

- **`relationship.py`**: Manages relationships between different entities in the system.

==========================
Role Endpoints
==========================

- **`role.py`**: Contains endpoints for role management, such as assigning roles and querying role data.

==========================
Room Management Endpoints
==========================

- **`room.py`**: Provides endpoints to create, modify, and view room data.

==========================
Shelter Endpoints
==========================

- **`shelter.py`**: Handles shelter management, including shelter creation and modification.

==========================
Tenant Endpoints
==========================

- **`tenant.py`**: Manages tenant data, including adding, updating, and removing tenants.

==========================
Tenant Relationship Endpoints
==========================

- **`tenant_relationship.py`**: Contains endpoints for managing relationships between tenants and other entities.
