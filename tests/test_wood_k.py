"""
Tests for the wood thermal conductivity function.
"""

import chemics as cm
from pytest import approx


def test_k_wood():
    k = cm.k_wood(0.54, 12.3, 10)
    assert k == approx(0.1567, rel=1e-2)
