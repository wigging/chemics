import numpy as np
import os
import pandas as pd

__all__ = ['mu_gas', 'mu_graham', 'mu_herning']


def _mu(df, formula, temp, cas, full):
    """
    Helper for the `mu_gas` function to determine gas viscosity.

    Parameters
    ----------
    df : dataframe
        Dataframe from inorganic or organic data
    formula : str
        Molecular formula for the gas
    temp : float
        Gas temperature
    cas : str
        CAS number
    full : bool
        Flag to print more information

    Returns
    -------
    mu_gas : float
        Viscosity of gas [micropoise]
    mu_gas, cas, tmin, tmax, a, b, c, d : tuple
        Additional values returned only if full=True.
    """

    if cas:
        # new dataframe based only on row for cas number
        df = df[df['CAS No.'] == str(cas)]

    cas = df.loc[formula]['CAS No.']
    tmin = df.loc[formula]['temperature, Tmin (K)']
    tmax = df.loc[formula]['temperature, Tmax (K)']
    a = df.loc[formula]['A']
    b = df.loc[formula]['B']
    c = df.loc[formula]['C']
    d = df.loc[formula]['D']

    if temp < tmin or temp > tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         f'{tmin} - {tmax} K for {formula} gas.')

    mu = a + b * temp + c * (temp**2) + d * (temp**3)

    if full:
        return mu, cas, tmin, tmax, a, b, c, d
    else:
        return mu


def mu_gas(formula, temp, cas=None, full=False):
    """
    Viscosity of gas as a function of temperature. Results calculated from
    coefficients in Yaws' Critical Property Data for Chemical Engineers and
    Chemists [1]_. CAS (Chemical Abstracts Service) number may be required for
    some species.

    Parameters
    ----------
    formula : str
        Molecular formula of the gas.
    temp : float
        Temperature of the gas [K]
    cas : str, optional
        CAS number of the gas, required for some species [-]
    full : bool, optional
        When set to :code:`False` (default) just gas viscosity is returned.
        When set to :code:`True` then return gas viscosity and other
        information.

    Returns
    -------
    mu_gas : float
        Viscosity of gas [micropoise]

    mu_gas, cas, tmin, tmax, a, b, c, d : tuple
        Additional values are only returned when keyword :code:`full=True`.

        | mu_gas - Viscosity of gas [micropoise]
        | cas - CAS number [-]
        | tmin, tmax - Temperature range at which results are applicable [K]
        | a, b, c, d - Values for regression coefficients [-]

    Raises
    ------
    ValueError
        If gas formula is not found in csv data file.
    ValueError
        If gas temperature is not in range between tmin and tmax.

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

    >>> mu_gas('N2', 773, full=True)
    (363.82, '7727-37-9', 63.15, 1970.0, 4.46, 0.63, -0.00026, 5.41e-08)

    References
    ----------
    .. [1] Carl L. Yaws. Viscosity Gas Tables 80 and 81 in Yaws' Critical
       Property Data for Chemical Engineers and Chemists. Published by Knovel,
       2014.
    """
    abs_path = os.path.dirname(os.path.abspath(__file__))

    data_inorganic = abs_path + '/data/mu-gas-inorganic.csv'
    df_inorganic = pd.read_csv(data_inorganic, index_col=0)

    data_organic = abs_path + '/data/mu-gas-organic.csv'
    df_organic = pd.read_csv(data_organic, index_col=0)

    if formula in df_inorganic.index:

        if isinstance(df_inorganic.loc[formula], pd.DataFrame) and cas is None:
            raise ValueError(f'Multiple substances available for {formula}. '
                             'Include CAS number with input parameters.')

        mu = _mu(df_inorganic, formula, temp, cas, full)
        return mu

    elif formula in df_organic.index:

        if isinstance(df_organic.loc[formula], pd.DataFrame) and cas is None:
            raise ValueError(f'Multiple substances available for {formula}. '
                             'Include CAS number with input parameters.')

        mu = _mu(df_organic, formula, temp, cas, full)
        return mu

    else:
        raise ValueError(f'Gas viscosity for {formula} is not available.')


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
