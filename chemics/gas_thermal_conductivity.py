import pandas as pd
import os


def k_gas_inorganic(formula, temp, full=False):
    """
    Thermal conductivity of gas as a function of temperature. Applicable to gas
    comprised of inorganic compounds. Results based on coefficients from Yaws'
    Critical Property Data for Chemical Engineers and Chemists [1]_.

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
    k_gas : float
        Thermal conductivity of gas [W/(m K)]

    k_gas, cas, tmin, tmax, a, b, c, d : tuple
        Additional values are only returned when keyword :code:`full=True`.

        | k_gas - Thermal conductivity of gas [W/(m K)]
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
    >>> k_gas_inorganic('N2', 773)
    0.0535

    >>> k_gas_inorganic('N2', 773, full=True)
    (0.0535, '7727-37-9', 63.15, 1500.0, -0.0002267, 0.0001027, -6.0151e-08,
    2.2331e-11)

    References
    ----------
    .. [1] Carl L. Yaws. Table 84. Thermal Conductivity of Gas – Inorganic
       Compounds in Yaws' Critical Property Data for Chemical Engineers and
       Chemists. Published by Knovel, 2014.
    """
    abs_path = os.path.dirname(os.path.abspath(__file__))
    data_file = abs_path + '/data/k-gas-inorganic.csv'

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

    k_gas = a + b * temp + c * (temp**2) + d * (temp**3)

    if full:
        return k_gas, cas, tmin, tmax, a, b, c, d
    else:
        return k_gas


def k_gas_organic(formula, temp, cas=None, full=False):
    """
    Thermal conductivity of gas as a function of temperature. Applicable to gas
    comprised of organic compounds. Results based on coefficients from Yaws'
    Critical Property Data for Chemical Engineers and Chemists [2]_.

    Parameters
    ----------
    formula : string
        Molecular formula of the gas.
    temp : float
        Temperature of the gas [K]
    cas : string
        CAS number of the gas, required for some species [-]
    full : bool, optional
        When set to :code:`False` (default) just thermal conductivity is
        returned. When set to :code:`True` then return thermal conductivity and
        other information.

    Returns
    -------
    k_gas : float
        Thermal conductivity of gas [W/(m K)]

    k_gas, cas, tmin, tmax, a, b, c, d : tuple
        Additional values are only returned when keyword :code:`full=True`.

        | k_gas - Thermal conductivity of gas [W/(m K)]
        | cas - CAS number [-]
        | tmin, tmax - Temperature range at which results are applicable [K]
        | a, b, c, d - Values for regression coefficients [-]

    Raises
    ------
    ValueError
        If gas formula is not available in CSV data file.
    ValueError
        If multiple substances have same formula. Require CAS number.
    ValueError
        If gas temperature is not in range between Tmin and Tmax.

    Examples
    --------
    >>> k_gas_organic('CO', 801)
    0.05722

    >>> k_gas_organic('C18H38O', 920, cas='593-32-8')
    0.04174

    References
    ----------
    .. [2] Carl L. Yaws. Table 85. Thermal Conductivity of Gas – Organic
       Compounds in Yaws' Critical Property Data for Chemical Engineers and
       Chemists. Published by Knovel, 2014.
    """
    abs_path = os.path.dirname(os.path.abspath(__file__))
    data_file = abs_path + '/data/k-gas-organic.csv'

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

    if temp < tmin or temp > tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         + f'{tmin} - {tmax} K for {formula} gas.')

    k_gas = a + b * temp + c * (temp**2) + d * (temp**3)

    if full:
        return k_gas, cas, tmin, tmax, a, b, c, d
    else:
        return k_gas
