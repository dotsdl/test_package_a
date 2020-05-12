"""
Unit and regression test for the test_package_a package.
"""

# Import package, test suite, and other packages as needed
import test_package_a
import pytest
import sys

def test_test_package_a_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "test_package_a" in sys.modules
