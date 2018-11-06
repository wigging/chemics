"""
Tests for the gas_thermal_conductivity module. Updated by G.W. on 11/06/2018.
"""

import chemics as cm
from pytest import approx

# Functions to test
# ----------------------------------------------------------------------------


def test_k_n2():
    # thermal conductivity of nitrogen gas [W/(m K)]
    k_n2 = cm.k_gas_inorganic('N2', 773)
    assert k_n2 == approx(0.0535, rel=1e-2)


def test_k_n2_full():
    # thermal conductivity of nitrogen gas [W/(m K)]
    # CAS number [-]
    # Temperature range at which results are applicable [K]
    # Values for regression coefficients [-]
    k_n2, *stats = cm.k_gas_inorganic('N2', 773, full=True)
    cas, tmin, tmax, a, b, c, d = stats
    assert k_n2 == approx(0.0535, rel=1e-2)
    assert cas == '7727-37-9'
    assert tmin == approx(63.15, rel=1e-2)
    assert tmax == approx(1500.0, rel=1e-2)
    assert a == approx(-0.00022677943366402798, rel=1e-2)
    assert b == approx(0.000102746291864698, rel=1e-2)
    assert c == approx(-6.015141955845571e-08, rel=1e-2)
    assert d == approx(2.2331907127430102e-11, rel=1e-2)


def test_k_o2():
    # thermal conductivity of oxygen gas [W/(m K)]
    k_o2 = cm.k_gas_inorganic('O2', 773)
    assert k_o2 == approx(0.0588, rel=1e-2)
