def pressure_drop_ergun(mu, epsilon, u0, rhof, dp):
    """
    Calculate the pressure drop per unit length across a packed bed for all
    flow conditions (laminar to turbulent) using the Ergun equation.

    .. math:: -\\frac{\\Delta P}{L} = 150 \\frac{\\mu (1-\\varepsilon)^2 u_0 }{d_p^2 \\varepsilon^3} + 1.75 \\frac{\\rho_f (1-\\varepsilon) u_0^2 }{d_p \\varepsilon^3}

    Parameters
    ----------
    mu : float
        Viscosity of the fluid flowing through the packed bed [Pa s]
    epsilon : float
        Bed porosity [-]
    u0 : float
        Superficial velocity [m/s]
    rhof : float
        Density of the fluid flowing through the packed bed [kg/m^3]
    dp : float
        Particle diameter or equivalent particle diameter for non-spherical
        particles [m]

    Returns
    -------
    pressure_drop : float
        Pressure drop per unit length of bed [Pa/m]

    Example
    -------
    >>> pressure_drop_ergun(5.60e-4, 0.335, 1.0e-3, 804.6, 5.0e-6)
    39527821.4

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    pressure_drop = 150 * mu * (1 - epsilon)**2 * u0 / (dp**2 * epsilon**3) + \
        1.75 * rhof * (1 - epsilon) * u0**2 / (dp * epsilon**3)
    return pressure_drop
