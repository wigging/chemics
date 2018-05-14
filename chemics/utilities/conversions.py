"""
Conversions
"""

import numpy as np


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
        raise ValueError('No mass or mole fractions specified in calculation '
                         'of average molar mass')
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


def mole_to_mass(mw, mole_fracs):
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
    mass_fracs = (mole_fracs * mw) / mwa

    return mass_fracs


def mass_to_mole(mw, mass_fracs):
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
    to liters per minute (LPM). Assume STP defined as 273.25 K and 101,325 Pa.

    Conversion
    ----------
    1 LPM = 1 SLPM * (Tgas / 273.15 K) * (14.696 psi / Pgas)

    Reference
    ---------
    Wikipedia contributors. (2018, February 8). Standard litre per minute.
    In Wikipedia online. Retrieved from
    https://en.wikipedia.org/wiki/Standard_litre_per_minute

    Parameters
    ----------
    pgas = absolute gas pressure, kPa
    tgas = gas temperature, Kelvin

    Returns
    -------
    lpm = volumetric gas flow, liter/min
    """
    # equation requires gas pressure as psi so convert kPa to psi
    pgas_psi = pgas * 0.1450377
    lpm = slm * (tgas / 273.15) * (14.696 / pgas_psi)
    return lpm
