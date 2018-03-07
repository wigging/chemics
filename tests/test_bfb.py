"""
Tests for bfb.py module
"""

import chemics as cm
from pytest import approx


def test_fbexp():
    """ fluidized bed expansion factor """

    db = 0.05232    # bed diameter, m
    dp = 0.0004     # diameter of bed particle, m
    rhog = 0.4413   # density of gas, kg/m^3
    rhop = 2500     # density of bed particle, kg/m^3
    umf = 0.1157    # minimum fluidization velocity, m/s
    us = 3.0 * umf  # superficial gas velocity, m/s

    # bed expansion factor, fbexp (-)
    fbexp = cm.fbexp(db, dp, rhog, rhop, umf, us)

    assert fbexp == approx(1.48, rel=1e-2)
