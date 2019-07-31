"""
Tests for terminal velocity module.
"""

import chemics as cm
from pytest import approx


# Parameters to use for terminal velocity tests
# ----------------------------------------------------------------------------

cd = 11.6867    # drag coefficient [-]
dp = 0.00016    # particle diameter [m]
mu = 1.8e-5     # gas viscosity [kg/(m s)]
phi = 0.67      # particle sphericity [-]
rhog = 1.2      # gas density [kg/m^3]
rhos = 2600     # particle density [kg/m^3]


# Functions to test
# ----------------------------------------------------------------------------

def test_ut():
    # terminal velocity [m/s]
    ut = cm.ut(cd, dp, rhog, rhos)
    assert ut == approx(0.6227, rel=1e-2)


def test_ut_haider():
    # terminal velocity [m/s]
    ut_haider = cm.ut_haider(dp, mu, phi, rhog, rhos)
    assert ut_haider == approx(0.8857, rel=1e-2)


def test_ut_ganser():
    # terminal velocity [m/s]
    ut_ganser = cm.ut_ganser(dp, mu, phi, rhog, rhos)
    assert ut_ganser == approx(0.6230, rel=1e-2)
