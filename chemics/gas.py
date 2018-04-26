import numpy as np


def k_n2(T):
    """
    Equation for thermal conductivity of nitrogen gas, N2, as a function of
    temperature based on formula from Yaw's online reference [#yaw1]_. Valid at
    temperatures from 63-1500 K.

    .. math::
       k_{N_2} = A + B*T + C*T^2 + D*T^3

    Parameters
    ----------
    T : float
        Temperature of N2 gas [K]

    Returns
    -------
    k : float
        Thermal conductivity of N2 gas [W/mK]

    Examples
    --------
    >>> k_n2(773)
    0.0535

    References
    ----------
    .. [#yaw1] Yaws' Transport Properties of Chemicals and Hydrocarbons.
    """
    A = -0.000226779
    B = 0.000102746
    C = -6.01514e-8
    D = 2.23319E-11
    k = A + B*T + C*(T**2) + D*(T**3)
    return k


def k_o2(T):
    """
    Equation for thermal conductivity of oxygen gas, O2, as a function of
    temperature based on formula from Yaw's online reference [#yaw2]_. Valid at
    temperatures from 80 K to 2000 K.

    .. math::
       k_{O_2} = A + B*T + C*T^2 + D*T^3

    Parameters
    ----------
    T : float
        Temperature of O2 gas [K]

    Returns
    -------
    k : float
        Thermal conductivity of O2 gas [W/mK]

    Examples
    --------
    >>> k_o2(773)
    0.0588

    References
    ----------
    .. [#yaw2] Yaws' Transport Properties of Chemicals and Hydrocarbons.
    """
    A = 0.000154746
    B = 9.41534E-05
    C = -2.75292E-08
    D = 5.20693E-12
    k = A + B*T + C*(T**2) + D*(T**3)
    return k


def mu_h2(T):
    """
    Calculate viscosity of hydrogen gas, H2, as a function of temperture. Valid
    at temperatures from 15 K to 1500 K. Equation and coefficients from Yaws'
    Handbook [#yaw3]_.

    .. math::
       \\mu_{H_2} = A + B \\cdot T + C \\cdot T^2 + D \\cdot T^3

    Parameters
    ----------
    T : float
       Temperature of hydrogen gas [K]

    Returns
    -------
    mu : float
        Viscosity of hydrogen gas in micropoise [uP]

    Examples
    --------
    .. code-block:: python

        # in units of micropoise, uP
        >>> mu_h2(773)
        179.73
        # in units of kilogram per meter per second, kg/(m s)
        >>> mu_h2(773) / 1e7
        1.79e-05

    References
    ----------
    .. [#yaw3] Yaws' Handbook of Properties of the Chemical Elements.
    """
    a = 1.761132
    b = 0.341654
    c = -0.000183676
    d = 5.114748e-8
    mu = a + (b * T) + (c * T**2) + (d * T**3)
    return mu


def mu_n2(T):
    """
    Calculate viscosity of nitrogen gas, N2, as a function of temperature.
    Valid at temperatures from 63.15 K to 1970 K. Equation and coefficients
    from Yaws' Handbook [#yaw4]_.

    .. math::
       \\mu_{N_2} = A + B \\cdot T + C \\cdot T^2 + D \\cdot T^3

    Parameters
    ----------
    T : float
        Tempreature of nitrogen gas [K]

    Returns
    -------
    mug : float
        Viscosity of nitrogen gas in micropoise [uP]

    Examples
    --------
    .. code-block:: python

        # in units of micropoise, uP
        >>> mu_n2(773)
        363.82
        # in units of kilogram per meter per second, kg/(ms)
        >>> mu_n2(773) / 1e7
        3.63e-05

    References
    ----------
    .. [#yaw4] Yaws' Handbook of Properties of the Chemical Elements.
    """
    a = 4.465557
    b = 0.638137
    c = -0.000265956
    d = 5.411268e-8
    mu = a + (b * T) + (c * T**2) + (d * T**3)
    return mu


def patm(alt):
    """
    Determine atmospheric pressure at altitudes up to 51 km. Based on article
    by Roland Stull [#stull]_.

    Parameters
    ----------
    alt : float
        Altitude or elevation above sea level [m]

    Returns
    -------
    Patm : float
        Atmospheric pressure [Pa]

    References
    ----------
    .. [#stull] Practical Meteorology: An Algebra-based Survey of Atmospheric
       Science by Roland Stull.
    """
    alt = alt/1000              # convert altitude from meters to kilometers
    Ro = 6356.766               # average radius of the Earth, km
    H = (Ro * alt)/(Ro + alt)   # geopotential height, km

    Patm = None     # initiate pressure variable

    if H <= 11:
        T = 288.15 - (6.5 * H)
        Patm = 101325 * (288.15 / T) ** (-5.255877)
    elif H <= 20:
        T = 216.65
        Patm = 22632 * np.exp(-0.1577 * (H - 11))
    elif H <= 32:
        T = 216.65 + (H - 20)
        Patm = 5474.9 * (216.65 / T) ** (34.16319)
    elif H <= 47:
        T = 228.65 + 2.8 * (H - 32)
        Patm = 868 * (228.65 / T) ** 12.2011
    elif H <= 51:
        T = 270.65
        Patm = 110.9 * np.exp(-0.1262 * (H - 47))
    else:
        raise ValueError('geopotential height must be less than 51 km')

    # return atmospheric pressure at altitude, Pa
    return Patm


def rhog(mw, Pgas, Tgas):
    """
    Calculate gas density from molecular weight, pressure, and temperature.

    .. math::
       \\rho = \\frac{P * MW}{R * T}

    Parameters
    ----------
    mw : float
        Molecular weight of gas [g/mol]
    Pgas : float
        Pressure of the gas [Pa]
    Tgas : float
        Temperature of the gas [K]

    Returns
    -------
    rho : float
        Density of gas [kg/m^3]

    Examples
    --------
    >>> rhog(28, 101325, 773)
    0.4414
    """
    mw = mw / 1000  # convert g/mol to kg/mol
    R = 8.3145      # ideal gas constant, (m^3 Pa)/(K mol)
    rho = (Pgas*mw) / (R*Tgas)
    return rho
