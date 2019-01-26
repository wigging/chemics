"""
Tests for transport velocity module.
"""

import chemics as cm
from pytest import approx


# Parameters to use for transport velocity tests
# ----------------------------------------------------------------------------

dp = 0.0005     # paricle diameter [m]
mu = 3.6e-5     # viscosity of nitrogen gas at 773 K and 1 atm [kg/(m s)]
rhog = 0.44     # density of nitrogen gas at 773 K and 1 atm [kg/m^3]
rhos = 1630     # particle density [kg/m^3]


# Functions to test
# ----------------------------------------------------------------------------

def test_utr():
    # transport velocity [m/s]
    ut = cm.utr(dp, mu, rhog, rhos)
    assert ut == approx(26.0617, rel=1e-2)
