"""
Tests for proximate analysis class object.
"""

import chemics as cm
from pytest import approx


def test_proximate_analysis():
    prox = cm.Proximate([47.26, 40.05, 4.46, 8.23], 'ad')
    assert prox.ar_basis == approx([39.52, 33.49, 3.73, 23.24], rel=1e-2)
