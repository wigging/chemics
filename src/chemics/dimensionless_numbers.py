"""
Functions for dimensionless numbers.
"""


def archimedes(dp, rhog, rhos, mu):
    r"""
    Calculate the dimensionless Archimedes number.

    .. math:: Ar = \frac{d_p^3 \rho_g (\rho_s - \rho_g) g}{\mu^2}

    Parameters
    ----------
    dp : float
        Particle diameter in meters
    rhog : float
        Gas density in kg/m\ :sup:`3`
    rhos : float
        Solid density in kg/m\ :sup:`3`
    mu : float
        Dynamic viscosity in kg/(m⋅s)

    Returns
    -------
    ar : float
        Archimedes number

    Example
    -------
    >>> cm.archimedes(0.001, 910, 2500, 0.001307)
    8309.1452...

    References
    ----------
    Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
    Butterworth-Heinemann, 2nd edition, 1991.
    """
    g = 9.81  # gravity acceleration in m/s²
    ar = (dp**3 * rhog * (rhos - rhog) * g) / (mu**2)
    return ar


def biot(h, d, k):
    r"""
    Calculate the dimensionless Biot number.

    .. math:: Bi = \frac{h\, d}{k}

    Parameters
    ----------
    h : float
        Convective heat transfer coefficient in W/(m\ :sup:`2`\ ⋅K)
    d : float
        Characteristic length or dimension in meters
    k : float
        Thermal conductivity in W/(m⋅K)

    Returns
    -------
    bi : float
        Biot number

    Example
    -------
    >>> cm.biot(4.63, 0.001, 3.84)
    0.0012057...

    References
    ----------
    Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
    Butterworth-Heinemann, 2nd edition, 1991.
    """
    bi = (h * d) / k
    return bi


def peclet(ui, L, Dax):
    r"""
    Calculate the dimensionless Peclet number for mass transfer.

    The Peclet number is defined as the ratio between the bulk mass transport
    (convection) and the molecular diffusion.

    .. math:: Pe = \frac{u_i L}{D_{ax}}

    Parameters
    ----------
    ui : float
        Interstitial velocity in m/s
    L : float
        Length or characteristic dimension in meters
    Dax : float
        Axial dispersion coefficient in m\ :sup:`2`\ /s

    Returns
    -------
    pe : float
        Peclet number

    Example
    -------
    >>> cm.peclet(3.0e-3, 0.25, 4.7e-4)
    1.5957...

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    pe = ui * L / Dax
    return pe


def prandtl(cp=None, mu=None, k=None, nu=None, alpha=None):
    r"""
    Calculate the dimensionless Prandtl number for a fluid or gas.

    .. math:: Pr = \frac{c_p \mu}{k} = \frac{\nu}{\alpha}

    Parameters
    ----------
    cp : float
        Specific heat in J/(kg⋅K)
    mu : float
        Dynamic viscosity in kg/(m⋅s)
    k : float
        Thermal conductivity in W/(m⋅K)
    nu : float, optional
        Kinematic viscosity in m\ :sup:`2`\ /s
    alpha : float, optional
        Thermal diffusivity in m\ :sup:`2`\ /s

    Returns
    -------
    pr : float
        Prandtl number

    Examples
    --------
    >>> cm.prandtl(cp=4188, mu=0.001307, k=0.5674)
    9.647...

    >>> cm.prandtl(nu=1.5064e-5, alpha=2.1002e-5)
    0.71726...

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
        raise ValueError("Must provide (cp, mu, k) or (nu, alpha)")

    return pr


def pyrolysis_one(k, kr, rho, cp, r):
    r"""
    Calculate the pyrolysis number Py I for a biomass particle.

    .. math:: Py^I = \frac{k}{\rho\,C_p\,R^2\,K}

    Parameters
    ----------
    k : float
        Thermal conductivity of the biomass particle in W/(m⋅K)
    kr : float
        Rate constant in 1/s
    rho : float
        Density of the biomass particle in kg/m\ :sup:`3`
    cp : float
        Heat capacity of the biomass particle in J/(kg⋅K)
    r : float
        Radius or characteristic length of the biomass particle in meters

    Returns
    -------
    pyro_one : float
        Pyrolysis number Py I

    Example
    -------
    >>> cm.pyrolysis_one(k=0.12, kr=1.38556, rho=540, cp=3092.871049, r=0.0001847)
    1.52...

    References
    ----------
    D.L. Pyle and C.A. Zaror. Heat Transfer and Kinetics in the Low
    Temperature Pyrolysis of Solids. Chemical Engineering Science, vol. 39,
    no. 1, pg. 147-158, 1984.
    """
    pyro_one = k / (kr * rho * cp * (r**2))
    return pyro_one


