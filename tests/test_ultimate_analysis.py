"""
Tests for ultimate analysis class object.
"""

import chemics as cm
from pytest import approx


def test_ultimate_bases():
    ult = cm.Ultimate([60.08, 5.44, 25.01, 0.88, 0.73, 7.86, 9.00], 'ad')
    assert ult.ar_basis == approx([46.86, 6.70, 39.04, 0.68, 0.56, 6.13, 29.02], rel=1e-1)
