import numpy as np


def massfrac_to_molefrac(y, mw):
    """
    Convert from mass fractions to mole fractions. Calculation assumes a total
    mass of 100 g.

    .. math::

       m_i = y_i \\times 100

       x_i = \\frac{\\frac{m_i}{MW_i}}{\\sum\\frac{m_i}{MW_i}}

    where :math:`m` is mass [g], :math:`y` is mass fraction [-], :math:`x` is
    mole fraction [-], and :math:`MW` is molecular weight [g/mol] of each
    component.

    Parameters
    ----------
    y : list, tuple or array
        Mass fraction of each component [-]
    mw : list, tuple or array
        Molecular weight of each component [g/mol]

    Returns
    -------
    x : array
        Mole fractions of each component [-]

    Example
    -------
    >>> y = [0.36, 0.16, 0.20, 0.28]
    ... mw = [12.011, 1.008, 15.999, 14.007]
    ... massfrac_to_molefrac(y, mw)
    [0.136 0.718 0.057 0.09]
    """

    # convert inputs to NumPy arrays
    y = np.asarray(y)
    mw = np.asarray(mw)

    if not np.isclose(y.sum(), 1.0):
        raise ValueError('Sum of mass fractions must be 1.0')

    # mass of each component assuming 100 total grams [g]
    m = y * 100

    # mole fraction of each component [-]
    x = (m / mw) / np.sum(m / mw)

    return x


def molefrac_to_massfrac(x, mw):
    """
    Convert from mole fractions to mass fractions. Calculation assumes total
    moles is 100.

    .. math::

       n_i &= x_i \\times 100

       y_i &= \\frac{n_i\\, MW_i}{\\sum n_i\\, MW_i}

    where :math:`n` is moles [mol], :math:`x` is mole fraction [-], :math:`y`
    is mass fraction [-], and :math:`MW` is molecular weight [g/mol] of each
    component.

    Parameters
    ----------
    x : list, tuple, or array
        Mole fraction of each component [-]
    mw : list, tuple or array
        Molecular weight of each component [g/mol]

    Returns
    -------
    y : array
        Mass fraction of each component [-]

    Example
    -------
    >>> x = [0.36, 0.16, 0.20, 0.28]
    >>> mw = [12.011, 1.008, 15.999, 14.007]
    ... molefrac_to_massfrac(x, mw)
    [0.373 0.014 0.276 0.338]
    """

    # convert inputs to NumPy arrays
    x = np.asarray(x)
    mw = np.asarray(mw)

    if not np.isclose(x.sum(), 1.0):
        raise ValueError('Sum of mole fractions must be 1.0')

    # moles of each component assuming 100 total moles [mol]
    n = x * 100

    # mass fraction of each component [-]
    y = (n * mw) / np.sum(n * mw)

    return y


def slm_to_lpm(slm, pgas, tgas):
    """
    Convert volumetric gas flow from standard liters per minute (SLM or SLPM)
    to liters per minute (LPM) where STP defined as 273.25 K and 101,325 Pa.

    .. math::

       1 LPM = 1 SLPM \\times \\frac{T_{gas}}{273.15\\,K} \\times \\frac{14.696\\,psi}{P_{gas}}

    Parameters
    ----------
    slm : float
        Volumetric gas flow in standard liters per minute [SLM]
    pgas : float
        Absolute gas pressure [kPa]
    tgas : float
        Gas temperature [K]

    Returns
    -------
    lpm : float
        Volumetric gas flow in liters per minute [LPM]

    Example
    -------
    >>> slm_to_lpm(580, 150, 773)
    1108.74

    References
    ----------
    Wikipedia contributors. (2018, February 8). Standard litre per minute.
    In Wikipedia online. Retrieved from
    https://en.wikipedia.org/wiki/Standard_litre_per_minute
    """

    # equation requires gas pressure as psi so convert kPa to psi
    pgas_psi = pgas * 0.1450377
    lpm = slm * (tgas / 273.15) * (14.696 / pgas_psi)
    return lpm
