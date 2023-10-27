"""
Tests for the molecular_weight module. Updated by G.W. on 11/30/2018.
"""

import chemics as cm
from pytest import approx


# Functions to test
# ----------------------------------------------------------------------------

def test_carbon():
    mw = cm.molecular_weight('C')
    assert mw == 12.011


def test_methane():
    mw = cm.molecular_weight('CH4')
    assert mw == approx(16.04, rel=1e-2)


def test_ammonium_sulfate():
    mw = cm.molecular_weight('(NH4)2SO4')
    assert mw == approx(132.13, rel=1e-2)
