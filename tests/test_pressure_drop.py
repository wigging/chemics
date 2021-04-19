"""
Tests for pressure drop module.
"""

import chemics as cm
from pytest import approx


# Parameters to use for pressure drop tests
# ----------------------------------------------------------------------------

mu = 5.60e-4        # fluid viscosity [Pa s]
epsilon = 0.335     # bed porosity [-]
u0 = 1.0e-3         # superficial velocity [m/s]
rhof = 804.6        # fluid density [kg/m^3]
dp = 5.0e-6         # particle diameter [m]


# Functions to test
# ----------------------------------------------------------------------------

def test_pressure_drop_ergun():
    # perssure drop per unit length [Pa/m]
    pressure_drop = cm.pressure_drop_ergun(mu, epsilon, u0, rhof, dp)
    assert pressure_drop == approx(3.9762253e7, rel=1e1)
