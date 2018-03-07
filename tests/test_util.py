"""
Tests for the util.py module
"""

import chemics as cm
from pytest import approx


def test_slm_to_lpm():
    """ Conversion of SLM to LPM. """
    slm = 580   # standard liter per minute, SLM or SLPM
    Pgas = 150  # absolute pressure of gas, kPa
    Tgas = 773  # temperature of gas, Kelvin
    lpm = cm.slm_to_lpm(slm, Pgas, Tgas)
    assert lpm == approx(1029.208)
