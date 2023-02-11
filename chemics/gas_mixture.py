import numpy as np


def mu_graham(mus, xs):
    """
    Gas mixture viscosity using Graham's method [2]_. Formula presented here
    is based on Equation 1 from the Davidson report [3]_.

    .. math:: \\mu_{mix} = \\sum (x_i \\cdot \\mu_i)

    where :math:`\\mu_{mix}` is viscosity of the gas mixture, :math:`x_i` is
    mole fraction [-] of each component, and :math:`\\mu_i` is gas viscosity of
    each component.

    Parameters
    ----------
    mus : list, tuple, or array
        Viscosity of each gas component.
    xs : list, tuple, or array
        Mole fraction of each gas component [-]

    Returns
    -------
    mu : float
        Gas viscosity of the mixture. Units are same as input viscosity.

    Raises
    ------
    ValueError
        If sum of mole fractions does not equal 1.0

    Example
    -------
    >>> import chemics as cm
    >>> gas1 = cm.Gas('H2')
    >>> mu1 = gas1.mu_yaws(773.15)
    >>> gas2 = cm.Gas('N2')
    >>> mu2 = gas2.mu_yaws(773.15)
    >>> cm.mu_graham([mu1, mu2], [0.85, 0.15])
    207.37

    References
    ----------
    .. [2] Thomas Graham. On the Motion of Gases. Philosophical Transactions of
       the Royal Society of London, vol. 136, pp. 573-631, 1846.
    .. [3] Thomas Davidson. A Simple and Accurate Method for Calculating
       Viscosity of Gaseous Mixtures. United States Department of the Interior:
       Report of Investigations 9456, 1993.
    """
    mus = np.asarray(mus)
    xs = np.asarray(xs)
    if not np.isclose(xs.sum(), 1.0):
        raise ValueError('Sum of mole fractions must be 1.0')
    mu_mix = np.sum(mus * xs)
    return mu_mix


def mu_herning(mus, mws, xs):
    """
    Gas mixture viscosity using the approach by Herning and Zipperer
    [4]_. Formula presented here is based on Equation 1 from the Davidson
    report [5]_.

    .. math:: \\mu_{mix} = \\frac{\\sum (\\mu_i \\cdot x_i \\cdot \\sqrt{MW_i})}{\\sum (x_i \\cdot \\sqrt{MW_i})}

    where :math:`\\mu_{mix}` is viscosity of the gas mixture, :math:`x_i` is
    mole fraction [-] of each component, :math:`\\mu_i` is gas viscosity of
    each component, and :math:`MW_i` is the molecular weight [g/mol] of each
    component.

    Parameters
    ----------
    mus : list, tuple, or array
        Viscosity of each gas component.
    mws : list, tuple, or array
        Molecular weight of each gas component [g/mol]
    xs : list, tuple, or array
        Mole fraction of each gas component [-]

    Returns
    -------
    mu : float
        Gas viscosity of the mixture. Units are same as input viscosity.

    Raises
    ------
    ValueError
        If sum of mole fractions does not equal 1.0

    Example
    -------
    >>> import chemics as cm
    >>> gas1 = cm.Gas('H2')
    >>> mw1 = gas1.mw
    >>> mu1 = gas1.mu_yaws(773.15)
    >>> gas2 = cm.Gas('N2')
    >>> mw2 = gas2.mw
    >>> mu2 = gas2.mu_yaws(773.15)
    >>> cm.mu_herning([mu1, mu2], [mw1, mw2], [0.85, 0.15])
    252.81

    References
    ----------
    .. [4] F. Herning and L. Zipperer. Calculation of the Viscosity of
       Technical Gas Mixtures From the Viscosity of the Individual Gases.
       Gas-und Wasserfach, vol. 79, pp. 69-73, 1936.
    .. [5] Thomas Davidson. A Simple and Accurate Method for Calculating
       Viscosity of Gaseous Mixtures. United States Department of the Interior:
       Report of Investigations 9456, 1993.
    """
    mus = np.asarray(mus)
    mws = np.asarray(mws)
    xs = np.asarray(xs)
    if not np.isclose(xs.sum(), 1.0):
        raise ValueError('Sum of mole fractions must be 1.0')
    mu = np.sum(mus * xs * np.sqrt(mws)) / np.sum(xs * np.sqrt(mws))
    return mu
