"""
Tests for gas heat capacity method.
"""

import chemics as cm
from pytest import approx


def test_gas_cp1():
    gas = cm.Gas('CBrClF2')
    cp = gas.cp_yaws(700)
    assert cp == approx(97.4982, rel=1e-2)


def test_gas_cp2():
    gas = cm.Gas('C5H10O2')
    cp = gas.cp_yaws(850, cas='75-98-9')
    assert cp == approx(268.4920, rel=1e-2)


def test_gas_cp3():
    gas = cm.Gas('NO2')
    cp = gas.cp_yaws(900)
    assert cp == approx(51.0686, rel=1e-2)
