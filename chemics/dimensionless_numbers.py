import chemics as cm


def archimedes(dp, rhog, rhos, mu):
    """
    Calculate the dimensionless Archimedes number.

    .. math:: Ar = \\frac{d_p^3 \\rho_g (\\rho_s - \\rho_g) g}{\\mu^2}

    Parameters
    ----------
    dp : float
        Particle diameter [m]
    rhog : float
        Gas density [kg/m³]
    rhos : float
        Solid density [kg/m³]
    mu : float
        Dynamic viscosity [kg/(m⋅s)]

    Returns
    -------
    ar : float
        Archimedes number [-]

    Example
    -------
    >>> archimedes(0.001, 910, 2500, 0.001307)
    8309.1452

    References
    ----------
    Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
    Butterworth-Heinemann, 2nd edition, 1991.
    """
    g = 9.81    # gravity acceleraton [m/s²]
    ar = (dp**3 * rhog * (rhos - rhog) * g) / (mu**2)
    return ar


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


def peclet(ui, L, Dax):
    """
    Calculate the dimensionless Peclet number for mass transfer.

    The Peclet number is defined as the ratio between the bulk mass transport
    (convection) and the molecular diffusion.

    .. math:: Pe = \\frac{u_i L}{D_{ax}}

    Parameters
    ----------
    ui : float
        Interstitial velocity [m/s]
    L : float
        Length or characteristic dimension [m]
    Dax : float
        Axial dispersion coefficient [m^2/s]

    Returns
    -------
    pe : float
        Peclet number [-]

    Example
    -------
    >>> peclet(3.0e-3, 0.25, 4.7e-4)
    1.5957

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    pe = ui * L / Dax
    return pe


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


def schmidt(mu, rho, Dm):
    """
    Calculate the dimensionless Schmidt number.

    The Schmidt number represents the ratio between momentum diffusivity
    (kinematic viscosity) and mass diffusivity.

    .. math:: Sc = \\frac{\\mu}{\\rho D_m}

    Parameters
    ----------
    mu : float
        Viscosity of the fluid flowing through the packed bed [Pa s]
    rho : float
        Density of the fluid flowing through the packed bed [kg/m^3]
    Dm : float
        Molecular diffusion coefficient [m^2/s]

    Returns
    -------
    sc : float
        Schmidt number [-]

    Example
    -------
    >>> schmidt(8.90e-4, 997.07, 2.299e-9)
    388.26

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    sc = mu / rho / Dm
    return sc


def sherwood(k, d, Dm):
    """
    Calculate the dimensionless Sherwood number.

    The Sherwood number represents the ratio between the convective mass
    transfer and the rate of diffusive mass transport.

    .. math:: Sh = \\frac{k d}{D_m}

    Parameters
    ----------
    k : float
        Convective mass transfer coefficient [m/s]
    d : float
        Particle diameter or characteristic length [m]
    Dm : float
        Molecular diffusion coefficient [m^2/s]

    Returns
    -------
    sh : float
        Sherwood number [-]

    Example
    -------
    >>> sherwood(2.3e-4, 5.0e-6, 4.0e-9)
    0.2875

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    sh = k * d / Dm
    return sh


def flow_regime(Re=None, u=None, d=None, rho=None, mu=None, nu=None):
    """
    Determine flow regime (laminar, transitional or turbulent) considering the
    Reynolds number boundaries for the case of a straight, non-smooth pipe.
    
    Laminar regime: Re < 2100
    
    Transitional regime: 2100 <= Re <= 4000
    
    Laminar regime: Re > 4000

    Parameters
    ----------
    Re : float, optional
        Reynolds number [-]
    u : float, optional
        Flow speed [m/s]
    d : float, optional
        Characteristic length or dimension [m]
    rho : float, optional
        Density of the fluid or gas [kg/m^3]
    mu : float, optional
        Dynamic viscosity of the fluid or gas [kg/(m s)]
    nu : float, optional
        Kinematic viscosity of the fluid or gas [m^2/s]

    Returns
    -------
    regime : string
        Flow regime. One of laminar, transitional or turbulent.

    Examples
    --------
    >>> flow_regime(u=2.6, d=0.025, rho=910, mu=0.38)
    'laminar'

    >>> flow_regime(Re=3250)
    'transitional'

    >>> flow_regime(u=0.25, d=0.102, nu=1.4e-6)
    'turbulent'

    Raises
    ------
    ValueError
        Must provide Re or (u, d, rho, mu) or (u, d, nu)

    References
    ----------
    R.H. Perry, D.W. Green. Perry's Chemical Engineers' Handbook.
    McGraw-Hill, 8th edition, 2008.
    """
    if not Re:
        if (rho and mu and not nu) or (nu and not rho and not mu):
            Re = cm.reynolds(u, d, rho=rho, mu=mu, nu=nu)
        else:
            raise ValueError(
                'Must provide Re or (u, d, rho, mu) or (u, d, nu)'
            )
    if Re < 2100:
        regime = 'laminar'
    elif 2100 <= Re <= 4000:
        regime = 'transitional'
    elif Re > 4000:
        regime = 'turbulent'

    return regime
