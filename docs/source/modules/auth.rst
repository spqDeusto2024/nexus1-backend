Authentication Module
=====================

The `auth` module handles the authentication and authorization logic in the application, including managing JWT tokens and dependencies related to authentication.

Files in the `auth` module:
---------------------------

- `dependencies.py`: Contains dependencies used for authentication, such as JWT-related functions.
- `jwt_handler.py`: Handles the creation and validation of JWT tokens.

Description:
------------
This module is essential for securing access to the application by ensuring that users are authenticated and authorized before accessing protected resources.

==========================
Dependencies File
==========================

.. automodule:: app.auth.dependencies
    :members:
    :undoc-members:
    :show-inheritance:

=======================
JWT File
=======================

.. automodule:: app.auth.jwt_handler
    :members:
    :undoc-members:
    :show-inheritance:
