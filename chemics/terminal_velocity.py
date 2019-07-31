import numpy as np


def ut(cd, dp, rhog, rhos):
    """
    Calculate terminal velocity of a single particle based on Equation 28 on
    page 80 in the Kunii and Levenspiel book [1]_ where :math:`C_D` is an
    experimentally determined drag coefficient.

    .. math:: u_t = \\left( \\frac{4 d_p\\, (\\rho_s - \\rho_g) g}{3 \\rho_g\\, C_D} \\right)^{1/2}

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
    tm1 = 4 * dp * (rhos - rhog) * g
    tm2 = 3 * rhog * cd
    ut = (tm1 / tm2)**(1 / 2)
    return ut


def ut_ganser(dp, mu, phi, rhog, rhos):
    """
    Estimate terminal velocity of a non-spherical particle based on the Ganser
    drag coefficient [2]_. According to the Chhabra paper [3]_, the Ganser drag
    correlation is applicable for sphericity values from 0.09 to 1.

    .. math::

       C_d &= \\frac{24}{Re\\, K_1} \\left( 1 + 0.1118 (Re\\, K_1 K_2)^{0.6567} \\right) + \\frac{0.4305 K_2}{1 + \\frac{3305}{Re\\, K_1 K_2}}

       K_1 &= \\left( \\frac{1}{3} + \\frac{2}{3}\\phi \\right)

       K_2 &= 10^{1.8148 (-log\\, \\phi)^{0.5743}}

    where K₁ is Stokes' shape factor and K₂ is Newton's shape factor. The Cui 2007
    and Chhabra 1999 papers leave out the :math:`-2.25*d_v/D` term in the shape
    factor equations.

    Parameters
    ----------
    dp : float
        Diameter of the particle [m]
    mu : float
        Viscosity of gas [kg/(m s)]
    phi : float
        Sphericity of the particle [-]
    rhog : float
        Density of the gas [kg/m³]
    rhos : float
        Density of the particle [kg/m³]

    Returns
    -------
    ut : float
        Terminal velocity of non-spherical particle [m/s]

    Example
    -------
    >>> ut_ganser(0.00016, 1.8e-5, 0.67, 1.2, 2600)
    0.6230

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
    g = 9.81    # acceleration from gravity [m/s²]

    # Guess a range for Ut [m/s] to perform calculations
    # max terminal velocity in range determined from Newton's law
    ut_newton = 1.74 * np.sqrt(9.81 * dp * (rhos - rhog) / rhog)
    ut = np.arange(0.0001, ut_newton, 0.004)

    # Shape factors
    # papers Cui 2007 and Chhabra 1999 leave out the -2.25*dv/D term
    k1 = (1 / 3 + 2 / 3 * (phi**-0.5))**(-1)           # Stokes' shape factor
    k2 = 10**(1.8148 * ((-np.log(phi))**0.5743))       # Newton's shape factor

    # Evaluate Ganser drag coefficient [-] for a range of Ut
    # re and cd are vectors
    re = (dp * rhog * ut) / mu
    cd = (24 / (re * k1)) * (1 + 0.1118 * ((re * k1 * k2)**0.6567)) \
        + (0.4305 * k2) / (1 + (3305 / (re * k1 * k2)))

    # Evaluate sphere drag coefficient [-] for a range of Ut
    # this expression is from the Levenspiel book
    # cdd is a vector
    cdd = (4 * g * dp * (rhos - rhog)) / (3 * (ut**2) * rhog)

    # Interpolate value for Ut where Cd-Cdd = 0
    ut_interp = np.interp(0, cd - cdd, ut)

    return ut_interp


def ut_haider(dp, mu, phi, rhog, rhos):
    """
    Calculate terminal velocity of a particle as discussed in the Haider and
    Levenspiel [5]_. Valid for particle sphericities of 0.5 to 1. Particle
    diameter should be an equivalent spherical diameter, such as the diameter
    of a sphere having same volume as the particle.

    To determine the terminal velocity for a range of particle sphericities, Haider
    and Levenspiel first define two dimensionless quantities

    .. math::

       d_{*} = d_p \\left[ \\frac{g\\, \\rho_g (\\rho_s - \\rho_g)}{\\mu^2} \\right]^{1/3} \\
       u_* = \\left[ \\frac{18}{d{_*}^2} + \\frac{2.3348 - 1.7439\\, \\phi}{d{_*}^{0.5}} \\right]^{-1}

    where :math:`0.5 \\leq \\phi \\leq 1` and particle diameter :math:`d_p` is an
    equivalent spherical diameter, the diameter of a sphere having the same volume
    as the particle. The relationship between :math:`u_*` and :math:`u_t` is given
    by

    .. math:: u_* = u_t \\left[ \\frac{\\rho{_g}^2}{g\\, \\mu\\, (\\rho_s - \\rho_g)} \\right]^{1/3}

    The terminal velocity of the particle can finally be determined by rearranging
    the above equation such that

    .. math:: u_t = u_* \\left[ \\frac{g\\, \\mu\\, (\\rho_s - \\rho_g)}{\\rho{_g}^2} \\right]^{1/3}

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
        Terminal velocity of a particle [m/s]

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

    d_star = dp * ((9.81 * rhog * (rhos - rhog)) / (mu**2))**(1 / 3)
    u_star = (18 / (d_star**2) + ((2.3348 - 1.7439 * phi) / (d_star**0.5)))**-1
    ut = u_star * ((9.81 * (rhos - rhog) * mu) / rhog**2)**(1 / 3)
    return ut
