"""
Utilities
=========

See doc string and comments in each function for more details.

Functions
---------
archimedes
mw_avg
rho_avg
dpSauter
mole2mass
mass2mole
slm_to_lpm
rhog
"""

import numpy as np


def archimedes(dp, rhog, rhos, mug):
    """
    Archimedes number as a dimensionless constant.

    Parameters
    ----------
    dp = diameter of particle, m
    rhos = density of solid particle, kg/m^3
    rhog = density of gas, kg/m^3
    mug = viscosity of gas, kg/(m s)

    Returns
    -------
    Ar = Archimedes number, (-)
    """
    g = 9.81    # gravitational constant, m/s^2
    Ar = ((dp**3)*rhog*(rhos-rhog)*g)/(mug**2)
    return Ar


def mw_avg(mw, mole_fracs=None, mass_fracs=None):
    """
    This function calculates the average molar mass of a mixture.

    Parameters
    ----------
    mw = a list/array of molar masses in the mixture (g/mol)
    mole_fracs = a list/array of mole fractions
    mass_fracs = a list/array of mass fractions

    NOTE: Either the set of mole or the set of mass fractions should be
    specified. If both are specified, mole fractions are used.

    Returns
    mwa = the average mixture molar mass (g/mol)
    """

    if mole_fracs is not None:
        mwa = np.dot(mw, mole_fracs)
    elif mass_fracs is not None:
        mwa = 1./np.sum(np.divide(mass_fracs, mw))
    else:
        raise ValueError(
            'No mass or mole fractions specified in calculation of average molar mass')

    return mwa


def rho_avg(rho, mass_fracs):
    """
    Calculates the mixture mass density assuming additive volumes and an ideal
    solution.

    Parameters
    ----------
    rho = array of species mass densities (kg/m^3)
    mass_fracs = array of species mass fractions (kg/kg)

    Returns
    -------
    rhoa = average density (kg/m^3)
    """

    rhoa = 1./np.sum(np.divide(mass_fracs, rho))
    return rhoa


def dpSauter(dp, mass_fracs):
    """
    This function calculates the Sauter mean diameter of a particle size
    distribution.

    Parameters
    ----------
    dp = an array of particle diameters (m)
    mass_fracs = an array of the mass fractions for each particle size

    Returns
    -------
    dp_bar = the Sauter mean diameter (m)
    """

    dp_bar = 1./np.sum(np.divide(mass_fracs, dp))
    return dp_bar


def mole2mass(mw, mole_fracs):
    """
    This function converts mole fractions to mass fractions.

    Parameters
    ----------
    mw = list/array of molar masses (g/mol)
    mole_fracs = list/array of mole fractions

    Returns
    -------
    mass_fracs = list of mass fractions
    """

    # Calculate the average molar mass
    mwa = mw_avg(mw, mole_fracs=mole_fracs)

    # Calculate the mass fractions
    mass_fracs = np.dot(mole_fracs, mw) / mwa

    return mass_fracs


def mass2mole(mw, mass_fracs):
    """
    This function converts mass fractions to mole fractions.

    Parameters
    ----------
    mw = list/array of molar masses (g/mol)
    mass_fracs = list/array of mass fractions

    Returns
    -------
    mole_fracs = list of mole fractions
    """

    # Calculate the average molar mass
    mwa = mw_avg(mw, mass_fracs=mass_fracs)

    # Calculate the mole fractions
    mole_fracs = np.divide(mass_fracs, mw) * mwa

    return mole_fracs


def slm_to_lpm(slm, pgas, tgas):
    """
    Convert volumetric gas flow from standard liters per minute (SLM or SLPM)
    to liters per minute (LPM).

    Parameters
    ----------
    pgas : scalar
        Absolute gas pressure in kPa
    tgas : scalar
        Gas temperature in Kelvin

    Returns
    -------
    lpm : scalar
        Volumetric gas flow in liter per minutre or liter/min
    """
    # equation assumes pgas in psi so convert kPa to psi
    pgas = pgas * 0.1450377
    lpm = slm * (tgas / 294.26) * (14.696 / pgas)
    return lpm


def rhog(mw, pgas, tgas):
    """
    Calculate gas density from molecular weight, pressure, and temperature.

    Parameters
    ----------
    mw : scalar
        Molecular weight in g/mol
    pgas : scalar
        Absolute gas pressure in Pa
    tgas : scalar
        Gas temperature in Kelvin

    Returns
    -------
    rhog : scalar
        Gas density in kg/m^3
    """
    # R is ideal gas constant in (m^3 Pa)/(mol K)
    # convert mw in g/mol to kg/mol
    R = 8.314
    mw = mw / 1000
    rhog = (mw * pgas) / (R * tgas)
    return rhog

