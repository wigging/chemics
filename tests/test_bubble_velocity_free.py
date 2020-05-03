"""
Tests for bubble_velocity_free

Running through tests for each bubble regime
"""

from pytest import approx

import chemics as cm


# Parameters for test functions
# -----------------------------

# Using data for bubbles of air in water at 20 degC

rho_l = 998 # [kg/m^3]
rho_g = 0 # orders of magnitude smaller than rho_l
sig = 72.75 # [dynes/cm]
mu_l = 1.21 # [cP]


def test_ubrf1():
    """
    Region 1 test
    """
    ubf = cm.ubrf(0.00003, rho_l, rho_g, sig, mu_l)
    print(ubf)
    assert ubf == approx(0.0004046, rel=1e-2)


def test_ubrf2():
    """
    Region 2 test
    """
    ubf = cm.ubrf(0.0008, rho_l, rho_g, sig, mu_l)
    print(ubf)
    assert ubf == approx(0.1, rel=1e-2)


def test_ubrf3():
    """
    Region 3 test
    """
    ubf = cm.ubrf(0.003, rho_l, rho_g, sig, mu_l)
    print(ubf)
    assert ubf == approx(0.3, rel=1e-2)


def test_ubrf4():
    """
    Region 4 test
    """
    ubf = cm.ubrf(0.01, rho_l, rho_g, sig, mu_l)
    print(ubf)
    assert ubf == approx(0.22, rel=1e-2)


def test_ubrf5():
    """
    Region 5 test
    """
    ubf = cm.ubrf(0.1, rho_l, rho_g, sig, mu_l)
    print(ubf)
    assert ubf == approx(0.7, rel=1e-2)
