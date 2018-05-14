"""
Terminal velocity
"""

import numpy as np


def ut(cd, dp, rhog, rhos):
    """
    Terminal velocity of a single particle.

    Parameters
    ----------
    cd = drag coefficient, (-)
    dp = diameter of particle, m
    rhog = density of gas, kg/m^3
    rhos = density of solid, kg/m^3

    Return
    ------
    Ut = terminal velocity, m/s
    """
    g = 9.81  # gravity acceleration, m/s^2
    tm1 = 4*dp*(rhos - rhog)*g
    tm2 = 3*dp*cd
    Ut = (tm1/tm2)**(1/2)
    return Ut


def ut_ganser(dp, mug, rhog, rhos, sp):
    """
    Uses Ganser correlation to estimate terminal velocity of a specified
    particle in a gas with specified properties. According to the Chhabra 1999
    paper, the Ganser 1993 Cd correlation is applicable for sphericity values
    from 0.09 to 1. Cd drag coefficient from Ganser 1993 Eq. 18, Cd also
    referenced in Cui 2007 Eq. 2, and in Chhabra 1999 Eq. 6.

    Parameters
    ----------
    dp = particle diameter, m
    mug = gas viscosity, kg/(m s)
    rhog = gas density, kg/m^3
    rhos = solid particle density, kg/m^3
    sp = sphericity, -

    Returns
    -------
    Cd = particle terminal drag coefficient, (-)
    Re = particle terminal Reynolds number, (-)
    ut = particle terminal velocity, m/s

    References
    ----------
    Ganser, 1993. A rational approach to drag prediction of spherical and
    nonsperical particles. Powder Technology, 77, 143-152.

    Cui, Grace, 2007. Fluidization of biomass particles: A review of
    experimental multiphase flow aspects. Chemical Engineering Science, 62,
    45-55.

    Chhabra, Agarwal, Sinha, 1999. Drag on non-spherical particles: An
    evaluation of available methods. Powder Technology, 101, 288-295.
    """
    g = 9.81    # acceleration from gravity, m/s^2

    # shape factors
    # papers Cui 2007 and Chhabra 1999 leave out the -2.25*dv/D term
    K1 = (1/3 + 2/3*(sp**-0.5))**(-1)           # Stokes' shape factor
    K2 = 10**(1.8148*((-np.log(sp))**0.5743))   # Newton's shape factor

    # guess a range for terminal velocity, m/s
    ut = np.arange(0.001, 20, 0.001)

    # evaluate drag coefficients for range of ut
    # Re is Reynolds number, (-)
    # Cd is Ganser 1993 drag coefficient as function of Re, K1, K2 (-)
    # Cdd is drag coefficient as function of ut, etc. (-)
    Re = (dp*rhog*ut)/mug
    Cd = (24/(Re*K1))*(1 + 0.1118*((Re*K1*K2)**0.6567)) + (0.4305*K2)/(1+(3305/(Re*K1*K2)))
    Cdd = (4*g*dp*(rhos-rhog))/(3*(ut**2)*rhog)

    delta = np.abs(Cd-Cdd)  # compare difference between Cd and Cdd
    idx = np.argmin(delta)  # find index of minimum value in delta

    # select values to return based on above index
    return Cd[idx], Re[idx], ut[idx]


def uTerminal(dp, rhog, rhop, ug, phi):
    """
    Calculates the terminal velocity of a solid particle from K/L eqs.
    3.31-3.33.

    Parameters
    ----------
    dp : float
        Diameter of the particle [m]
    rhog : float
        Gas mass density [kg/m^3]
    rhop : float
        Particle mass density [kg/m^3]
    ug : float
        Gas dynamic viscosity [kg/m/s]
    phi : float
        Particle sphericity [-]

    Note
    ----
    This calculation is only valid if 0.5 < phi < 1

    Returns
    -------
    ut : float
        Terminal velocity of the particle [m/s]
    """

    # Constants
    g = 9.81    # m/s^2

    # Calculate the dimensionless particle diameter (the cube root of the
    # Archimedes number)
    Ar = (g* (dp**3) * rhog * (rhop - rhog)) / (ug**2)   # Ar = Archimedes number, (-)
    d_star = Ar**(1.0 / 3)  # K/L eq. 3.31

    # Calculate the dimensionless terminal velocity, K/L eq. 3.33
    ut_star_inv = 18.0 / (d_star**2) + (2.335 - 1.744 * phi) / sqrt(d_star)
    ut_star = 1.0 / ut_star_inv

    # Calculate the terminal velocity
    ut = ut_star * ((ug * (rhop - rhog) * g) / (rhog**2))**(1.0 / 3)

    return ut
