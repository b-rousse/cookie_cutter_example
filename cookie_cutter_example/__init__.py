"""
cookie_cutter_example
A python package for the MolSSI Summer School, + intro to cookiecutters
"""

# Add imports here
from .molecule import *
from .measure import *
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
