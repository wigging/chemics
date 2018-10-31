"""
Tests for the conversions module. Updated by G.W. on 10/31/2018.
"""

import chemics as cm
from pytest import approx

# Parameters for test functions
# ----------------------------------------------------------------------------

slm = 580       # standard liter per minute [SLM]
p = 150         # absolute pressure of gas [kPa]
temp = 773      # gas temperature [K]


# Functions to test
# ----------------------------------------------------------------------------

def test_slm_to_lpm():
    # liter per minute [LPM]
    lpm = cm.slm_to_lpm(slm, p, temp)
    assert lpm == approx(1108.74, rel=1e-2)
