"""
Tests for the gas_mixture.py module.
"""

import chemics as cm
from pytest import approx


def test_viscosity1():
    gas1 = cm.Gas('H2', 773)
    gas2 = cm.Gas('N2', 773)
    gas_mixture = cm.GasMixture([gas1, gas2], [0.85, 0.15])
    mu_mix = gas_mixture.viscosity()
    assert mu_mix == approx(207.37, rel=1e-2)


def test_viscosity2():
    gas1 = cm.Gas('H2', 773)
    gas2 = cm.Gas('N2', 773)
    gas_mixture = cm.GasMixture([gas1, gas2], [0.85, 0.15])
    mu_mix = gas_mixture.viscosity(method='herning')
    assert mu_mix == approx(252.81, rel=1e-2)


def test_molecular_weight1():
    gas1 = cm.Gas('H2', 773)
    gas2 = cm.Gas('N2', 773)
    gas_mixture = cm.GasMixture([gas1, gas2], [0.8, 0.2])
    mw_mixture = gas_mixture.molecular_weight()
    assert mw_mixture == approx(7.2156, rel=1e-2)


def test_molecular_weight2():
    gas1 = cm.Gas('H2', 773)
    gas2 = cm.Gas('N2', 773)
    gas3 = cm.Gas('CH4', 773)
    gas_mixture = cm.GasMixture([gas1, gas2, gas3], [0.4, 0.1, 0.5])
    mw_mixture = gas_mixture.molecular_weight()
    assert mw_mixture == approx(11.6293, rel=1e-2)
