"""
Tests for the conversions module. Updated by G.W. on 5/25/19.
"""

import chemics as cm
from pytest import approx


def test_massfrac_to_molefrac():
    y = [0.36, 0.16, 0.20, 0.28]            # mass fraction [-]
    mw = [12.011, 1.008, 15.999, 14.007]    # molecular weight [g/mol]
    x = cm.massfrac_to_molefrac(y, mw)      # mole fraction [-]
    assert x[0] == approx(0.136, rel=1e-2)


def test_molefrac_to_massfrac():
    x = [0.36, 0.16, 0.20, 0.28]            # mole fraction [-]
    mw = [12.011, 1.008, 15.999, 14.007]    # molecular weight [g/mol]
    y = cm.molefrac_to_massfrac(x, mw)      # mass fraction [-]
    assert y[0] == approx(0.373, rel=1e-2)


def test_slm_to_lpm():
    slm = 580                           # standard liter per minute [SLM]
    p = 150                             # absolute pressure of gas [kPa]
    temp = 773                          # gas temperature [K]
    lpm = cm.slm_to_lpm(slm, p, temp)   # liter per minute [LPM]
    assert lpm == approx(1108.74, rel=1e-2)
