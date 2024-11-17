import sys
import os
from pathlib import Path
from unittest import mock


sys.path.insert(0, os.path.abspath('../..'))
print(sys.path)


#Avoided libs

autodoc_mock_imports = [
    'fastapi', 'pydantic', 'SQLAlchemy', 'pyjwt', 'passlib', 
    'python-multipart', 'pytest', 'httpx', 'coverage', 'requests','sqlalchemy'
]


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nexus1'
copyright = '2024, Manuel Garcés,Josu Igoa,Iker Perez,Carlos Gonzalez.'
author = 'Manuel Garcés,Josu Igoa,Iker Perez,Carlos Gonzalez.'
release = 'development'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
