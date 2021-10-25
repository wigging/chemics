import pandas as pd
from pathlib import Path


def cp_liquid(formula, T, CAS='', full=False):
    """
    Calculate the heat capacity of a liquid as a function of temperature using
    coefficients from Yaws' Critical Property Data for Chemical Engineers and
    Chemists [1]_. The CAS (Chemical Abstracts Service) number may be
    required for some species. Inorganic species are calculated using

    .. math:: C_p = A + B\\,T + C\\,T^2 + D\\,T^3

    while organic species are determined from

    .. math:: C_p = A + B\\,T + C\\,T^2 + D\\,T^3 + E\\,T^4

    Parameters
    ----------
    formula : str
        Chemical formula.
    T : float
        Temperature [K].
    CAS : str, optional
        CAS number for the given chemical formula.
    full : bool, optional
        When `False` (default) only liquid heat capacity is returned, otherwise
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
    A, B, C, D : float
        Coefficients used to calculate the heat capacity. Also returns
        coefficient E for organic species.

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
    >>> cp_liquid('CBrF3', 250)
    107.2774

    >>> cp_liquid('CBrF3', 250, full=True)
    107.2774, '75-63-8', 177.59, 299.82, -215.02, 4.01, -0.017, 2.68e-05, 1.54e-09

    >>> cp_liquid('C38H76', 400, CAS='61828-17-9')
    1307.0624

    References
    ----------
    .. [1] Carl L. Yaws. Heat capacity of liquid Tables 43 and 44 in Yaws'
       Critical Property Data for Chemical Engineers and Chemists. Published
       by Knovel, 2014.
    """
    abs_path = Path(__file__).parent.absolute()

    path_org = abs_path / 'data/cp-liquid-organic.csv'
    path_inorg = abs_path / 'data/cp-liquid-inorganic.csv'

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

    if len(ser) == 8:
        Cp = A + B * T + C * T**2 + D * T**3
    else:
        E = ser['E']
        Cp = A + B * T + C * T**2 + D * T**3 + E * T**4

    if T < Tmin or T > Tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         f'{Tmin}-{Tmax} K for {formula} gas.')

    if full and len(ser) == 8:
        return Cp, CAS, Tmin, Tmax, A, B, C, D
    elif full and len(ser) == 9:
        return Cp, CAS, Tmin, Tmax, A, B, C, D, E
    else:
        return Cp
