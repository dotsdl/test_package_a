"""
test_package_a
The first of two pages to test implicit namespaces
"""

# Add imports here
import pkg_resources

from .test_package_a import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

for entry_point in pkg_resources.iter_entry_points(
    "test_org.test_package_a.plugins"
):

    entry_point.load()
    print(entry_point, dir(entry_point))
