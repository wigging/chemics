"""
Test for the Prandtl number module.
"""

import chemics as cm
from pytest import approx


def test_prandtl():
    cp = 4188
    mu = 0.001307
    k = 0.5674
    pr = cm.prandtl(cp, mu, k)
    assert pr == approx(9.64, rel=1e-2)
