"""
Test for gas density method.
"""

import chemics as cm
from pytest import approx


def test_gas_rho():
    p = 150_000  # absolule gas pressure [Pa]
    tk = 773     # gas temperature [K]

    gas = cm.Gas('N2')
    rho = gas.rho(p, tk)
    assert rho == approx(0.65, rel=1e-2)
