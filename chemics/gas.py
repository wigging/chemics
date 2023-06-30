import pandas as pd
from pathlib import Path
from .molecular_weight import mw


class Gas:
    """
    Gas properties class.

    Parameters
    ----------
    formula : str
        Molecular formula of the gas
    cas : str, optional
        CAS (Chemical Abstracts Service) number of the gas, may be required
        for some species

    Attributes
    ----------
    formula : str
        Molecular formula of the gas
    cas : str
        CAS number of the gas
    mw : float
        Molecular weight of the gas [g/mol]
    """

    def __init__(self, formula, cas=None):
        self.formula = formula
        self.cas = cas
        self.mw = mw(formula)

    def density(self, press, temp):
        """
        Calculate gas density using the molecular weight, pressure, and
        temperature of the gas.

        Parameters
        ----------
        press : float
            Pressure of the gas [Pa]
        temp : float
            Temperature of the gas [K]

        Returns
        -------
        rho : float
            Density of the gas [kg/m^3]

        Examples
        --------
        >>> import chemics as cm
        >>> gas = cm.Gas('N2')
        >>> gas.density(101325, 773)
        0.4416
        """
        mw = self.mw / 1000  # convert g/mol to kg/mol
        r = 8.3145  # ideal gas constant in units of (m^3 Pa)/(K mol)
        rho = (press * mw) / (r * temp)
        return rho

    def heat_capacity(self, temp, disp=False):
        """
        Calculate gas heat capacity as a function of temperature using Yaws'
        coefficients [1]_. The CAS (Chemical Abstracts Service) number may be
        required for some species.

        .. math:: C_p = A + B\\,T + C\\,T^2 + D\\,T^3 + E\\,T^4 + F\\,T^5 + G\\,T^6

        Parameters
        ----------
        temp : float
            Temperature of the gas [K]
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
            Heat capacity of the gas [J/(mol⋅K)]

        Examples
        --------
        >>> import chemics as cm
        >>> gas = cm.Gas('CBrClF2')
        >>> gas.heat_capacity(700)
        97.4982

        >>> gas = cm.Gas('C5H10O2', cas='75-98-9')
        >>> gas.heat_capacity(850)
        268.4920

        >>> gas = cm.Gas('NO2')
        >>> gas.heat_capacity(900)
        51.0686

        References
        ----------
        .. [1] Carl L. Yaws. Heat capacity of gas Tables 39 and 40 in Yaws'
           Critical Property Data for Chemical Engineers and Chemists. Published
           by Knovel, 2014.
        """
        formula = self.formula
        cas = self.cas

        path = Path(__file__).parent.absolute()
        df = pd.read_csv(path / 'data/gas-cp-yaws.csv')

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

    def thermal_conductivity(self, temp, cas=None, disp=False):
        """
        Calculate gas thermal conductivity as a function of temperature using
        Yaws' coefficients [2]_. The CAS (Chemical Abstracts Service) number
        may be required for some species.

        Parameters
        ----------
        temp : float
            Temperature of the gas [K]
        cas : str, optional
            CAS number of the gas, required for some species
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
            Thermal conductivity of the gas [W/m⋅K]

        Examples
        --------
        >>> import chemics as cm
        >>> gas = cm.Gas('N2')
        >>> gas.thermal_conductivity(773)
        0.0535

        >>> gas = cm.Gas('C18H38O')
        >>> gas.thermal_conductivity(920, cas='593-32-8')
        0.0417

        >>> gas = cm.Gas('N2')
        >>> gas.thermal_conductivity(773, disp=True)
        Formula        N2
        Name           nitrogen
        CAS            7727-37-9
        Min Temp. (K)  63.15
        Max Temp. (K)  1500.0
        A              -0.000226779433664
        B              0.0001027462918646
        C              -6.015141955845571e-08
        D              2.2331907127430105e-11
        k (W/m⋅K)      0.05356876932986771
        0.05356876932986771

        References
        ----------
        .. [2] Carl L. Yaws. Thermal Conductivity Gas Tables 84 and 85 in Yaws'
           Critical Property Data for Chemical Engineers and Chemists. Published
           by Knovel, 2014.
        """
        formula = self.formula

        path = Path(__file__).parent.absolute()
        df = pd.read_csv(path / 'data/gas-k-yaws.csv')

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
            print('k (W/m⋅K)     ', k)

        return k

    def viscosity(self, temp, *, method, cas=None, disp=False):
        """
        Gas viscosity as a function of temperature using Ludwig's coefficients
        [3]_ or Yaws' coefficients [4]_. The CAS (Chemical Abstracts Service)
        number may be required for some species.

        .. math:: \\mu = A + B\\,T + C\\,T^2

        Parameters
        ----------
        temp : float
            Gas temperature [K]
        method : str
            Method for determining coefficients, choose yaws or ludwig.
        cas : str, optional
            CAS number of the gas, required for some species.
        disp : bool
            Display information about the calculation such as the applicable
            temperature range in Kelvin and values for regression
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
        mu : float
            Gas viscosity [microPoise]

        Examples
        --------
        >>> import chemics as cm
        >>> gas = cm.Gas('CH4')
        >>> gas.viscosity(810, method='yaws')
        234.21

        >>> gas = cm.Gas('C2Cl2F4')
        >>> gas.viscosity(900, method='yaws', cas='374-07-2')
        314.90

        >>> gas = cm.Gas('H2')
        >>> gas.viscosity(404, method='yaws')
        113.18

        >>> gas = cm.Gas('N2')
        >>> gas.viscosity(773, method='yaws', disp=True)
        Formula        N2
        Name           nitrogen
        CAS            7727-37-9
        Min Temp. (K)  63.15
        Max Temp. (K)  1970.0
        A              4.46555763078484
        B              0.638137789753159
        C              -0.0002659562785407
        D              5.41126875437814e-08
        μ (microPoise) 363.8235847080749
        363.8235847080749

        >>> gas = cm.Gas('NH3')
        >>> gas.viscosity(850, method='ludwig')
        300.8464

        >>> gas = cm.Gas('C2H4O')
        >>> gas.viscosity(920, method='ludwig', cas='75-07-0')
        242.4685

        References
        ----------
        .. [3] A. Kayode Coker. Table C-2 Viscosity of Gas in Ludwig's Applied
           Process Design for Chemical and Petrochemical Plants, Volume 2, 4th
           Edition. Elsevier, 2010.
        .. [4] Carl L. Yaws. Viscosity Gas Tables 80 and 81 in Yaws' Critical
           Property Data for Chemical Engineers and Chemists. Published by Knovel,
           2014.
        """
        formula = self.formula

        path = Path(__file__).parent.absolute()

        if method == 'yaws':
            df = pd.read_csv(path / 'data/gas-viscosity-yaws.csv')
        elif method == 'ludwig':
            df = pd.read_csv(path / 'data/gas-viscosity-ludwig.csv')
        else:
            raise ValueError('Method not available. Choose yaws or ludwig.')

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

        if method == 'yaws':
            formula = row['Formula'].iloc[0]
            name = row['Name'].iloc[0]
            cas = row['CAS'].iloc[0]
            tmin = row['Tmin'].iloc[0]
            tmax = row['Tmax'].iloc[0]
            a = row['A'].iloc[0]
            b = row['B'].iloc[0]
            c = row['C'].iloc[0]
            d = row['D'].iloc[0]
            mu = a + b * temp + c * (temp**2) + d * (temp**3)

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
                print('μ (microPoise)', mu)
        elif method == 'ludwig':
            formula = row['Formula'].iloc[0]
            name = row['Name'].iloc[0]
            tmin = row['Tmin'].iloc[0]
            tmax = row['Tmax'].iloc[0]
            a = row['A'].iloc[0]
            b = row['B'].iloc[0]
            c = row['C'].iloc[0]
            mu = a + (b * temp) + (c * temp**2)

            if temp < tmin or temp > tmax:
                raise ValueError('Temperature out of range. Applicable values are '
                                 f'{tmin}-{tmax} K for {formula} gas.')

            if disp:
                print('Formula       ', formula)
                print('Name          ', name)
                print('Min Temp. (K) ', tmin)
                print('Max Temp. (K) ', tmax)
                print('A             ', a)
                print('B             ', b)
                print('C             ', c)
                print('μ (microPoise)', mu)

        return mu
