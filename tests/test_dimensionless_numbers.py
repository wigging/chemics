"""
Tests for the dimensionless numbers module.
"""

import chemics as cm
from pytest import approx


def test_prandtl_args1():
    pr = cm.prandtl(cp=4188, mu=0.001307, k=0.5674)
    assert pr == approx(9.647, rel=1e-2)


def test_prandtl_args2():
    pr = cm.prandtl(nu=1.5064e-5, alpha=2.1002e-5)
    assert pr == approx(0.71726, rel=1e-2)


def test_reynolds_args1():
    re = cm.reynolds(2.6, 0.025, rho=910, mu=0.38)
    assert re == approx(155.65789, rel=1e-2)


def test_reynolds_args2():
    re = cm.reynolds(0.25, 0.102, nu=1.4e-6)
    assert re == approx(18214.2857, rel=1e-2)
