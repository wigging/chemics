"""
Class for gas mixture properties.
"""

import numpy as np


class GasMixture:
    """
    Gas mixture class.

    Parameters
    ----------
    gases : list of Gas objects
        Gas objects representing each component of the gas mixture.
    mole_fractions : list
        Mole fraction of each gas component.

    Attributes
    ----------
    molecular_weights : list of float
        Molecular weight of each gas component in g/mol.
    viscosities : list of float
        Viscosity of each gas component in microPoise (μP).
    mole_fractions : list of float
        Mole fraction of each gas component.

    Raises
    ------
    ValueError
        If sum of mole fractions does not equal 1.
    """

    def __init__(self, gases, mole_fractions):
        if not np.isclose(sum(mole_fractions), 1.0):
            raise ValueError("Sum of mole fractions must be 1")

        n = len(gases)
        molecular_weights = np.zeros(n)
        viscosities = np.zeros(n)

        for i, gas in enumerate(gases):
            mw = gas.molecular_weight
            mu = gas.viscosity()
            molecular_weights[i] = mw
            viscosities[i] = mu

        self.molecular_weights = molecular_weights
        self.viscosities = viscosities
        self.mole_fractions = np.asarray(mole_fractions)

    def molecular_weight(self):
        """
        Calculate molecular weight of the gas mixture as a weighted mean.

        Returns
        -------
        mw_mixture : float
            Molecular weight of the gas mixture in g/mol.

        Examples
        --------
        >>> gas1 = cm.Gas('H2', 773)
        >>> gas2 = cm.Gas('N2', 773)
        >>> gas_mixture = cm.GasMixture([gas1, gas2], [0.8, 0.2])
        >>> gas_mixture.molecular_weight()
        7.2156...
        """
        mw_gases = self.molecular_weights
        x_gases = self.mole_fractions
        mw_mixture = np.average(mw_gases, weights=x_gases)
        return mw_mixture

    def viscosity(self, method="graham"):
        r"""
        Gas mixture viscosity.

        Calculate viscosity of the gas mixture using Graham's method [1]_ or
        the Herning and Zipperer method [2]_. For the Graham method, Equation
        1 from the Davidson report [3]_ is used

        .. math:: \mu_{mix} = \sum (x_i \cdot \mu_i)

        where :math:`\mu_{mix}` is viscosity of the gas mixture, :math:`x_i`
        is mole fraction [-] of each component, and :math:`\mu_i` is gas
        viscosity of each component. For the Herning and Zipperer method,
        Equation 1 from the Davidson report is used

        .. math::

           \mu_{mix} = \frac{\sum (\mu_i \cdot x_i \cdot \sqrt{MW_i})}{\sum (x_i \cdot \sqrt{MW_i})}

        where :math:`\mu_{mix}` is viscosity of the gas mixture, :math:`x_i`
        is mole fraction [-] of each component, :math:`\mu_i` is gas
        viscosity of each component, and :math:`MW_i` is the molecular
        weight [g/mol] of each gas component.

        Parameters
        ----------
        method : str
            Method for calculating the gas mixture viscosity, choose graham or
            herning. Default value is graham.

        Returns
        -------
        mu_mixture : float
            Viscosity of the gas mixture in units of microPoise (μP).

        Examples
        --------
        >>> gas1 = cm.Gas('H2', 773)
        >>> gas2 = cm.Gas('N2', 773)
        >>> gas_mixture = cm.GasMixture([gas1, gas2], [0.85, 0.15])
        >>> gas_mixture.viscosity()
        207.34...

        >>> gas1 = cm.Gas('H2', 773)
        >>> gas2 = cm.Gas('N2', 773)
        >>> gas_mixture = cm.GasMixture([gas1, gas2], [0.85, 0.15])
        >>> gas_mixture.viscosity(method='herning')
        252.78...

        References
        ----------
        .. [1] Thomas Graham. On the Motion of Gases. Philosophical Transactions of
           the Royal Society of London, vol. 136, pp. 573-631, 1846.
        .. [2] F. Herning and L. Zipperer. Calculation of the Viscosity of
           Technical Gas Mixtures From the Viscosity of the Individual Gases.
           Gas-und Wasserfach, vol. 79, pp. 69-73, 1936.
        .. [3] Thomas Davidson. A Simple and Accurate Method for Calculating
           Viscosity of Gaseous Mixtures. United States Department of the Interior:
           Report of Investigations 9456, 1993.
        """
        mw_gases = self.molecular_weights
        mu_gases = self.viscosities
        x_gases = self.mole_fractions

        if method == "graham":
            mu_mixture = np.sum(mu_gases * x_gases)
        elif method == "herning":
            mu_mixture = np.sum(mu_gases * x_gases * np.sqrt(mw_gases)) / np.sum(
                x_gases * np.sqrt(mw_gases)
            )
        else:
            raise ValueError("Method not available. Choose graham or herning.")

        return mu_mixture
