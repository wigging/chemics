"""
Tests for ultimate bases module.
"""

import chemics as cm
from pytest import approx


def test_ultimate_bases():
    ult = cm.ultimate_bases(49.52, 5.28, 38.35, 0.15, 0.02, 0.64, 6.04)
    assert ult['ar'][0] == approx(49.52)
    assert ult['dry'][1] == approx(5.61, rel=1e-2)
    assert ult['daf'][3] == approx(0.16, rel=1e-2)
