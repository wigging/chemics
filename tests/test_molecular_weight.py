"""
Tests for the molecular_weight module. Updated by G.W. on 11/30/2018.
"""

import chemics as cm
from pytest import approx


# Functions to test
# ----------------------------------------------------------------------------

def test_carbon():
    mw = cm.mw('C')
    assert mw == 12.011


def test_methane():
    mw = cm.mw('CH4')
    assert mw == approx(16.04, rel=1e-2)


def test_ammonium_sulfate():
    mw = cm.mw('(NH4)2SO4')
    assert mw == approx(132.13, rel=1e-2)


def test_mix_a():
    mw_h2 = cm.mw('H2')
    mw_n2 = cm.mw('N2')
    mw = cm.mw_mix([mw_h2, mw_n2], [0.8, 0.2])
    assert mw == approx(7.2156, rel=1e-2)


def test_mix_b():
    mw_h2 = cm.mw('H2')
    mw_n2 = cm.mw('N2')
    mw_ch4 = cm.mw('CH4')
    mw = cm.mw_mix([mw_h2, mw_n2, mw_ch4], [0.4, 0.1, 0.5])
    assert mw == approx(11.6293, rel=1e-2)
