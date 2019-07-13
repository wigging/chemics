
def cp_wood(x, tk):
    """
    Heat capacity of wood based on moisture content and temperature

    .. math:: c_{p,x} = \\left(c_{p0} + c_{pw} \\frac{x}{100}\\right) / \\left(1 + \\frac{x}{100}\\right) + A_c

    where :math:`c_{p,x}` is heat capacity of wet wood [kJ/(kg K)],
    :math:`c_{p0}` is heat capacity of dry wood [kJ/(kg K)], :math:`c_{pw}` is
    heat capacity of water as 4.18 kJ/(kg K), :math:`x` is moisture content [%],
    and :math:`Ac` is an adjustment factor that accounts for the additional
    energy in the wood–water bond [1]_.

    The :math:`c_{p0}` term is determined from

    .. math:: c_{p0} = 0.1031 + 0.003867\\,T

    where :math:`T` is temperature [K]. The :math:`A_c` term is calculated from

    .. math:: A_c = x (b_1 + b_2 T + b_3 x)

    with :math:`b_1 = -0.06191`, :math:`b_2 = 2.36e\\times10^{-4}`, and :math:`b_3 = -1.33\\times10^{-4}`.

    Parameters
    ----------
    x : float
        Moisture content [%]
    tk : float
        Temperature [K]

    Returns
    -------
    cp : float
        Heat capacity of wood [kJ/(kg K)]

    Example
    -------
    >>> cp_wood(12, 340)
    1.91

    References
    ----------
    .. [1] Samuel V. Glass and Samuel L. Zelinka. Moisture Relations and
       Physical Properties of Wood. Ch. 4 in Wood Handbook, pp. 1-19, 2010.
    """

    cpw = 4.18  # heat capacity of water, kJ/(kg K)

    # coefficients for adjustment factor Ac
    b1 = -0.06191
    b2 = 2.36e-4
    b3 = -1.33e-4

    # adjustment factor for additional energy in wood-water bond, Eq. 4-18
    Ac = x * (b1 + b2 * tk + b3 * x)

    # heat capacity of dry wood, Eq. 4-16a, kJ/(kg K)
    cp_dry = 0.1031 + 0.003867 * tk

    # heat capacity of wood that contains water, Eq. 4-17, kJ/(kg K)
    cp_wet = (cp_dry + cpw * x / 100) / (1 + x / 100) + Ac

    return cp_wet
