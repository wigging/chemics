"""
Tests for the util.py module
"""

import chemics as cm
from pytest import approx


def test_slm2lpm():
    """ convert from SLM to LPM """

    slm = 580   # standard liter per minute, SLM or SLPM
    pgas = 150  # absolute pressure of gas, kPa
    tgas = 773  # temperature of gas, Kelvin

    # liter per minute, LPM
    lpm = cm.slm2lpm(slm, pgas, tgas)

    assert lpm == approx(1108.74, rel=1e-2)
