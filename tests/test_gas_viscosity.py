"""
Tests for gas viscosity and gas mixture viscosity.
"""

import chemics as cm
from pytest import approx, raises


def test_mu_yaws1():
    gas = cm.Gas('H2')
    mu = gas.viscosity(404, method='yaws')
    assert mu == approx(113.18, rel=1e-2)


def test_mu_yaws2():
    gas = cm.Gas('CH4')
    mu = gas.viscosity(810, method='yaws')
    assert mu == approx(234.21, rel=1e-2)


def test_mu_yaws3():
    gas = cm.Gas('NH3')
    mu = gas.viscosity(900, method='yaws', cas='7664-41-7')
    assert mu == approx(319.14, rel=1e-2)


def test_mu_yaws4():
    gas = cm.Gas('C2Cl2F4')
    mu = gas.viscosity(900, method='yaws', cas='374-07-2')
    assert mu == approx(314.90, rel=1e-2)


def test_mu_yaws6():
    with raises(ValueError):
        gas = cm.Gas('N2')
        _ = gas.viscosity(6010, method='yaws')


def test_mu_yaws7():
    with raises(ValueError):
        gas = cm.Gas('NH3')
        _ = gas.viscosity(900, method='yaws')


def test_mu_yaws8():
    with raises(ValueError):
        gas = cm.Gas('C2Cl2F4')
        _ = gas.viscosity(900, method='yaws')


def test_mu_ludwig1():
    gas = cm.Gas('NH3')
    mu = gas.viscosity(850, method='ludwig')
    assert mu == approx(300.8464, rel=1e-2)


def test_mu_ludwig2():
    gas = cm.Gas('C2H4O')
    mu = gas.viscosity(920, method='ludwig', cas='75-07-0')
    assert mu == approx(242.4685, rel=1e-2)


def test_mu_graham():
    gas1 = cm.Gas('H2')
    mu1 = gas1.viscosity(773.15, method='yaws')

    gas2 = cm.Gas('N2')
    mu2 = gas2.viscosity(773.15, method='yaws')

    mu_mix = cm.mu_graham([mu1, mu2], [0.85, 0.15])
    assert mu_mix == approx(207.37, rel=1e-2)


def test_mu_herning():
    gas1 = cm.Gas('H2')
    mw1 = gas1.mw
    mu1 = gas1.viscosity(773.15, method='yaws')

    gas2 = cm.Gas('N2')
    mw2 = gas2.mw
    mu2 = gas2.viscosity(773.15, method='yaws')

    mu_mix = cm.mu_herning([mu1, mu2], [mw1, mw2], [0.85, 0.15])
    assert mu_mix == approx(252.81, rel=1e-2)
