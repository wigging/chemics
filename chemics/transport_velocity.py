def utr(dp, mu, rhog, rhos):
    """
    Determine the transport velocity of particles in a circulating fluidized
    bed riser. Based on Equation 2 in article by Zhang et al. [1]_.

    Parameters
    ----------
    dp : float
        Diameter of particle [m]
    mu : float
        Viscosity of gas [kg/(m s)]
    rhog : float
        Density of gas [kg/m^3]
    rhos : float
        Density of solid particle [kg/m^3]

    Returns
    -------
    utr : float
        Transport velocity [m/s]

    Example
    -------
    >>> utr(0.0005, 3.6e-5, 0.44, 1630)
    26.0617

    References
    ----------
    .. [1] H.L. Zhang, J. Degreve, R. Dewil, and J. Baeyens. Operation diagram
        of Circulating Fluidized Beds (CFBs). Procedia Engineering, 102,
        pp. 1092-1103, 2015.
    """
    g = 9.81                                                # gravity acceleraton [m/s^2]
    ar = ((dp**3) * rhog * (rhos - rhog) * g) / (mu**2)     # Archimedes number [-]
    utr = (mu / (dp * rhog)) * (3.23 + 0.23 * ar)           # transport velocity [m/s]
    return utr
