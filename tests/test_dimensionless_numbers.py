"""
Tests for the dimensionless numbers module.
"""

import chemics as cm
from pytest import approx


def test_archimedes():
    ar = cm.archimedes(0.001, 910, 2500, 0.001307)
    assert ar == approx(8309.1452, rel=1e-2)


def test_biot():
    bi = cm.biot(4.63, 0.001, 3.84)
    assert bi == approx(0.0012057, rel=1e-2)


def test_peclet():
    pe = cm.peclet(3.0e-3, 0.25, 4.7e-4)
    assert pe == approx(1.5957, rel=1e-2)


def test_prandtl_args1():
    pr = cm.prandtl(cp=4188, mu=0.001307, k=0.5674)
    assert pr == approx(9.647, rel=1e-2)


def test_prandtl_args2():
    pr = cm.prandtl(nu=1.5064e-5, alpha=2.1002e-5)
    assert pr == approx(0.71726, rel=1e-2)


def test_pyroI():
    pyI = cm.pyroI(k=0.12, kr=1.38556, rho=540, cp=3092.871049, r=0.0001847)
    assert pyI == approx(1.5198, rel=1e-2)


def test_pyroII():
    pyII = cm.pyroII(h=862.6129, kr=1.38556, rho=540, cp=3092.871049, r=0.0001847)
    assert pyII == approx(2.018038, rel=1e-2)


def test_reynolds_args1():
    re = cm.reynolds(2.6, 0.025, rho=910, mu=0.38)
    assert re == approx(155.65789, rel=1e-2)


def test_reynolds_args2():
    re = cm.reynolds(0.25, 0.102, nu=1.4e-6)
    assert re == approx(18214.2857, rel=1e-2)


def test_schmidt():
    sc = cm.schmidt(8.90e-4, 997.07, 2.299e-9)
    assert sc == approx(388.26, rel=1e-2)


def test_sherwood():
    sh = cm.sherwood(2.3e-4, 5.0e-6, 4.0e-9)
    assert sh == approx(0.2875, rel=1e-2)


def test_flow_regime_args1():
    regime = cm.flow_regime(u=2.6, d=0.025, rho=910, mu=0.38)
    assert regime == "laminar"


def test_flow_regime_args2():
    regime = cm.flow_regime(Re=3250)
    assert regime == "transitional"


def test_flow_regime_args3():
    regime = cm.flow_regime(u=0.25, d=0.102, nu=1.4e-6)
    assert regime == "turbulent"
