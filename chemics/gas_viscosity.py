import numpy as np
import os
import pandas as pd


def mu_gas(formula, temp, cas=None, disp=False):
    """
    Gas viscosity as a function of temperature using coefficients in Yaws'
    Critical Property Data for Chemical Engineers and Chemists [1]_. CAS
    (Chemical Abstracts Service) number may be required for some species.

    Parameters
    ----------
    formula : str
        Molecular formula of the gas.
    temp : float
        Gas temperature [K].
    cas : str, optional
        CAS number of the gas, required for some species.
    disp : bool
        Display information about the calculation such as the CAS number,
        applicable temperature range in Kelvin, and values for regression
        coefficients.

    Raises
    ------
    KeyError
        If provided CAS number is not found.
    ValueError
        If multiple substances found for given formula.
    KeyError
        If gas chemical formula not found.
    ValueError
        If given temperataure is out of range for calculation.

    Returns
    -------
    mu : float
        Gas viscosity [microPoise].

    Examples
    --------
    >>> mu_gas('CH4', 810)
    234.21

    >>> mu_gas('C2Cl2F4', 900, cas='374-07-2')
    314.90

    >>> mu_gas('H2', 404)
    113.18

    >>> mu_gas('N2', 773)
    363.82

    >>> mu_gas('N2', 773, disp=True)
    Formula        N2
    CAS            7727-37-9
    Min Temp. (K)  63.15
    Max Temp. (K)  1970.0
    A              4.46555763078484
    B              0.638137789753159
    C              -0.0002659562785407
    D              5.41126875437814e-08
    μ (microPoise) 363.8235847080749
    363.8235847080749

    References
    ----------
    .. [1] Carl L. Yaws. Viscosity Gas Tables 80 and 81 in Yaws' Critical
       Property Data for Chemical Engineers and Chemists. Published by Knovel,
       2014.
    """
    abs_path = os.path.dirname(os.path.abspath(__file__))
    data_inorganic = abs_path + '/data/mu-gas-inorganic.csv'
    data_organic = abs_path + '/data/mu-gas-organic.csv'

    if cas:
        df_inorg = pd.read_csv(data_inorganic, index_col=2)
        df_org = pd.read_csv(data_organic, index_col=2)

        if cas in df_inorg.index:
            data = df_inorg.loc[cas]
            formula = data['molecular formula']
        elif cas in df_org.index:
            data = df_org.loc[cas]
            formula = data['molecular formula']
        else:
            raise KeyError(f'CAS number {cas} not found')
    else:
        df_inorg = pd.read_csv(data_inorganic, index_col=0)
        df_org = pd.read_csv(data_organic, index_col=0)

        if formula in df_inorg.index:
            data = df_inorg.loc[formula]
            if isinstance(data, pd.DataFrame):
                raise ValueError(f'Multiple substances available for {formula}. '
                                 'Include CAS number with input parameters.')
            cas = data['CAS No.']
        elif formula in df_org.index:
            data = df_org.loc[formula]
            if isinstance(data, pd.DataFrame):
                raise ValueError(f'Multiple substances available for {formula}. '
                                 'Include CAS number with input parameters.')
            cas = data['CAS No.']
        else:
            raise KeyError(f'Formula {formula} not found')

    tmin = data['temperature, Tmin (K)']
    tmax = data['temperature, Tmax (K)']
    a = data['A']
    b = data['B']
    c = data['C']
    d = data['D']
    mu = a + b * temp + c * (temp**2) + d * (temp**3)

    if temp < tmin or temp > tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         f'{tmin}-{tmax} K for {formula} gas.')

    if disp:
        print('Formula       ', formula)
        print('CAS           ', cas)
        print('Min Temp. (K) ', tmin)
        print('Max Temp. (K) ', tmax)
        print('A             ', a)
        print('B             ', b)
        print('C             ', c)
        print('D             ', d)
        print('μ (microPoise)', mu)

    return mu


def mu_graham(mus, xs):
    """
    Calculate viscosity of a gas mixture using Graham's method [2]_. Formula
    presented here is based on Equation 1 from the Davidson report [3]_.

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
    >>> mu_h2 = cm.mu_gas('H2', 773.15)
    ... mu_n2 = cm.mu_gas('N2', 773.15)
    ... mu_graham([mu_h2, mu_n2], [0.85, 0.15])
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
    Calculate viscosity of a gas mixture using the approach by Herning and
    Zipperer [4]_. Formula presented here is based on Equation 1 from the
    Davidson report [5]_.

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
    >>> mu_h2 = cm.mu_gas('H2', 773.15)
    ... mu_n2 = cm.mu_gas('N2', 773.15)
    ... mw_h2 = cm.mw('H2')
    ... mw_n2 = cm.mw('N2')
    ... mu_herning([mu_h2, mu_n2], [mw_h2, mw_n2], [0.85, 0.15])
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
