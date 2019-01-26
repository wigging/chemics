"""
Tests for bed expansion factor module.
"""

import chemics as cm
from pytest import approx


# Parameters for test functions
# ----------------------------------------------------------------------------

db = 0.05232    # bed diameter [m]
dp = 0.0004     # diameter of bed particle [m]
rhog = 0.4413   # density of gas [kg/m³]
rhos = 2500     # density of bed particle [kg/m³]

umf = 0.1157    # minimum fluidization velocity [m/s]
us = 3.0 * umf  # superficial gas velocity [m/s]


# Functions to test
# ----------------------------------------------------------------------------

def test_fbexp():
    # bed expansion factor [-]
    fbexp = cm.fbexp(db, dp, rhog, rhos, umf, us)
    assert fbexp == approx(1.4864, rel=1e-2)
