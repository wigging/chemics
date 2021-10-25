import pandas as pd
from pathlib import Path


def cp_gas(formula, T, CAS='', full=False):
    """
    Calculate heat capacity of a gas as a function of temperature using
    coefficients from Yaws' Critical Property Data for Chemical Engineers and
    Chemists [1]_. The CAS (Chemical Abstracts Service) number may be required for
    some species.

    .. math:: C_p = A + B\\,T + C\\,T^2 + D\\,T^3 + E\\,T^4 + F\\,T^5 + G\\,T^6

    Parameters
    ----------
    formula : str
        Chemical formula.
    T : float
        Temperature [K].
    CAS : str, optional
        CAS number for the given chemical formula.
    full : bool, optional
        When `False` (default) only gas heat capacity is returned, otherwise
        heat capacity and other information are returned.

    Returns
    -------
    Cp : float
        Heat capacity [J/(mol⋅K)].

    If `full` is `True` then also return

    CAS : str
        CAS number for the given chemical formula.
    Tmin : float
        Minimum temperature for the correlation [K].
    Tmax : float
        Maximum temperature for the correlation [K].
    A, B, C, D, E, F, G : float
        Coefficients used to calculate the heat capacity.

    Raises
    ------
    ValueError
        If heat capacity is not available for chemical formula.
    ValueError
        If multiple substances have same chemical then CAS number is required.
    ValueError
        If temperature is outside range of applicable data.

    Examples
    --------
    >>> cp_gas('CBrClF2', 700)
    97.4982

    >>> cp_gas('C5H10O2', 850, CAS='75-98-9')
    268.4920

    >>> cp_gas('NO2', 900)
    51.0686

    References
    ----------
    .. [1] Carl L. Yaws. Heat capacity of gas Tables 39 and 40 in Yaws'
       Critical Property Data for Chemical Engineers and Chemists. Published
       by Knovel, 2014.
    """
    abs_path = Path(__file__).parent.absolute()

    path_org = abs_path / 'data/cp-gas-organic.csv'
    path_inorg = abs_path / 'data/cp-gas-inorganic.csv'

    df_org = pd.read_csv(path_org, index_col=0)
    df_inorg = pd.read_csv(path_inorg, index_col=0)

    # Determine if formula is organic or inorganic species otherwise it's not
    # available in the Yaws' correlation data.
    if formula in df_org.index:
        df = df_org
    elif formula in df_inorg.index:
        df = df_inorg
    else:
        raise ValueError(f'Heat capacity for {formula} is not available.')

    # Require CAS number if multiple species are found.
    if isinstance(df.loc[formula], pd.DataFrame) and CAS == '':
        raise ValueError(f'Multiple substances available for {formula}. '
                         'Include CAS number with input parameters.')
    elif isinstance(df.loc[formula], pd.DataFrame):
        df = df[df['CAS No.'] == CAS]

    ser = df.loc[formula]

    CAS = ser['CAS No.']
    Tmin = ser['temperature, Tmin (K)']
    Tmax = ser['temperature, Tmax (K)']
    A = ser['A']
    B = ser['B']
    C = ser['C']
    D = ser['D']
    E = ser['E']
    F = ser['F']
    G = ser['G']

    if T < Tmin or T > Tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         f'{Tmin}-{Tmax} K for {formula} gas.')

    Cp = A + B * T + C * T**2 + D * T**3 + E * T**4 + F * T**5 + G * T**6

    if full:
        return Cp, CAS, Tmin, Tmax, A, B, C, D, E, F, G
    else:
        return Cp
