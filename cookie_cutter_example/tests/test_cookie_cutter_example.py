"""
Unit and regression test for the cookie_cutter_example package.
"""

# Import package, test suite, and other packages as needed
import cookie_cutter_example
import pytest
import sys
import numpy as np

def test_cookie_cutter_example_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "cookie_cutter_example" in sys.modules

def test_calculate_distance():
    '''test the calculate_distance function'''

    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])

    expected_distance = np.sqrt(2.)

    calculated_distance = cookie_cutter_example.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance


def test_calculate_angle():
    '''test the calculate_angle function'''

    r1 = np.array([0,0,0])
    r2 = np.array([1,0,0])
    r3 = np.array([2,0,0])
    
    calculated_angle = cookie_cutter_example.calculate_angle(r1, r2, r3)# % (2*np.pi)

    expected_angle = np.pi

    assert expected_angle == calculated_angle
