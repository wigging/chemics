import numpy as np


def devol_time(dp, tbed):
    """
    Correlation for 95% devolatilization time for wood particles. Refer to
    Equation 2 in the Di Blasi [1]_ article which is based on beech wood
    cylinders in a fluidized sand bed.

    Parameters
    ----------
    dp : float or array
        Diameter of biomass particle [mm]
    tbed : float or array
        Bed temperature [K]

    Returns
    -------
    tv : float or array
        Devolatilization time for 95% conversion [s]

    Example
    -------
    >>> devol_time(2.0, 773.15)
    13.2114

    References
    ----------
    .. [1] Colomba Di Blasi and Carmen Branca. Temperatures of Wood Particles
       in a Hot Sand Bed Fluidized by Nitrogen. Energy and Fuels, 17,
       pp. 247-254, 2003.
    """
    tv = 0.8 * np.exp(1525 / tbed) * (dp**1.2)
    return tv
