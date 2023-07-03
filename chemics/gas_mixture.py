import numpy as np


class GasMixture:
    """
    Gas mixture class.

    Parameters
    ----------
    mus : list, tuple, or array
        Viscosity of each gas component.
    xs : list, tuple, or array
        Mole fraction of each gas component.
    mws : optional list, tuple, or array
        Molecular weight of each gas component [g/mol].

    Attributes
    ----------
    mus : list, tuple, or array
        Viscosity of each gas component.
    xs : list, tuple, or array
        Mole fraction of each gas component.
    mws : optional list, tuple, or array
        Molecular weight of each gas component [g/mol].

    Raises
    ------
    ValueError
        If sum of mole fractions does not equal one.
    """

    def __init__(self, mus, xs, mws=None):
        self.mus = np.asarray(mus)
        self.xs = np.asarray(xs)
        self.mws = np.asarray(mws)

        if not np.isclose(self.xs.sum(), 1.0):
            raise ValueError('Sum of mole fractions must be one.')

    def viscosity(self, *, method):
        """
        Gas mixture viscosity using Graham's method [1]_ or the Herning and
        Zipperer method [2]_. For the Graham method, Equation 1 from the Davidson
        report [3]_ is used

        .. math:: \\mu_{mix} = \\sum (x_i \\cdot \\mu_i)

        where :math:`\\mu_{mix}` is viscosity of the gas mixture, :math:`x_i`
        is mole fraction [-] of each component, and :math:`\\mu_i` is gas
        viscosity of each component. For the Herning and Zipperer method,
        Equation 1 form the Davidson report is used

        .. math:: \\mu_{mix} = \\frac{\\sum (\\mu_i \\cdot x_i \\cdot \\sqrt{MW_i})}{\\sum (x_i \\cdot \\sqrt{MW_i})}

        where :math:`\\mu_{mix}` is viscosity of the gas mixture, :math:`x_i`
        is mole fraction [-] of each component, :math:`\\mu_i` is gas
        viscosity of each component, and :math:`MW_i` is the molecular
        weight [g/mol] of each gas component.

        Parameters
        ----------
        method : str
            Method for calculating the gas mixture viscosity, choose graham or
            herning.

        Returns
        -------
        mu_mix : float
            Gas mixture viscosity. Units are same as input viscosity.

        Example
        -------
        >>> import chemics as cm

        >>> gas1 = cm.Gas('H2')
        ... mu1 = gas1.viscosity(773.15, method='yaws')

        >>> gas2 = cm.Gas('N2')
        ... mu2 = gas2.viscosity(773.15, method='yaws')

        >>> mus = [mu1, mu2]
        ... xs = [0.85, 0.15]
        ... gasmix = cm.GasMixture(mus, xs)
        ... gasmix.viscosity(method='graham')
        207.37

        >>> gas1 = cm.Gas('H2')
        ... mw1 = gas1.mw
        ... mu1 = gas1.viscosity(773.15, method='yaws')

        >>> gas2 = cm.Gas('N2')
        ... mw2 = gas2.mw
        ... mu2 = gas2.viscosity(773.15, method='yaws')

        >>> mus = [mu1, mu2]
        ... xs = [0.85, 0.15]
        ... mws = [mw1, mw2]
        ... gasmix = cm.GasMixture(mus, xs, mws)
        ... gasmix.viscosity(method='herning')
        252.81

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
        mus = self.mus
        xs = self.xs
        mws = self.mws

        if method == 'graham':
            mu_mix = np.sum(mus * xs)
        elif method == 'herning':
            mu_mix = np.sum(mus * xs * np.sqrt(mws)) / np.sum(xs * np.sqrt(mws))
        else:
            raise ValueError('Method not available. Choose graham or herning.')

        return mu_mix
