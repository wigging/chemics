"""
Tests for the transport disengaging height module.
"""

import chemics as cm
from pytest import approx


def test_tdh_chan():
    tdh = cm.tdh_chan(0.3)
    assert tdh == approx(1.7587, rel=1e-2)
