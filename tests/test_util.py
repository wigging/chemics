"""
Tests for the util.py module
"""

# add parent directory to python path
import sys
sys.path.append('.')

import chemics as cm
from pytest import approx


def test_slm_to_lpm():
    """ Conversion of SLM to LPM. """
    slm = 580   # standard liter per minute, SLM or SLPM
    Pgas = 150  # absolute pressure of gas, kPa
    Tgas = 773  # temperature of gas, Kelvin
    lpm = cm.slm_to_lpm(slm, Pgas, Tgas)
    assert lpm == approx(1029.208)


def test_rhog():
    """ Calculate density of gas. """
    mw = 28         # molecular weight of N2 gas, g/mol
    Pgas = 150000   # absolule gas pressre, Pa
    Tgas = 773      # temperature of gas, Kelvin
    rhog = cm.rhog(mw, Pgas, Tgas)
    assert rhog == approx(0.653521)

