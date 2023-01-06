# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# region Django doc setup

import django
import os
import sys

sys.path.insert(0, os.path.abspath('./../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'kitchen.settings'

django.setup()

# endregion

project = 'kitchen'
copyright = '2022, nevermore'
author = 'nevermore'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.viewcode',  # 源码索引
    'sphinx.ext.autodoc',
    'autoapi.extension',  # 自动生成python的doc
    'sphinx.ext.napoleon'  # 适配GoogleStyle docstring
]

templates_path = ['_templates']
exclude_patterns = ['venv', '**/migrations']

language = 'zh_cn'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# region autoapi setting
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html

autoapi_type = 'python'
autoapi_dirs = ['../../kitchen', '../../services']
autoapi_options = [
    'members', 'undoc-members', 'private-members',
    'show-module-summary', 'special-members',
    'imported-members'
]

# endregion
