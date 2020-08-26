
def biot(h, d, k):
    """
    Calculate the dimensionless Biot number.

    .. math:: Bi = \\frac{h\\, d}{k}

    Parameters
    ----------
    h : float
        Convective heat transfer coefficient [W/(m²⋅K)]
    d : float
        Characteristic length or dimension [m]
    k : float
        Thermal conductivity [W/(m⋅K)]

    Returns
    -------
    bi : float
        Biot number [-]

    Example
    -------
    >>> biot(4.63, 0.001, 3.84)
    0.0012057

    References
    ----------
    Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
    Butterworth-Heinemann, 2nd edition, 1991.
    """
    bi = (h * d) / k
    return bi


def prandtl(cp=None, mu=None, k=None, nu=None, alpha=None):
    """
    Calculate the dimensionless Prandtl number for a fluid or gas.

    .. math:: Pr = \\frac{c_p \\mu}{k} = \\frac{\\nu}{\\alpha}

    Parameters
    ----------
    cp : float
        Specific heat [J/(kg⋅K)]
    mu : float
        Dynamic viscosity [kg/(m⋅s)]
    k : float
        Thermal conductivity [W/(m⋅K)]
    nu : float, optional
        Kinematic viscosity [m²/s]
    alpha : float, optional
        Thermal diffusivity [m²/s]

    Returns
    -------
    pr : float
        Prandtl number [-]

    Examples
    --------
    >>> prandtl(cp=4188, mu=0.001307, k=0.5674)
    9.647

    >>> prandtl(nu=1.5064e-5, alpha=2.1002e-5)
    0.71726

    Raises
    ------
    ValueError
        Must provide (cp, mu, k) or (nu, alpha)

    References
    ----------
    Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
    Butterworth-Heinemann, 2nd edition, 1991.
    """
    if cp and mu and k:
        pr = (cp * mu) / k
    elif nu and alpha:
        pr = nu / alpha
    else:
        raise ValueError('Must provide (cp, mu, k) or (nu, alpha)')

    return pr


def pyroI(k, kr, rho, cp, r):
    """
    Calculate the pyrolysis number Py I for a biomass particle.

    .. math:: Py^I = \\frac{k}{\\rho\\,C_p\\,R^2\\,K}

    Parameters
    ----------
    k : float
        Thermal conductivity of the biomass particle [W/mK]
    kr : float
        Rate constant [1/s]
    rho : float
        Density of the biomass particle [kg/m³]
    cp : float
        Heat capacity of the biomass particle [J/kgK]
    r : float
        Radius or characteristic length of the biomass particle [m]

    Returns
    -------
    pyI : float
        Pyrolysis number Py I [-]

    Example
    -------
    >>> pyroI(k=0.12, kr=1.38556, rho=540, cp=3092.871049, r=0.0001847)
    1.5198

    References
    ----------
    D.L. Pyle and C.A. Zaror. Heat Transfer and Kinetics in the Low
    Temperature Pyrolysis of Solids. Chemical Engineering Science, vol. 39,
    no. 1, pg. 147-158, 1984.
    """
    pyI = k / (kr * rho * cp * (r**2))
    return pyI


def pyroII(h, kr, rho, cp, r):
    """
    Calculate the pyrolysis number Py II for a biomass particle.

    .. math:: Py^{II} = \\frac{h}{\\rho\\,C_p\\,R\\,K}

    Parameters
    ----------
    h : float
        Convective heat transfer coefficient [W/m²K]
    kr : float
        Rate constant [1/s]
    rho : float
        Density of the biomass particle [kg/m³]
    cp : float
        Heat capacity of the biomass particle [J/kgK]
    r : float
        Radius or characteristic length of the biomass particle [m]

    Returns
    -------
    pyII : float
        Pyrolysis number Py II [-]

    Example
    -------
    >>> pyroII(h=862.6129, kr=1.38556, rho=540, cp=3092.871049, r=0.0001847)
    2.018038

    References
    ----------
    D.L. Pyle and C.A. Zaror. Heat Transfer and Kinetics in the Low
    Temperature Pyrolysis of Solids. Chemical Engineering Science, vol. 39,
    no. 1, pg. 147-158, 1984.
    """
    pyII = h / (kr * rho * cp * r)
    return pyII


def reynolds(u, d, rho=None, mu=None, nu=None):
    """
    Calculate the dimensionless Reynolds number for a fluid or gas flow.

    .. math:: Re = \\frac{\\rho\\, u\\, d}{\\mu} = \\frac{u\\, d}{\\nu}

    Parameters
    ----------
    u : float
        Flow speed [m/s]
    d : float
        Characteristic length or dimension [m]
    rho : float, optional
        Density of the fluid or gas [kg/m³]
    mu : float, optional
        Dynamic viscosity of the fluid or gas [kg/(m⋅s)]
    nu : float, optional
        Kinematic viscosity of the fluid or gas [m²/s]

    Returns
    -------
    re : float
        Reynolds number [-]

    Examples
    --------
    >>> reynolds(2.6, 0.025, rho=910, mu=0.38)
    155.65789

    >>> reynolds(0.25, 0.102, nu=1.4e-6)
    18214.2857

    Raises
    ------
    ValueError
        Must provide (u, d, rho, mu) or (u, d, nu)

    References
    ----------
    Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
    Butterworth-Heinemann, 2nd edition, 1991.
    """
    if rho and mu and not nu:
        re = (rho * u * d) / mu
    elif nu and not rho and not mu:
        re = (u * d) / nu
    else:
        raise ValueError('Must provide (u, d, rho, mu) or (u, d, nu)')

    return re
