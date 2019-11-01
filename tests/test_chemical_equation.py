"""
Tests for `chemical_equation` module.
"""

import chemics as cm
from pytest import approx


# Functions to test
# ----------------------------------------------------------------------------

def test_eq1():
    eq = '2 HCl + 2 Na -> 2 NaCl + H2'
    ce = cm.ChemicalEquation(eq)
    assert ce.names is None
    assert ce.balance is True
    assert ce.rct_properties['HCl']['moles'] == approx(2)
    assert ce.rct_properties['HCl']['species'] == 'HCl'
    assert ce.rct_properties['HCl']['molwt'] == approx(36.458)
    assert ce.rct_properties['HCl']['mass'] == approx(72.916)
    assert ce.rct_properties['HCl']['molfrac'] == approx(0.5)
    assert ce.rct_properties['HCl']['massfrac'] == approx(0.613275)
    assert ce.rct_elements == {'H': 2.0, 'Cl': 2.0, 'Na': 2.0}
    assert ce.rct_moles == approx(4)
    assert ce.rct_mass == approx(118.896)


def test_eq2():
    eq = '5 NaCl + 3 H2O -> CH4 + 2.2 CHAR + CH2OHCHO + GCO2'
    names = {'CHAR': 'C', 'GCO2': 'CO2'}
    ce = cm.ChemicalEquation(eq, names)
    assert ce.balance is False
    assert ce.prod_properties['GCO2']['moles'] == approx(1)
    assert ce.prod_properties['GCO2']['species'] == 'CO2'
    assert ce.prod_properties['GCO2']['molwt'] == approx(44.009)
    assert ce.prod_properties['GCO2']['mass'] == approx(44.009)
    assert ce.prod_properties['GCO2']['molfrac'] == approx(0.19230769)
    assert ce.prod_properties['GCO2']['massfrac'] == approx(0.300345)
    assert ce.prod_elements == {'C': 6.2, 'H': 8.0, 'O': 4.0}
    assert ce.prod_moles == approx(5.2)
    assert ce.prod_mass == approx(146.5282)
