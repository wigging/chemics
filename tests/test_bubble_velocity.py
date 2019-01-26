"""
Tests for bubble velocity module.
"""

import chemics as cm
from pytest import approx


# Parameters for test functions
# ----------------------------------------------------------------------------

db = 0.05   # effective bubble diameter [m]
dt = 0.6    # fluidized bed diameter [m]


# Functions to test
# ----------------------------------------------------------------------------

def test_ubr():
    # here
    ubr = cm.ubr(db, dt)
    assert ubr == approx(0.4979, rel=1e-2)
