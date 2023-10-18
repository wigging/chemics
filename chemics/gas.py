import pandas as pd
from pathlib import Path

from .molecular_weight import mw


class Gas:
    """
    Gas properties class.

    Parameters
    ----------
    formula : str
        Molecular formula of the gas.
    cas : str, optional
        CAS (Chemical Abstracts Service) number of the gas, may be required
        for some species.

    Attributes
    ----------
    formula : str
        Molecular formula of the gas
    cas : str
        CAS number of the gas
    mw : float
        Molecular weight of the gas in g/mol
    """

    def __init__(self, formula, cas=None):
        self.formula = formula
        self.cas = cas
        self.mw = mw(formula)

        # Store viscosity coefficients after first execution. This prevents
        # lookup time for subsequent executions of the viscosity() method.
        self._coeff_yaws = None
        self._coeff_ludwig = None

    def density(self, press, temp):
        """
        Calculate gas density using the molecular weight, pressure, and
        temperature of the gas.

        Parameters
        ----------
        press : float
            Pressure of the gas in pascal
        temp : float
            Temperature of the gas in Kelvin

        Returns
        -------
        rho : float
            Density of the gas in kg/m\\ :sup:`3`

        Examples
        --------
        >>> gas = cm.Gas('N2')
        >>> gas.density(101325, 773)
        0.4416
        """
        mw = self.mw / 1000  # convert g/mol to kg/mol
        r = 8.3145           # ideal gas constant in units of (m^3 Pa)/(K mol)
        rho = (press * mw) / (r * temp)
        return rho

    def heat_capacity(self, temp):
        """
        Calculate gas heat capacity as a function of temperature using Yaws'
        coefficients [1]_. The CAS (Chemical Abstracts Service) number may be
        required for some species.

        .. math:: C_p = A + B\\,T + C\\,T^2 + D\\,T^3 + E\\,T^4 + F\\,T^5 + G\\,T^6

        Parameters
        ----------
        temp : float
            Temperature of the gas in Kelvin

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
            Heat capacity of the gas in J/(mol⋅K)

        Examples
        --------
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
        path = Path(__file__).parent.absolute()
        df = pd.read_csv(path / 'data/gas-cp-yaws.csv')

        if self.cas:
            row = df.query(f"CAS == '{self.cas}'")
            if len(row) == 0:
                raise ValueError(f'CAS number {self.cas} not found')
        else:
            row = df.query(f"Formula == '{self.formula}'")
            if len(row) > 1:
                raise ValueError(f'Multiple substances available for {self.formula}. '
                                 'Include CAS number with input parameters.')
            elif len(row) == 0:
                raise ValueError(f'Formula {self.formula} not found')

        tmin = row['Tmin'].iloc[0]
        tmax = row['Tmax'].iloc[0]

        if temp < tmin or temp > tmax:
            raise ValueError('Temperature out of range. Applicable values are '
                             f'{tmin}-{tmax} K for {self.formula} gas.')

        a = row['A'].iloc[0]
        b = row['B'].iloc[0]
        c = row['C'].iloc[0]
        d = row['D'].iloc[0]
        e = row['E'].iloc[0]
        f = row['F'].iloc[0]
        g = row['G'].iloc[0]
        cp = a + (b * temp) + (c * temp**2) + (d * temp**3) + (e * temp**4) + (f * temp**5) + (g * temp**6)

        return cp

    def thermal_conductivity(self, temp):
        """
        Calculate gas thermal conductivity as a function of temperature using
        Yaws' coefficients [2]_. The CAS (Chemical Abstracts Service) number
        may be required for some species.

        Parameters
        ----------
        temp : float
            Temperature of the gas in Kelvin

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
            Thermal conductivity of the gas in W/(m⋅K)

        Examples
        --------
        >>> gas = cm.Gas('N2')
        >>> gas.thermal_conductivity(773)
        0.0535

        >>> gas = cm.Gas('C18H38O', cas='593-32-8')
        >>> gas.thermal_conductivity(920)
        0.0417

        References
        ----------
        .. [2] Carl L. Yaws. Thermal Conductivity Gas Tables 84 and 85 in Yaws'
           Critical Property Data for Chemical Engineers and Chemists. Published
           by Knovel, 2014.
        """
        path = Path(__file__).parent.absolute()
        df = pd.read_csv(path / 'data/gas-k-yaws.csv')

        if self.cas:
            row = df.query(f"CAS == '{self.cas}'")
            if len(row) == 0:
                raise ValueError(f'CAS number {self.cas} not found')
        else:
            row = df.query(f"Formula == '{self.formula}'")
            if len(row) > 1:
                raise ValueError(f'Multiple substances available for {self.formula}. '
                                 'Include CAS number with input parameters.')
            elif len(row) == 0:
                raise ValueError(f'Formula {self.formula} not found')

        tmin = row['Tmin'].iloc[0]
        tmax = row['Tmax'].iloc[0]

        if temp < tmin or temp > tmax:
            raise ValueError('Temperature out of range. Applicable values are '
                             f'{tmin}-{tmax} K for {self.formula} gas.')

        a = row['A'].iloc[0]
        b = row['B'].iloc[0]
        c = row['C'].iloc[0]
        d = row['D'].iloc[0]
        k = a + (b * temp) + (c * temp**2) + (d * temp**3)

        return k

    def viscosity(self, temp, *, method):
        """
        Gas viscosity as a function of temperature using Ludwig's coefficients
        [3]_ or Yaws' coefficients [4]_. The CAS (Chemical Abstracts Service)
        number may be required for some species.

        .. math:: \\mu = A + B\\,T + C\\,T^2

        Parameters
        ----------
        temp : float
            Gas temperature in Kelvin
        method : str
            Method for determining coefficients, choose yaws or ludwig.

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
            Gas viscosity microPoise

        Examples
        --------
        >>> gas = cm.Gas('CH4')
        >>> gas.viscosity(810, method='yaws')
        234.21

        >>> gas = cm.Gas('C2Cl2F4', cas='374-07-2')
        >>> gas.viscosity(900, method='yaws')
        314.90

        >>> gas = cm.Gas('H2')
        >>> gas.viscosity(404, method='yaws')
        113.18

        >>> gas = cm.Gas('NH3')
        >>> gas.viscosity(850, method='ludwig')
        300.8464

        >>> gas = cm.Gas('C2H4O', cas='75-07-0')
        >>> gas.viscosity(920, method='ludwig')
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

        # Calculate viscosity if coefficients are already available from a
        # previous execution. This avoids lookup time if this method is
        # called multiple times.

        if method == 'yaws' and self._coeff_yaws:
            a, b, c, d = self._coeff_yaws
            mu = a + (b * temp) + (c * temp**2) + (d * temp**3)
            return mu
        elif method == 'ludwig' and self._coeff_ludwig:
            a, b, c = self._coeff_ludwig
            mu = a + (b * temp) + (c * temp**2)
            return mu

        # Lookup coefficients then calculate viscosity.

        path = Path(__file__).parent.absolute()

        if method == 'yaws':
            df = pd.read_csv(path / 'data/gas-viscosity-yaws.csv')
        elif method == 'ludwig':
            df = pd.read_csv(path / 'data/gas-viscosity-ludwig.csv')
        else:
            raise ValueError('Method not available. Choose yaws or ludwig.')

        if self.cas:
            row = df.query(f"CAS == '{self.cas}'")
            if len(row) == 0:
                raise ValueError(f'CAS number {self.cas} not found')
        else:
            row = df.query(f"Formula == '{self.formula}'")
            if len(row) > 1:
                raise ValueError(f'Multiple substances available for {self.formula}. '
                                 'Include CAS number with input parameters.')
            elif len(row) == 0:
                raise ValueError(f'Formula {self.formula} not found')

        tmin = row['Tmin'].iloc[0]
        tmax = row['Tmax'].iloc[0]

        if temp < tmin or temp > tmax:
            raise ValueError('Temperature out of range. Applicable values are '
                             f'{tmin}-{tmax} K for {self.formula} gas.')

        if method == 'yaws':
            a = row['A'].iloc[0]
            b = row['B'].iloc[0]
            c = row['C'].iloc[0]
            d = row['D'].iloc[0]
            self._coeff_yaws = a, b, c, d
            mu = a + b * temp + c * (temp**2) + d * (temp**3)
            return mu
        elif method == 'ludwig':
            a = row['A'].iloc[0]
            b = row['B'].iloc[0]
            c = row['C'].iloc[0]
            self._coeff_ludwig = a, b, c
            mu = a + (b * temp) + (c * temp**2)
            return mu
