"""
Class for gas properties.
"""

import pandas as pd
from pathlib import Path

from .molecular_weight import molecular_weight


def _check_temperature(formula, temperature, limits):
    """
    Check that temperature is within the given limits otherwise raise an error.
    """
    tmin = limits[0]
    tmax = limits[1]
    if temperature < tmin or temperature > tmax:
        msg = f"Temperature {temperature} K is out of range {tmin}-{tmax} K for {formula} gas"
        raise ValueError(msg)


def _get_row(csv_file, formula, cas_number):
    """
    Construct path to CSV data file then get row from the dataframe.
    """
    path = Path(__file__).parent.absolute()
    df = pd.read_csv(path / csv_file)

    if cas_number:
        row = df.query(f"CAS == '{cas_number}'")
        if len(row) == 0:
            raise ValueError(f"CAS number {cas_number} not found")
    else:
        row = df.query(f"Formula == '{formula}'")
        if len(row) > 1:
            m = f"Multiple substances available for {formula}. Include CAS number too."
            raise ValueError(m)
        elif len(row) == 0:
            raise ValueError(f"Formula {formula} not found")

    return row


class Gas:
    """
    Gas properties class.

    Parameters
    ----------
    formula : str
        Molecular formula of the gas.
    temperature : float
        Temperature of the gas in kelvin (K).
    pressure : float, optional
        Pressure of the gas in pascal (Pa). Default value is 101,325 Pa for standard atmosphere.
    cas_number : str, optional
        CAS (Chemical Abstracts Service) number of the gas, may be required for some species.

    Attributes
    ----------
    formula : str
        Molecular formula of the gas.
    temperature : float
        Temperature of the gas in kelvin (K).
    pressure : float
        Pressure of the gas in pascal (Pa).
    cas_number : str, optional
        CAS (Chemical Abstracts Service) number of the gas, may be required for some species.
    molecular_weight : float
        Molecular weight of the gas in g/mol.
    """

    def __init__(self, formula, temperature, pressure=101325, cas_number=None):
        self.formula = formula
        self.temperature = temperature
        self.pressure = pressure
        self.cas_number = cas_number
        self.molecular_weight = molecular_weight(formula)

        # State of each correlation stored as a dictionary
        # The state is checked for subsequent runs to avoid lookup time
        # Expects a dictionary such as
        # state = {'method': 'yaws', 'coefficients': (1, 2, 3), 'limits': (200, 6000)}
        self._cp_state = {"method": None, "coefficients": None, "limits": None}
        self._k_state = {"method": None, "coefficients": None, "limits": None}
        self._mu_state = {"method": None, "coefficients": None, "limits": None}

    def density(self):
        r"""
        Gas density.

        Calculate gas density using the molecular weight, pressure, and
        temperature of the gas.

        Returns
        -------
        rho : float
            Density of the gas in kg/m\ :sup:`3`.

        Examples
        --------
        >>> gas = cm.Gas('N2', 773)
        >>> gas.density()
        0.4416...
        """
        mw = self.molecular_weight / 1000  # convert g/mol to kg/mol
        r = 8.3145  # ideal gas constant in (m^3⋅Pa)/(K⋅mol)
        rho = (self.pressure * mw) / (r * self.temperature)
        return rho

    def heat_capacity(self):
        r"""
        Gas heat capacity.

        Calculate gas heat capacity as a function of temperature using Yaws'
        coefficients [1]_. The CAS (Chemical Abstracts Service) number may be
        required for some species.

        .. math:: C_p = A + B\,T + C\,T^2 + D\,T^3 + E\,T^4 + F\,T^5 + G\,T^6

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
            Heat capacity of the gas in J/(mol⋅K).

        Examples
        --------
        >>> gas = cm.Gas('CBrClF2', 700)
        >>> gas.heat_capacity()
        97.4982...

        >>> gas = cm.Gas('C5H10O2', 850, cas_number='75-98-9')
        >>> gas.heat_capacity()
        268.4920...

        >>> gas = cm.Gas('NO2', 900)
        >>> gas.heat_capacity()
        51.0686...

        References
        ----------
        .. [1] Carl L. Yaws. Heat capacity of gas Tables 39 and 40 in Yaws'
           Critical Property Data for Chemical Engineers and Chemists. Published
           by Knovel, 2014.
        """
        # Use coefficients if already set from a previous run
        # This avoids lookup time when method is called multiple times

        if self._cp_state["method"] == "yaws":
            _check_temperature(self.formula, self.temperature, self._cp_state["limits"])
            a, b, c, d, e, f, g = self._cp_state["coefficients"]
            cp = (
                a
                + (b * self.temperature)
                + (c * self.temperature**2)
                + (d * self.temperature**3)
                + (e * self.temperature**4)
                + (f * self.temperature**5)
                + (g * self.temperature**6)
            )
            return cp

        # Lookup coefficients then calculate heat capacity

        row = _get_row("data/gas-cp-yaws.csv", self.formula, self.cas_number)

        tmin = row["Tmin"].iloc[0]
        tmax = row["Tmax"].iloc[0]
        _check_temperature(self.formula, self.temperature, (tmin, tmax))

        a = row["A"].iloc[0]
        b = row["B"].iloc[0]
        c = row["C"].iloc[0]
        d = row["D"].iloc[0]
        e = row["E"].iloc[0]
        f = row["F"].iloc[0]
        g = row["G"].iloc[0]
        cp = (
            a
            + (b * self.temperature)
            + (c * self.temperature**2)
            + (d * self.temperature**3)
            + (e * self.temperature**4)
            + (f * self.temperature**5)
            + (g * self.temperature**6)
        )

        self._cp_state = {
            "method": "yaws",
            "coefficients": (a, b, c, d, e, f, g),
            "limits": (tmin, tmax),
        }

        return cp

    def thermal_conductivity(self):
        """
        Gas thermal conductivity.

        Calculate gas thermal conductivity as a function of temperature using
        Yaws' coefficients [2]_. The CAS (Chemical Abstracts Service) number
        may be required for some species.

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
            Thermal conductivity of the gas in W/(m⋅K).

        Examples
        --------
        >>> gas = cm.Gas('N2', 773)
        >>> gas.thermal_conductivity()
        0.0535...

        >>> gas = cm.Gas('C18H38O', 920, cas_number='593-32-8')
        >>> gas.thermal_conductivity()
        0.0417...

        References
        ----------
        .. [2] Carl L. Yaws. Thermal Conductivity Gas Tables 84 and 85 in Yaws'
           Critical Property Data for Chemical Engineers and Chemists. Published
           by Knovel, 2014.
        """
        # Use coefficients if already set from a previous run
        # This avoids lookup time when method is called multiple times

        if self._k_state["method"] == "yaws":
            _check_temperature(self.formula, self.temperature, self._k_state["limits"])
            a, b, c, d = self._k_state["coefficients"]
            k = a + (b * self.temperature) + (c * self.temperature**2) + (d * self.temperature**3)
            return k

        # Lookup coefficients then calculate thermal conductivity

        row = _get_row("data/gas-k-yaws.csv", self.formula, self.cas_number)

        tmin = row["Tmin"].iloc[0]
        tmax = row["Tmax"].iloc[0]
        _check_temperature(self.formula, self.temperature, (tmin, tmax))

        a = row["A"].iloc[0]
        b = row["B"].iloc[0]
        c = row["C"].iloc[0]
        d = row["D"].iloc[0]
        k = a + (b * self.temperature) + (c * self.temperature**2) + (d * self.temperature**3)

        self._k_state = {"method": "yaws", "coefficients": (a, b, c, d), "limits": (tmin, tmax)}

        return k

    def viscosity(self, method="yaws"):
        r"""
        Gas viscosity.

        Calculate gas viscosity as a function of temperature using Ludwig's
        coefficients [3]_ or Yaws' coefficients [4]_. The CAS
        (Chemical Abstracts Service) number may be required for some
        species.

        The Ludwig coefficients are used with the following correlation

        .. math:: \mu = A + B\,T + C\,T^2

        The Yaws coefficients are used with the following correlation

        .. math:: \mu = A + B\,T + C\,T^2 + D\,T^3

        Parameters
        ----------
        method : str, optional
            Method for determining coefficients, choose yaws or ludwig.
            Default method is yaws.

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
            Gas viscosity in microPoise (μP).

        Examples
        --------
        >>> gas = cm.Gas('CH4', 810)
        >>> gas.viscosity(method='yaws')
        234.21...

        >>> gas = cm.Gas('C2Cl2F4', 900, cas_number='374-07-2')
        >>> gas.viscosity()
        314.90...

        >>> gas = cm.Gas('H2', 404)
        >>> gas.viscosity()
        113.18...

        >>> gas = cm.Gas('NH3', 850)
        >>> gas.viscosity(method='ludwig')
        300.84...

        >>> gas = cm.Gas('C2H4O', 920, cas_number='75-07-0')
        >>> gas.viscosity(method='ludwig')
        242.46...

        References
        ----------
        .. [3] A. Kayode Coker. Table C-2 Viscosity of Gas in Ludwig's Applied
           Process Design for Chemical and Petrochemical Plants, Volume 2, 4th
           Edition. Elsevier, 2010.
        .. [4] Carl L. Yaws. Viscosity Gas Tables 80 and 81 in Yaws' Critical
           Property Data for Chemical Engineers and Chemists. Published by Knovel,
           2014.
        """
        # Use coefficients if already set from a previous run
        # This avoids lookup time when method is called multiple times

        if self._mu_state["method"] == "yaws":
            _check_temperature(self.formula, self.temperature, self._mu_state["limits"])
            a, b, c, d = self._mu_state["coefficients"]
            mu = a + (b * self.temperature) + (c * self.temperature**2) + (d * self.temperature**3)
            return mu

        if self._mu_state["method"] == "ludwig":
            _check_temperature(self.formula, self.temperature, self._mu_state["limits"])
            a, b, c = self._mu_state["coefficients"]
            mu = a + (b * self.temperature) + (c * self.temperature**2)
            return mu

        # Lookup coefficients then calculate viscosity

        if method == "yaws":
            row = _get_row("data/gas-viscosity-yaws.csv", self.formula, self.cas_number)
        elif method == "ludwig":
            row = _get_row("data/gas-viscosity-ludwig.csv", self.formula, self.cas_number)
        else:
            raise ValueError("Method not available. Choose yaws or ludwig.")

        tmin = row["Tmin"].iloc[0]
        tmax = row["Tmax"].iloc[0]
        _check_temperature(self.formula, self.temperature, (tmin, tmax))

        if method == "yaws":
            a = row["A"].iloc[0]
            b = row["B"].iloc[0]
            c = row["C"].iloc[0]
            d = row["D"].iloc[0]
            mu = a + b * self.temperature + c * (self.temperature**2) + d * (self.temperature**3)
            coeffs = a, b, c, d
        elif method == "ludwig":
            a = row["A"].iloc[0]
            b = row["B"].iloc[0]
            c = row["C"].iloc[0]
            mu = a + (b * self.temperature) + (c * self.temperature**2)
            coeffs = a, b, c

        self._mu_state = {"method": method, "coefficients": coeffs, "limits": (tmin, tmax)}

        return mu
