"""
test_package_a
The first of two pages to test implicit namespaces
"""

# Add imports here
from .test_package_a import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
