"""
Tests for proximate bases module.
"""

import chemics as cm
from pytest import approx


def test_proximate_bases():
    prox = cm.proximate_bases(16.92, 76.40, 0.64, 6.04)
    assert prox['ar'][0] == approx(16.92)
    assert prox['dry'][1] == approx(81.31, rel=1e-2)
    assert prox['daf'][1] == approx(81.86, rel=1e-2)
