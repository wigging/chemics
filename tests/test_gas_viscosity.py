"""
Tests for the gas_viscosity module grouped by functions for inorganic and
organic compounds. Updated by G.W. on 11/12/2018.

mu = Gas viscosity [micropoise]
cas = CAS number [-]
tmin = Minimum temperature applicable to equation [K]
tmax = Maximum temperature applicable to equation [K]
a, b, c, d = Regression coefficients [-]
"""

import chemics as cm
from pytest import approx


# Functions to test inorganic compounds
# ----------------------------------------------------------------------------

def test_mu_h2():
    mu_h2 = cm.mu_gas_inorganic('H2', 404)
    assert mu_h2 == approx(113.18, rel=1e-2)


def test_mu_n2():
    mu_n2 = cm.mu_gas_inorganic('N2', 773)
    assert mu_n2 == approx(363.82, rel=1e-2)


def test_mu_n2_full():
    mu_n2, *stats = cm.mu_gas_inorganic('N2', 773, full=True)
    cas, tmin, tmax, a, b, c, d = stats
    assert mu_n2 == approx(363.82, rel=1e-2)
    assert cas == '7727-37-9'
    assert tmin == approx(63.15, rel=1e-2)
    assert tmax == approx(1970.0, rel=1e-2)
    assert a == approx(4.465557, rel=1e-2)
    assert b == approx(0.63813778, rel=1e-2)
    assert c == approx(-0.0002659562, rel=1e-2)
    assert d == approx(5.411268e-08, rel=1e-2)


# Functions to test organic compounds
# ----------------------------------------------------------------------------

def test_mu_ch4():
    mu_ch4 = cm.mu_gas_organic('CH4', 810)
    assert mu_ch4 == approx(234.21, rel=1e-2)


def test_mu_c2cl2f4():
    mu_c2cl2f4 = cm.mu_gas_organic('C2Cl2F4', 900, cas='374-07-2')
    assert mu_c2cl2f4 == approx(314.90, rel=1e-2)
