
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
    nu : float
        Kinematic viscosity [m²/s]
    alpha : float
        Thermal diffusivity [m²/s]

    Returns
    -------
    pr : float
        Prandtl number [-]

    Example
    -------
    >>> prandtl(cp=4188, mu=0.001307, k=0.5674)
    9.647

    >>> prandtl(nu=1.5064e-5, alpha=2.1002e-5)
    0.71726
    """
    if cp and mu and k:
        pr = (cp * mu) / k
    elif nu and alpha:
        pr = nu / alpha
    else:
        raise ValueError('Must provide cp, mu, and k or nu and alpha')

    return pr


def reynolds(u, d, rho=None, mu=None, nu=None):
    """
    Calculate the dimensionless Reynolds number for a fluid or gas flow.

    .. math:: Re = \\frac{\\rho u d}{\\mu} = \\frac{u d}{\\nu}

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
    >>> 1

    >>> 2

    References
    ----------
    """

    if rho and mu and not nu:
        re = (rho * u * d) / mu
    elif nu and not rho and not mu:
        re = (u * d) / nu
    elif rho and mu and nu:
        raise ValueError('Must provide density and viscosity or dynamic viscosity. Not all three.')
    else:
        raise ValueError('Either density and viscosity, or dynamic viscosity is needed')

    return re
