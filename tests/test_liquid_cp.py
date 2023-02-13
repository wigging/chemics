"""
Tests for the liquid heat capacity method.
"""

import chemics as cm
from pytest import approx


def test_liquid_cp1():
    liquid = cm.Liquid('CBrF3')
    cp = liquid.cp_yaws(250)
    assert cp == approx(107.2774, rel=1e-2)


def test_liquid_cp2():
    liquid = cm.Liquid('C38H76')
    cp = liquid.cp_yaws(400, cas='61828-17-9')
    assert cp == approx(1307.0624, rel=1e-2)
