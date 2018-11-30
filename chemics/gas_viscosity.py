import pandas as pd
import os

__all__ = ['mu_gas']


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
    (363.823584708048, '7727-37-9', 63.15, 1970.0, 4.46555763078484,
    0.6381377897531589, -0.000265956278540745, 5.41126875437814e-08)

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


def _mu(df, formula, temp, cas, full):
    """
    Helper for the mu_gas function to determine gas viscosity.

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

    tmin = df.loc[formula]['temperature, Tmin (K)']
    tmax = df.loc[formula]['temperature, Tmax (K)']

    if temp < tmin or temp > tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         f'{tmin} - {tmax} K for {formula} gas.')

    mu = a + b * temp + c * (temp**2) + d * (temp**3)

    if full:
        return mu, cas, tmin, tmax, a, b, c, d
    else:
        return mu
