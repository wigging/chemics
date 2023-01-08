import pandas as pd
import os


def k_yaws(formula, temp, cas=None, disp=False):
    """
    Gas thermal conductivity as a function of temperature using Yaws'
    coefficients [1]_. The CAS(Chemical Abstracts Service) number may be
    required for some species.

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
    ValueError
        If provided CAS number is not found.
    ValueError
        If multiple substances found for given formula.
    ValueError
        If gas chemical formula not found.
    ValueError
        If given temperataure is out of range for calculation.

    Returns
    -------
    k : float
        Gas thermal conductivity [W/m⋅K].

    Examples
    --------
    >>> k_yaws('N2', 773)
    0.05356876932986771

    >>> k_yaws('C18H38O', 920, cas='593-32-8')
    0.04174183983759623

    >>> k_yaws('N2', 773, disp=True)
    Formula        N2
    Name           nitrogen
    CAS            7727-37-9
    Min Temp. (K)  63.15
    Max Temp. (K)  1500.0
    A              -0.000226779433664
    B              0.0001027462918646
    C              -6.015141955845571e-08
    D              2.2331907127430105e-11
    k      (W/m⋅K) 0.05356876932986771
    0.05356876932986771

    References
    ----------
    .. [1] Carl L. Yaws. Thermal Conductivity Gas Tables 84 and 85 in Yaws'
       Critical Property Data for Chemical Engineers and Chemists. Published
       by Knovel, 2014.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(path + '/data/gas-thermal-conductivity-yaws.csv')

    if cas:
        row = df.query(f"CAS == '{cas}'")
        if len(row) == 0:
            raise ValueError(f'CAS number {cas} not found')
    else:
        row = df.query(f"Formula == '{formula}'")
        if len(row) > 1:
            raise ValueError(f'Multiple substances available for {formula}. '
                             'Include CAS number with input parameters.')
        elif len(row) == 0:
            raise ValueError(f'Formula {formula} not found')

    formula = row['Formula'].iloc[0]
    name = row['Name'].iloc[0]
    cas = row['CAS'].iloc[0]
    tmin = row['Tmin'].iloc[0]
    tmax = row['Tmax'].iloc[0]
    a = row['A'].iloc[0]
    b = row['B'].iloc[0]
    c = row['C'].iloc[0]
    d = row['D'].iloc[0]
    k = a + b * temp + c * (temp**2) + d * (temp**3)

    if temp < tmin or temp > tmax:
        raise ValueError('Temperature out of range. Applicable values are '
                         f'{tmin}-{tmax} K for {formula} gas.')

    if disp:
        print('Formula       ', formula)
        print('Name          ', name)
        print('CAS           ', cas)
        print('Min Temp. (K) ', tmin)
        print('Max Temp. (K) ', tmax)
        print('A             ', a)
        print('B             ', b)
        print('C             ', c)
        print('D             ', d)
        print('k      (W/m⋅K)', k)

    return k
