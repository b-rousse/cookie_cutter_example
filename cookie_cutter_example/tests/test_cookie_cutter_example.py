"""
Unit and regression test for the cookie_cutter_example package.
"""

# Import package, test suite, and other packages as needed
import cookie_cutter_example
import pytest
import sys

def test_cookie_cutter_example_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "cookie_cutter_example" in sys.modules
