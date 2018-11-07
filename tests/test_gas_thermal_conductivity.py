"""
Tests for the gas_thermal_conductivity module grouped by functions for
inorganic and organic compounds. Updated by G.W. on 11/07/2018.

k = Gas thermal conductivity [W/(m K)]
cas = CAS number [-]
tmin = Minimum temperature applicable to equation [K]
tmax = Maximum temperature applicable to equation [K]
a, b, c, d = Regression coefficients [-]
"""

import chemics as cm
from pytest import approx


# Functions to test inorganic compounds
# ----------------------------------------------------------------------------

def test_k_n2():
    k_n2 = cm.k_gas_inorganic('N2', 773)
    assert k_n2 == approx(0.0535, rel=1e-2)


def test_k_n2_full():
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
    k_o2 = cm.k_gas_inorganic('O2', 773)
    assert k_o2 == approx(0.0588, rel=1e-2)


# Functions to test inorganic compounds
# ----------------------------------------------------------------------------

def test_k_co():
    k_co = cm.k_gas_organic('CO', 801)
    assert k_co == approx(0.05722, rel=1e-2)


def test_k_c18h38o():
    k_c18h38o = cm.k_gas_organic('C18H38O', 920, cas='593-32-8')
    assert k_c18h38o == approx(0.04174, rel=1e-2)
