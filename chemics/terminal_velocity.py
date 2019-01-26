import numpy as np


def ut(cd, dp, rhog, rhos):
    """
    Calculate terminal velocity of a single particle based on Equation 28 on
    page 80 in the Kunii and Levenspiel book [1]_.

    Parameters
    ----------
    cd : float
        Drag coefficient [-]
    dp : float
        Diameter of particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhos : float
        Density of solid [kg/m^3]

    Returns
    -------
    ut : float
        Terminal velocity [m/s]

    Example
    -------
    >>> ut(11.6867, 0.00016, 1.2, 2600)
    0.6227

    References
    ----------
    .. [1] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
           Butterworth-Heinemann, 2nd edition, 1991.
    """
    g = 9.81  # gravity acceleration, m/s^2
    tm1 = 4*dp*(rhos - rhog)*g
    tm2 = 3*rhog*cd
    ut = (tm1/tm2)**(1/2)
    return ut


def ut_ganser(dp, mu, phi, rhog, rhos):
    """
    Estimate terminal velocity of a particle based on the Ganser drag
    correlation [2]_. According to the Chhabra paper [3]_, the Ganser drag
    correlation is applicable for sphericity values from 0.09 to 1.

    Parameters
    ----------
    dp : float
        Diameter of the particle [m]
    mu : float
        Viscosity of gas [kg/(m s)]
    phi : float
        Sphericity of the particle [-]
    rhog : float
        Density of the gas [kg/m^3]
    rhos : float
        Density of the particle [kg/m^3]

    Returns
    -------
    cd : float
        Drag coefficient of the particle [-]
    re : float
        Reynolds number of the particle [-]
    ut : float
        Terminal velocity of particle [m/s]

    Example
    -------
    >>> cd, re, ut_ganser = ut_ganser(0.00016, 1.8e-5, 0.67, 1.2, 2600)
    11.6867, 6.6453, 0.6230

    Note
    ----
    Drag coefficient is referenced from Equation 18 in Ganser, Equation 6 in
    Chhabra, and as Equation 2 in Cui [4]_.

    References
    ----------
    .. [2] Gary H. Ganser. A rational approach to drag prediction of spherical
           and nonsperical particles. Powder Technology, 77, 143-152, 1993.
    .. [3] R.P. Chhabra, L. Agarwal, and N.K. Sinha. Drag on non-spherical
           particles: An evaluation of available methods. Powder Technology,
           101, 288-295, 1999.
    .. [4] Heping Cui and John R. Grace. Fluidization of biomass particles: A
           review of experimental multiphase flow aspects. Chemical Engineering
           Science, 62, 45-55, 2007.
    """
    g = 9.81    # acceleration from gravity, m/s^2

    # shape factors
    # papers Cui 2007 and Chhabra 1999 leave out the -2.25*dv/D term
    k1 = (1/3 + 2/3*(phi**-0.5))**(-1)           # Stokes' shape factor
    k2 = 10**(1.8148*((-np.log(phi))**0.5743))   # Newton's shape factor

    # guess a range for terminal velocity, m/s
    ut = np.arange(0.001, 20, 0.001)

    # evaluate drag coefficients for range of ut
    # Re is Reynolds number, (-)
    # Cd is Ganser 1993 drag coefficient as function of Re, K1, K2 (-)
    # Cdd is drag coefficient as function of ut, etc. (-)
    re = (dp*rhog*ut)/mu
    cd = (24/(re*k1))*(1 + 0.1118*((re*k1*k2)**0.6567)) \
        + (0.4305*k2)/(1+(3305/(re*k1*k2)))
    cdd = (4*g*dp*(rhos-rhog))/(3*(ut**2)*rhog)

    delta = np.abs(cd-cdd)  # compare difference between Cd and Cdd
    idx = np.argmin(delta)  # find index of minimum value in delta

    # select values to return based on above index
    return cd[idx], re[idx], ut[idx]


def ut_haider(dp, mu, phi, rhog, rhos):
    """
    Calculate terminal velocity of a particle as discussed in the Haider and
    Levenspiel [5]_. Valid for particle sphericities of 0.5 to 1. Particle
    diameter should be an equivalent spherical diameter, such as the diameter
    of a sphere having same volume as the particle.

    Parameters
    ----------
    dp : float
        Diameter of particle [m]
    mu : float
        Viscosity of gas [kg/(m s)]
    phi : float
        Sphericity of particle [-]
    rhog : float
        Density of gas [kg/m^3]
    rhos : float
        Density of particle [kg/m^3]

    Returns
    -------
    ut : float
        Terminal velocity of particle [m/s]

    Example
    -------
    >>> ut_haider(0.00016, 1.8e-5, 0.67, 1.2, 2600)
    0.8857

    References
    ----------
    .. [5] A. Haider and O. Levenspiel. Drag coefficient and terminal velocity
           of spherical and nonspherical particles. Powder Technology,
           58:63–70, 1989.
    """
    if phi > 1.0 or phi < 0.5:
        raise ValueError('Sphericity must be 0.5 <= phi <= 1.0')

    d_star = dp * ((9.81*rhog*(rhos-rhog))/(mu**2))**(1/3)
    u_star = (18/(d_star**2) + ((2.3348 - 1.7439*phi) / (d_star**0.5)))**-1
    ut = u_star * ((9.81*(rhos-rhog)*mu) / rhog**2)**(1/3)
    return ut
