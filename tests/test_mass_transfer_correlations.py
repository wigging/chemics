"""
Tests for the mass_transfer_correlations module.
"""

import chemics as cm
import pytest


def test_molecular_diffusion_coeff():
    Dm = cm.molecular_diffusion_coeff(32.04, 298.2, 0.386, 173.0, phi=1.9)
    assert Dm == pytest.approx(3.708e-5, rel=1e-3)


def test_convective_mt_coeff():
    kf = cm.convective_mt_coeff(4.79e-10, 5e-6, 0.335, 7.21e-3, 1452.0)
    assert kf == pytest.approx(6.77e-4, rel=1e-3)


def test_convective_mt_coeff_range():
    # tests for Exception if Re is out of range
    with pytest.raises(ValueError):
        cm.convective_mt_coeff(4.79e-10, 5e-6, 0.335, 7.21e-5, 1452.0)


def test_axial_dispersion_coeff():
    Dax = cm.axial_dispersion_coeff(4.7e-9, 5.0e-6, 3.0e-3)
    assert Dax == pytest.approx(1.0931e-8, rel=1e-10)


def test_axial_dispersion_coeff_sc():
    Dax = cm.axial_dispersion_coeff_sc(4.7e-9, 0.4, 1100.0, 135.0)
    assert Dax == pytest.approx(0.06835, rel=1e-4)


def test_axial_dispersion_coeff_sc_range():
    # tests for Exception if epsilon*Re*Sc or Sc are out of range
    with pytest.raises(ValueError):
        cm.axial_dispersion_coeff_sc(4.7e-9, 0.4, 1100.0, 1135.0)
