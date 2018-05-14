"""
Constants
"""


def archimedes(dp, rhog, rhos, mug):
    """
    Archimedes number as a dimensionless constant.

    Parameters
    ----------
    dp = diameter of particle, m
    rhos = density of solid particle, kg/m^3
    rhog = density of gas, kg/m^3
    mug = viscosity of gas, kg/(m s)

    Returns
    -------
    Ar = Archimedes number, (-)
    """
    g = 9.81    # gravitational constant, m/s^2
    Ar = ((dp**3)*rhog*(rhos-rhog)*g)/(mug**2)
    return Ar
