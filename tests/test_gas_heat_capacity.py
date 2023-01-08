"""
Tests for the gas_heat_capacity module.
"""

import chemics as cm
from pytest import approx


def test_cp1():
    cp1 = cm.cp_yaws('CBrClF2', 700)
    assert cp1 == approx(97.4982, rel=1e-2)


def test_cp2():
    cp2 = cm.cp_yaws('C5H10O2', 850, cas='75-98-9')
    assert cp2 == approx(268.4920, rel=1e-2)


def test_cp3():
    cp3 = cm.cp_yaws('NO2', 900)
    assert cp3 == approx(51.0686, rel=1e-2)
