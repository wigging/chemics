"""
Thermal conductivity
"""


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
