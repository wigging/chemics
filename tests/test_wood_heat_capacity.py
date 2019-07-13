"""
Tests for the wood heat capacity module.
"""

import chemics as cm
from pytest import approx


def test_cp_wood():
    cp = cm.cp_wood(12, 340)
    assert cp == approx(1.91, rel=1e-2)
