"""
Tests for gas thermal conductivity method.
"""

import chemics as cm
from pytest import approx, raises


def test_k_n2():
    gas = cm.Gas('N2')
    k = gas.thermal_conductivity(773)
    assert k == approx(0.0535, rel=1e-2)


def test_k_o2():
    gas = cm.Gas('O2')
    k = gas.thermal_conductivity(773)
    assert k == approx(0.0588, rel=1e-2)


def test_k_co_err():
    with raises(ValueError):
        gas = cm.Gas('CO')
        gas.thermal_conductivity(801)


def test_k_co():
    gas = cm.Gas('CO', cas='630-08-0')
    k = gas.thermal_conductivity(801)
    assert k == approx(0.05722, rel=1e-2)


def test_k_c18h38o():
    gas = cm.Gas('C18H38O', cas='593-32-8')
    k = gas.thermal_conductivity(920)
    assert k == approx(0.04174, rel=1e-2)
