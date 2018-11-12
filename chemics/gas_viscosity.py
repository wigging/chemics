import pandas as pd
import os


def mu_gas_inorganic(formula, temp, full=False):
    """
    Viscosity of gas as a function of temperature. Applicable to gas comprised
    of inorganic compounds. Results based on coefficients from Yaws' Critical
    Property Data for Chemical Engineers and Chemists [1]_.

    Parameters
    ----------
    formula : string
        Molecular formula of the gas.
    temp : float
        Temperature of the gas [K]
    full : bool, optional
        When set to :code:`False` (default) just thermal conductivity is
        returned. When set to :code:`True` then return thermal conductivity and
        other information.

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
    >>> mu_gas_inorganic('H2', 404)
    113.18

    >>> mu_gas_inorganic('N2', 773)
    363.82

    >>> mu_gas_inorganic('N2', 773, full=True)
    (363.823584708048, '7727-37-9', 63.15, 1970.0, 4.46555763078484,
    0.6381377897531589, -0.000265956278540745, 5.41126875437814e-08)

    References
    ----------
    .. [1] Carl L. Yaws. Table 80. Viscosity of Gas - Inorganic Compounds in
       Yaws' Critical Property Data for Chemical Engineers and Chemists.
       Published by Knovel, 2014.
    """
    abs_path = os.path.dirname(os.path.abspath(__file__))
    data_file = abs_path + '/data/mu-gas-inorganic.csv'

    df = pd.read_csv(data_file, index_col=0)

    if formula not in df.index:
        raise ValueError(f'Gas species {formula} is not available.')

    cas = df.loc[formula]['CAS No.']
    a = df.loc[formula]['A']
    b = df.loc[formula]['B']
    c = df.loc[formula]['C']
    d = df.loc[formula]['D']

    tmin = df.loc[formula]['temperature, Tmin (K)']
    tmax = df.loc[formula]['temperature, Tmax (K)']

    if temp < tmin or temp > tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         + f'{tmin} - {tmax} K for {formula} gas.')

    mu_gas = a + b * temp + c * (temp**2) + d * (temp**3)

    if full:
        return mu_gas, cas, tmin, tmax, a, b, c, d
    else:
        return mu_gas


def mu_gas_organic(formula, temp, cas=None, full=False):
    """
    Viscosity of gas as a function of temperature. Applicable to gas comprised
    of organic compounds. Results based on coefficients from Yaws' Critical
    Property Data for Chemical Engineers and Chemists [2]_.

    Parameters
    ----------
    formula : string
        Molecular formula of the gas.
    temp : float
        Temperature of the gas [K]
    full : bool, optional
        When set to :code:`False` (default) just thermal conductivity is
        returned. When set to :code:`True` then return thermal conductivity and
        other information.

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
    >>> mu_gas_organic('CH4', 810)
    234.21

    >>> mu_gas_organic('C2Cl2F4', 900, cas='374-07-2')
    314.90

    References
    ----------
    .. [2] Carl L. Yaws. Table 81. Viscosity of Gas - Organic Compounds in
       Yaws' Critical Property Data for Chemical Engineers and Chemists.
       Published by Knovel, 2014.
    """
    abs_path = os.path.dirname(os.path.abspath(__file__))
    data_file = abs_path + '/data/mu-gas-organic.csv'

    df = pd.read_csv(data_file, index_col=0)

    if formula not in df.index:
        raise ValueError(f'Gas species {formula} is not available.')

    if isinstance(df.loc[formula], pd.DataFrame) and cas is None:
        raise ValueError(f'Multiple substances available for {formula}.'
                         + ' Include CAS number as a function parameter.')

    if cas:
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
                         + f'{tmin} - {tmax} K for {formula} gas.')

    mu_gas = a + b * temp + c * (temp**2) + d * (temp**3)

    if full:
        return mu_gas, cas, tmin, tmax, a, b, c, d
    else:
        return mu_gas
