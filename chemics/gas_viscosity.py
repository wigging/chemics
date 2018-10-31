
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
