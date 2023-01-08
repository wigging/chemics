import pandas as pd
from pathlib import Path


def cp_yaws(formula, temp, cas=None, disp=False):
    """
    Gas heat capacity as a function of temperature using Yaws' coefficients
    [1]_. The CAS(Chemical Abstracts Service) number may be required for some
    species.

    .. math:: C_p = A + B\\,T + C\\,T^2 + D\\,T^3 + E\\,T^4 + F\\,T^5 + G\\,T^6

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
    cp : float
        Gas heat capacity [J/(mol⋅K)].

    Examples
    --------
    >>> cp_yaws('CBrClF2', 700)
    97.4982

    >>> cp_yaws('C5H10O2', 850, CAS='75-98-9')
    268.4920

    >>> cp_yaws('NO2', 900)
    51.0686

    References
    ----------
    .. [1] Carl L. Yaws. Heat capacity of gas Tables 39 and 40 in Yaws'
       Critical Property Data for Chemical Engineers and Chemists. Published
       by Knovel, 2014.
    """
    path = Path(__file__).parent.absolute()
    df = pd.read_csv(path / 'data/gas-heat-capacity-yaws.csv')

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
    e = row['E'].iloc[0]
    f = row['F'].iloc[0]
    g = row['G'].iloc[0]
    cp = a + (b * temp) + (c * temp**2) + (d * temp**3) + (e * temp**4) + (f * temp**5) + (g * temp**6)

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
        print('E             ', e)
        print('F             ', f)
        print('G             ', g)
        print('Cp (J/mol⋅K)  ', cp)

    return cp
