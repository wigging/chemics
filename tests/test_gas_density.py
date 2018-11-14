"""
Tests for the gas_density module. Updated by G.W. on 11/14/2018.
"""

import chemics as cm
from pytest import approx

# Parameters for test functions
# ----------------------------------------------------------------------------

mw = 28         # molecular weight of N2 gas [g/mol]
p = 150_000     # absolule gas pressure [Pa]
tk = 773        # gas temperature [K]


# Functions to test
# ----------------------------------------------------------------------------

def test_rhog():
    # nitrogen gas density [kg/m^3]
    rho = cm.rhog(mw, p, tk)
    assert rho == approx(0.65, rel=1e-2)
