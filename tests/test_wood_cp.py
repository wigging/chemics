"""
Tests for the wood heat capacity function.
"""

import chemics as cm
from pytest import approx


def test_wood_cp():
    cp = cm.cp_wood(12, 340)
    assert cp == approx(1.91, rel=1e-2)
