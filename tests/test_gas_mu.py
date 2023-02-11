"""
Tests for gas viscosity methods and gas mixture viscosity functions.
"""

import chemics as cm
from pytest import approx, raises


def test_mu_yaws1():
    gas = cm.Gas('H2')
    mu = gas.mu_yaws(404)
    assert mu == approx(113.18, rel=1e-2)


def test_mu_yaws2():
    gas = cm.Gas('CH4')
    mu = gas.mu_yaws(810)
    assert mu == approx(234.21, rel=1e-2)


def test_mu_yaws3():
    gas = cm.Gas('NH3')
    mu = gas.mu_yaws(900, cas='7664-41-7')
    assert mu == approx(319.14, rel=1e-2)


def test_mu_yaws4():
    gas = cm.Gas('C2Cl2F4')
    mu = gas.mu_yaws(900, cas='374-07-2')
    assert mu == approx(314.90, rel=1e-2)


def test_mu_yaws5(capsys):
    gas = cm.Gas('N2')
    mu = gas.mu_yaws(773, disp=True)
    assert mu == approx(363.82, rel=1e-2)

    captured = capsys.readouterr()
    assert captured.out == (
        'Formula        N2\n'
        'Name           nitrogen\n'
        'CAS            7727-37-9\n'
        'Min Temp. (K)  63.15\n'
        'Max Temp. (K)  1970.0\n'
        'A              4.46555763078484\n'
        'B              0.638137789753159\n'
        'C              -0.0002659562785407\n'
        'D              5.41126875437814e-08\n'
        'μ (microPoise) 363.8235847080749\n'
    )


def test_mu_yaws6():
    with raises(ValueError):
        gas = cm.Gas('N2')
        _ = gas.mu_yaws(6010)


def test_mu_yaws7():
    with raises(ValueError):
        gas = cm.Gas('NH3')
        _ = gas.mu_yaws(900)


def test_mu_yaws8():
    with raises(ValueError):
        gas = cm.Gas('C2Cl2F4')
        _ = gas.mu_yaws(900)


def test_mu_ludwig1():
    gas = cm.Gas('NH3')
    mu = gas.mu_ludwig(850)
    assert mu == approx(300.8464, rel=1e-2)


def test_mu_ludwig2():
    gas = cm.Gas('C2H4O')
    mu = gas.mu_ludwig(920, cas='75-07-0')
    assert mu == approx(242.4685, rel=1e-2)


def test_mu_graham():
    gas1 = cm.Gas('H2')
    mu1 = gas1.mu_yaws(773.15)

    gas2 = cm.Gas('N2')
    mu2 = gas2.mu_yaws(773.15)

    mu_mix = cm.mu_graham([mu1, mu2], [0.85, 0.15])
    assert mu_mix == approx(207.37, rel=1e-2)


def test_mu_herning():
    gas1 = cm.Gas('H2')
    mw1 = gas1.mw
    mu1 = gas1.mu_yaws(773.15)

    gas2 = cm.Gas('N2')
    mw2 = gas2.mw
    mu2 = gas2.mu_yaws(773.15)

    mu_mix = cm.mu_herning([mu1, mu2], [mw1, mw2], [0.85, 0.15])
    assert mu_mix == approx(252.81, rel=1e-2)
