
def prandtl(cp, mu, k):
    """
    Calculate the dimensionless Prandtl number.

    Parameters
    ----------
    cp : float
        Specific heat, J/(kg⋅K)
    mu : float
        Dynamic viscosity, kg/(m⋅s)
    k : float
        Thermal conductivity, W/(m⋅K)

    Returns
    -------
    pr : float
        Prandtl number

    Example
    -------
    >>> cp = 4188; mu = 0.001307; k = 0.5674
    >>> prandtl(cp, mu, k)
    9.647
    """
    pr = (cp * mu) / k

    return pr
