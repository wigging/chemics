"""
Tests for the gas_viscosity module. Updated by G.W. on 12/31/2022.

mu = Gas viscosity [micropoise]
cas = CAS number [-]
tmin = Minimum temperature applicable to equation [K]
tmax = Maximum temperature applicable to equation [K]
a, b, c, d = Regression coefficients [-]
"""

import chemics as cm
from pytest import approx, raises


# Functions to test
# ----------------------------------------------------------------------------

def test_mu_ch4():
    mu = cm.mu_gas('CH4', 810)
    assert mu == approx(234.21, rel=1e-2)


def test_nh3_err():
    with raises(KeyError):
        _ = cm.mu_gas('NH3', 900)


def test_nh3():
    mu = cm.mu_gas('NH3', 900, cas='7664-41-7')
    assert mu == approx(319.14, rel=1e-2)


def test_err():
    with raises(ValueError):
        _ = cm.mu_gas('C2Cl2F4', 900)


def test_mu_c2cl2f4():
    mu = cm.mu_gas('C2Cl2F4', 900, cas='374-07-2')
    assert mu == approx(314.90, rel=1e-2)


def test_mu_h2():
    mu = cm.mu_gas('H2', 404)
    assert mu == approx(113.18, rel=1e-2)


def test_mu_n2():
    mu = cm.mu_gas('N2', 773)
    assert mu == approx(363.82, rel=1e-2)


def test_mu_n2_disp(capsys):
    mu = cm.mu_gas('N2', 773, disp=True)
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


def test_mu_graham():
    mu_h2 = cm.mu_gas('H2', 773.15)
    mu_n2 = cm.mu_gas('N2', 773.15)
    mu_mix = cm.mu_graham([mu_h2, mu_n2], [0.85, 0.15])
    assert mu_mix == approx(207.37, rel=1e-2)


def test_mix_b():
    mu_h2 = cm.mu_gas('H2', 773.15)
    mu_n2 = cm.mu_gas('N2', 773.15)
    mw_h2 = cm.mw('H2')
    mw_n2 = cm.mw('N2')
    mu_mix = cm.mu_herning([mu_h2, mu_n2], [mw_h2, mw_n2], [0.85, 0.15])
    assert mu_mix == approx(252.81, rel=1e-2)
