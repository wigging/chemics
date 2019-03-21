"""
Tests for the devol_time module. Updated by G.W. on 3/20/2019.
"""

import chemics as cm
from pytest import approx

# Parameters for test function
# ----------------------------------------------------------------------------

dp = 2.0        # diameter of wood particle [mm]
tbed = 773.15   # temperatue of the fluidized bed [K]


# Functions to test
# ----------------------------------------------------------------------------

def test_devol_time():
    # devol. time for 95% conversion [s]
    dtime = cm.devol_time(dp, tbed)
    assert dtime == approx(13.2114, rel=1e-2)
