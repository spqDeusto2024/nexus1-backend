MySQL Module
============

The `mysql` module is responsible for interacting with the MySQL database. It includes the configuration and models required for database operations, as well as helper functions for managing connections and queries.

Files in the `mysql` module:
----------------------------

- `base.py`: Contains base functionality for database interactions.
- `models.py`: Defines the MySQL database models.
- `mysql.py`: Contains helper functions for managing MySQL connections and queries.

Description:
------------
This module is essential for the application to interact with MySQL. It includes base functionalities, the data models for the database schema, and helper functions for performing database operations. The `models.py` file provides the structure of the data in the database, while the `mysql.py` file contains logic for managing connections and queries.

==========================
Base Functionality
==========================

The `base.py` file contains general helper functions for interacting with the MySQL database. It serves as a foundational component for other modules and files in the project that need to interact with MySQL.

Since this file doesn't contain docstrings, it is not auto-documented by Sphinx.

==========================
MySQL Models
==========================

.. automodule:: app.mysql.models
   :members:
   :undoc-members:
   :show-inheritance:

The `models.py` file defines the MySQL database models used by the application. These models represent the structure of tables in the MySQL database, and are used with an ORM to query and manipulate the database records. 

==========================
MySQL Helper Functions
==========================

.. automodule:: app.mysql.mysql
   :members:
   :undoc-members:
   :show-inheritance:

The `mysql.py` file provides helper functions for managing MySQL database connections, executing queries, and handling database transactions. These functions help streamline the process of interacting with MySQL in the application.

