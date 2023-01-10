"""
Tests for the liquid_heat_capacity module.
"""

import chemics as cm
from pytest import approx


def test_cp1():
    cp1 = cm.cp_liq_yaws('CBrF3', 250)
    assert cp1 == approx(107.2774, rel=1e-2)


def test_cp2():
    cp2 = cm.cp_liq_yaws('C38H76', 400, cas='61828-17-9')
    assert cp2 == approx(1307.0624, rel=1e-2)