def pyrolysis_two(h, kr, rho, cp, r):
    r"""
    Calculate the pyrolysis number Py II for a biomass particle.

    .. math:: Py^{II} = \frac{h}{\rho\,C_p\,R\,K}

    Parameters
    ----------
    h : float
        Convective heat transfer coefficient in W/m\ :sup:`2`\ K
    kr : float
        Rate constant in 1/s
    rho : float
        Density of the biomass particle in kg/m\ :sup:`3`
    cp : float
        Heat capacity of the biomass particle in J/(kg⋅K)
    r : float
        Radius or characteristic length of the biomass particle in meters

    Returns
    -------
    pyro_two : float
        Pyrolysis number Py II

    Example
    -------
    >>> cm.pyrolysis_two(h=862.6129, kr=1.38556, rho=540, cp=3092.871049, r=0.0001847)
    2.018...

    References
    ----------
    D.L. Pyle and C.A. Zaror. Heat Transfer and Kinetics in the Low
    Temperature Pyrolysis of Solids. Chemical Engineering Science, vol. 39,
    no. 1, pg. 147-158, 1984.
    """
    pyro_two = h / (kr * rho * cp * r)
    return pyro_two


def reynolds(u, d, rho=None, mu=None, nu=None):
    r"""
    Calculate the dimensionless Reynolds number for a fluid or gas flow.

    .. math:: Re = \frac{\rho\, u\, d}{\mu} = \frac{u\, d}{\nu}

    Parameters
    ----------
    u : float
        Flow speed in m/s
    d : float
        Characteristic length or dimension in meters
    rho : float, optional
        Density of the fluid or gas in kg/m\ :sup:`3`
    mu : float, optional
        Dynamic viscosity of the fluid or gas in kg/(m⋅s)
    nu : float, optional
        Kinematic viscosity of the fluid or gas in m\ :sup:`2`\ /s

    Returns
    -------
    re : float
        Reynolds number

    Examples
    --------
    >>> cm.reynolds(2.6, 0.025, rho=910, mu=0.38)
    155.65789...

    >>> cm.reynolds(0.25, 0.102, nu=1.4e-6)
    18214.2857...

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
        raise ValueError("Must provide (u, d, rho, mu) or (u, d, nu)")

    return re


def schmidt(mu, rho, Dm):
    r"""
    Calculate the dimensionless Schmidt number.

    The Schmidt number represents the ratio between momentum diffusivity
    (kinematic viscosity) and mass diffusivity.

    .. math:: Sc = \frac{\mu}{\rho D_m}

    Parameters
    ----------
    mu : float
        Viscosity of the fluid flowing through the packed bed in Pa⋅s
    rho : float
        Density of the fluid flowing through the packed bed in kg/m\ :sup:`3`
    Dm : float
        Molecular diffusion coefficient in m\ :sup:`2`\ /s

    Returns
    -------
    sc : float
        Schmidt number

    Example
    -------
    >>> cm.schmidt(8.90e-4, 997.07, 2.299e-9)
    388.26...

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    sc = mu / rho / Dm
    return sc


def sherwood(k, d, Dm):
    r"""
    Calculate the dimensionless Sherwood number.

    The Sherwood number represents the ratio between the convective mass
    transfer and the rate of diffusive mass transport.

    .. math:: Sh = \frac{k d}{D_m}

    Parameters
    ----------
    k : float
        Convective mass transfer coefficient in m/s
    d : float
        Particle diameter or characteristic length in meters
    Dm : float
        Molecular diffusion coefficient in m\ :sup:`2`\ /s

    Returns
    -------
    sh : float
        Sherwood number

    Example
    -------
    >>> cm.sherwood(2.3e-4, 5.0e-6, 4.0e-9)
    0.2875...

    References
    ----------
    J.D. Seader, E.J. Henley, D.K. Roper. Separation Process Principles.
    John Wiley & Sons, Inc., 3rd edition, 2011.
    """
    sh = k * d / Dm
    return sh


def flow_regime(Re=None, u=None, d=None, rho=None, mu=None, nu=None):
    r"""
    Flow regime.

    Determine flow regime (laminar, transitional or turbulent) considering the
    Reynolds number boundaries for the case of a straight, non-smooth pipe.

    | Laminar regime ........ Re < 2100
    | Transitional regime ... 2100 <= Re <= 4000
    | Laminar regime ........ Re > 4000

    Parameters
    ----------
    Re : float, optional
        Reynolds number
    u : float, optional
        Flow speed in m/s
    d : float, optional
        Characteristic length or dimension in meters
    rho : float, optional
        Density of the fluid or gas in kg/m\ :sup:`3`
    mu : float, optional
        Dynamic viscosity of the fluid or gas in kg/(m⋅s)
    nu : float, optional
        Kinematic viscosity of the fluid or gas in m\ :sup:`2`\ /s

    Returns
    -------
    regime : string
        Flow regime. One of laminar, transitional or turbulent.

    Examples
    --------
    >>> cm.flow_regime(u=2.6, d=0.025, rho=910, mu=0.38)
    'laminar'

    >>> cm.flow_regime(Re=3250)
    'transitional'

    >>> cm.flow_regime(u=0.25, d=0.102, nu=1.4e-6)
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
            Re = reynolds(u, d, rho=rho, mu=mu, nu=nu)
        else:
            raise ValueError("Must provide Re or (u, d, rho, mu) or (u, d, nu)")
    if Re < 2100:
        regime = "laminar"
    elif 2100 <= Re <= 4000:
        regime = "transitional"
    elif Re > 4000:
        regime = "turbulent"
    else:
        regime = ""

    return regime
