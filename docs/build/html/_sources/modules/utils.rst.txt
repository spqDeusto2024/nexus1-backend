Utils Module
============

The `utils` module provides utility functions and constants used throughout the application. It includes hashing utilities for securely managing sensitive data and other shared variables.

Files in the `utils` module:
----------------------------

- `hashing.py`: Contains utilities for hashing and verifying sensitive data, such as passwords.
- `vars.py`: Defines shared variables and constants used across the application.

Description:
------------
This module centralizes reusable logic and shared variables, improving the maintainability and consistency of the application. The `hashing.py` file handles sensitive operations, while the `vars.py` file stores commonly used constants.

==========================
Hashing Utilities
==========================

.. automodule:: app.utils.hashing
   :members:
   :undoc-members:
   :show-inheritance:

The `hashing.py` file provides secure hashing utilities, such as generating hashed passwords and verifying them. It uses libraries like `bcrypt` for enhanced security.

==========================
Shared Variables
==========================

The `vars.py` file contains shared variables and constants used throughout the application. 

Since this file doesn't contain docstrings, it is not auto-documented by Sphinx.
