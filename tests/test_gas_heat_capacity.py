"""
Tests for gas heat capacity method.
"""

import chemics as cm
from pytest import approx


def test_gas_heat_capacity1():
    gas = cm.Gas('CBrClF2')
    cp = gas.heat_capacity(700)
    assert cp == approx(97.4982, rel=1e-2)


def test_gas_heat_capacity2():
    gas = cm.Gas('C5H10O2', '75-98-9')
    cp = gas.heat_capacity(850)
    assert cp == approx(268.4920, rel=1e-2)


def test_gas_heat_capacity3():
    gas = cm.Gas('C5H10O2', cas='75-98-9')
    cp = gas.heat_capacity(850)
    assert cp == approx(268.4920, rel=1e-2)


def test_gas_heat_capacity4():
    gas = cm.Gas('NO2')
    cp = gas.heat_capacity(900)
    assert cp == approx(51.0686, rel=1e-2)
