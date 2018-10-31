
def rhog(mw, Pgas, Tgas):
    """
    Calculate gas density from molecular weight, pressure, and temperature.

    .. math::
       \\rho = \\frac{P * MW}{R * T}

    Parameters
    ----------
    mw : float
        Molecular weight of gas [g/mol]
    Pgas : float
        Pressure of the gas [Pa]
    Tgas : float
        Temperature of the gas [K]

    Returns
    -------
    rho : float
        Density of gas [kg/m^3]

    Examples
    --------
    >>> rhog(28, 101325, 773)
    0.4414
    """
    mw = mw / 1000  # convert g/mol to kg/mol
    R = 8.3145      # ideal gas constant, (m^3 Pa)/(K mol)
    rho = (Pgas*mw) / (R*Tgas)
    return rho
