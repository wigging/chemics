"""
Tests for biomass composition module.
"""

from chemics import biocomp
from pytest import approx


# Functions to test
# ----------------------------------------------------------------------------

def test_biocomp():
    yc = 0.534  # mass fraction for carbon
    yh = 0.06   # mass fraction for hydrogen

    bc = biocomp(yc, yh)
    assert bc['y_daf'][0] == approx(0.2936, rel=1e-2)
    assert bc['y_daf'][1] == approx(0.1594, rel=1e-2)
    assert bc['y_daf'][2] == approx(0.0712, rel=1e-2)
    assert bc['y_daf'][3] == approx(0.2934, rel=1e-2)
    assert bc['y_daf'][4] == approx(0.1822, rel=1e-2)
    assert bc['y_daf'][5] == approx(0.0)
    assert bc['y_daf'][6] == approx(0.0)


def test_biocomp2():
    yc = 0.500      # mass fraction of carbon
    yh = 0.060      # mass fraction of hydrogen
    yo = 0.440      # mass fraction of oxygen
    yash = 0.15     # mass fraction of ash

    bc = biocomp(yc, yh, yo, yash=yash)
    assert bc['x_daf'][0] == approx(0.5016, rel=1e-2)
    assert bc['x_daf'][1] == approx(0.3344, rel=1e-2)
    assert bc['x_daf'][2] == approx(0.0328, rel=1e-2)
    assert bc['x_daf'][3] == approx(0.0614, rel=1e-2)
    assert bc['x_daf'][4] == approx(0.0698, rel=1e-2)
    assert bc['x_daf'][5] == approx(0.0)
    assert bc['x_daf'][6] == approx(0.0)
