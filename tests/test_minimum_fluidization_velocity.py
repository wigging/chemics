import chemics as cm
from pytest import approx


# Parameters to use for minimum fluidization velocity tests
# ----------------------------------------------------------------------------

dp = 0.0005     # diameter of bed particle [m]
ep = 0.46       # void fraction [-]
mu = 3.6e-5     # dynamic viscosity of gas [kg/ms]
phi = 0.86      # sphericity [-]
rhog = 0.44     # density of gas [kg/m³]
rhos = 2500     # density of bed particle [kg/m³]


# Functions to test
# ----------------------------------------------------------------------------

def test_umf_wenyu():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_coeff(dp, mu, rhog, rhos)
    assert umf == approx(0.1021, rel=1e-2)


def test_umf_rich():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_coeff(dp, mu, rhog, rhos, 'rich')
    assert umf == approx(0.1192, rel=1e-2)


def test_umf_sax():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_coeff(dp, mu, rhog, rhos, 'sax')
    assert umf == approx(0.1879, rel=1e-2)


def test_umf_babu():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_coeff(dp, mu, rhog, rhos, 'babu')
    assert umf == approx(0.2136, rel=1e-2)


def test_umf_grace():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_coeff(dp, mu, rhog, rhos, 'grace')
    assert umf == approx(0.1259, rel=1e-2)


def test_umf_chit():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_coeff(dp, mu, rhog, rhos, 'chit')
    assert umf == approx(0.1443, rel=1e-2)


def test_umf_ergun():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_ergun(dp, ep, mu, phi, rhog, rhos)
    assert umf == approx(0.1488, rel=1e-2)


def test_umf_small_re():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_reynolds(dp, ep, mu, phi, 19, rhog, rhos)
    assert umf == approx(0.1513, rel=1e-2)


def test_umf_large_re():
    # minimum fluidization velocity [m/s]
    umf = cm.umf_reynolds(dp, ep, mu, phi, 1001, rhog, rhos)
    assert umf == approx(1.1545, rel=1e-2)
