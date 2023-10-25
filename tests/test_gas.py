"""
Tests for the gas.py module.
"""

from pytest import approx, raises

import chemics as cm


def test_density():
    gas = cm.Gas('N2', 773, 150000)
    rho = gas.density()
    assert rho == approx(0.6538, rel=1e-4)


def test_heat_capacity1():
    gas = cm.Gas('CBrClF2', 700)
    cp = gas.heat_capacity()
    assert cp == approx(97.4982, rel=1e-4)


def test_heat_capacity2():
    gas = cm.Gas('C5H10O2', 850, cas_number='75-98-9')
    cp = gas.heat_capacity()
    assert cp == approx(268.4920, rel=1e-4)


def test_heat_capacity3():
    gas = cm.Gas('C5H10O2', 850, cas_number='75-98-9')
    cp = gas.heat_capacity()
    assert cp == approx(268.4920, rel=1e-4)


def test_heat_capacity4():
    gas = cm.Gas('NO2', 900)
    cp = gas.heat_capacity()
    assert cp == approx(51.0686, rel=1e-4)


def test_thermal_conductivity1():
    gas = cm.Gas('N2', 773, 110350)
    k = gas.thermal_conductivity()
    assert k == approx(0.053568, rel=1e-4)


def test_thermal_conductivity2():
    gas = cm.Gas('O2', 773)
    k = gas.thermal_conductivity()
    assert k == approx(0.058890, rel=1e-4)


def test_thermal_conductivity3():
    with raises(ValueError):
        gas = cm.Gas('CO', 801)
        gas.thermal_conductivity()


def test_thermal_conductivity4():
    gas = cm.Gas('CO', 801, cas_number='630-08-0')
    k = gas.thermal_conductivity()
    assert k == approx(0.05722, rel=1e-4)


def test_thermal_conductivity5():
    gas = cm.Gas('C18H38O', 920, cas_number='593-32-8')
    k = gas.thermal_conductivity()
    assert k == approx(0.04174, rel=1e-4)


def test_viscosity1():
    gas = cm.Gas('H2', 404)
    mu = gas.viscosity()
    assert mu == approx(113.18, rel=1e-2)


def test_viscosity2():
    gas = cm.Gas('CH4', 810)
    mu = gas.viscosity()
    assert mu == approx(234.21, rel=1e-2)


def test_viscosity3():
    gas = cm.Gas('NH3', 900, cas_number='7664-41-7')
    mu = gas.viscosity()
    assert mu == approx(319.14, rel=1e-2)


def test_viscosity4():
    gas = cm.Gas('C2Cl2F4', 900, cas_number='374-07-2')
    mu = gas.viscosity()
    assert mu == approx(314.90, rel=1e-2)


def test_viscosity5():
    with raises(ValueError):
        gas = cm.Gas('N2', 6010)
        _ = gas.viscosity()


def test_viscosity6():
    with raises(ValueError):
        gas = cm.Gas('NH3', 900)
        _ = gas.viscosity()


def test_viscosity7():
    with raises(ValueError):
        gas = cm.Gas('C2Cl2F4', 900)
        _ = gas.viscosity()


def test_viscosity8():
    gas = cm.Gas('NH3', 850)
    mu = gas.viscosity(method='ludwig')
    assert mu == approx(300.8464, rel=1e-2)


def test_viscosity9():
    gas = cm.Gas('C2H4O', 920, cas_number='75-07-0')
    mu = gas.viscosity('ludwig')
    assert mu == approx(242.4685, rel=1e-2)
