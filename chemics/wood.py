
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
       Physical Properties of Wood. Chapter 4 in Wood Handbook, pp. 1-19,
       2010.
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


def k_wood(gb, so, x):
    """
    Thermal conductivity of wood based on moisture content, volumetric
    shrinkage, and basic specific gravity

    .. math:: k = G_x (B + C x) + A

    where :math:`k` is thermal conductivity [W/(mK)] of wood, :math:`G_x` is
    specific gravity [-] based on volume at moisture content :math:`x` [%] and
    :math:`A, B, C` are constants.

    The :math:`G_x` term is determined from

    .. math:: G_x = \\frac{G_b}{1 - S_x / 100}

    where :math:`G_b` is basic specific gravity [-] and :math:`S_x` is
    volumetric shrinkage [%] from green condition to moisture content :math:`x`.

    The :math:`S_x` term is calculated from

    .. math:: S_x = S_o \\left(1 - \\frac{x}{MC_{fs}} \\right)

    where :math:`S_o` is volumetric shrinkage [%] from Table 4-3 [2]_ and :math:`MC_{fs}`
    is the fiber saturation point assumed to be 30% moisture content.

    Parameters
    ----------
    gb : float
        Basic specific gravity [-]
    so : float
        Volumetric shrinkage [%]
    x : float
        Moisture content [%]

    Returns
    -------
    k : float
        Thermal conductivity [W/(mK)]

    Example
    -------
    >>> k_wood(0.54, 12.3, 10)
    0.1567

    References
    ----------
    .. [2] Samuel V. Glass and Samuel L. Zelinka. Moisture Relations and
       Physical Properties of Wood. Chapter 4 in Wood Handbook, pp. 1-19,
       2010.
    """

    mcfs = 30   # fiber staturation point estimate [%]

    # shrinkage from green to final moisture content, Eq. 4-7 [%]
    sx = so * (1 - x / mcfs)

    # specific gravity based on volume at given moisture content, Eq. 4-9
    gx = gb / (1 - sx / 100)

    # thermal conductivity, Eq. 4-15 [W/(mK)]
    a = 0.01864
    b = 0.1941
    c = 0.004064
    k = gx * (b + c * x) + a

    return k
