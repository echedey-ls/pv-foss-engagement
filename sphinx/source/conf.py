# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pv-foss-engagment'
copyright = '2022, Kevin Anderson'
author = 'Kevin Anderson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []

nbsphinx_execute = 'always'
nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_title = ''
