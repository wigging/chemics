"""
Tests for the gas_thermal_conductivity module.
"""

import chemics as cm
from pytest import approx, raises


def test_k_n2():
    k_n2 = cm.k_gas_yaws('N2', 773)
    assert k_n2 == approx(0.0535, rel=1e-2)


def test_k_n2_disp(capsys):
    k = cm.k_gas_yaws('N2', 773, disp=True)
    assert k == approx(0.0535, rel=1e-2)

    captured = capsys.readouterr()
    assert captured.out == (
        'Formula        N2\n'
        'Name           nitrogen\n'
        'CAS            7727-37-9\n'
        'Min Temp. (K)  63.15\n'
        'Max Temp. (K)  1500.0\n'
        'A              -0.000226779433664\n'
        'B              0.0001027462918646\n'
        'C              -6.015141955845571e-08\n'
        'D              2.2331907127430105e-11\n'
        'k      (W/m⋅K) 0.05356876932986771\n'
    )


def test_k_o2():
    k_o2 = cm.k_gas_yaws('O2', 773)
    assert k_o2 == approx(0.0588, rel=1e-2)


def test_k_co_err():
    with raises(ValueError):
        _ = cm.k_gas_yaws('CO', 801)


def test_k_co():
    k_co = cm.k_gas_yaws('CO', 801, cas='630-08-0')
    assert k_co == approx(0.05722, rel=1e-2)


def test_k_c18h38o():
    k_c18h38o = cm.k_gas_yaws('C18H38O', 920, cas='593-32-8')
    assert k_c18h38o == approx(0.04174, rel=1e-2)
