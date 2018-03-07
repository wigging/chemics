"""
Tests for the gas.py module
"""

import chemics as cm
from pytest import approx


def test_rhog():
    """ Calculate density of gas. """
    mw = 28         # molecular weight of N2 gas, g/mol
    Pgas = 150000   # absolule gas pressre, Pa
    Tgas = 773      # temperature of gas, Kelvin
    rho = cm.rhog(mw, Pgas, Tgas)
    assert rho == approx(0.65, rel=1e-2)
