
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

    where :math:`S_o` is volumetric shrinkage [%] from Table 4-3 [1]_ and :math:`MC_{fs}`
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
    .. [1] Samuel V. Glass and Samuel L. Zelinka. Moisture Relations and
       Physical Properties of Wood. Ch. 4 in Wood Handbook, pp. 1-19, 2010.
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
