def rhog(mw, p, tk):
    """
    Calculate gas density from molecular weight, pressure, and temperature.

    Parameters
    ----------
    mw : float
        Molecular weight of gas [g/mol]
    p : float
        Pressure of the gas [Pa]
    tk : float
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
    r = 8.3145      # ideal gas constant in units of (m^3 Pa)/(K mol)
    rho = (p * mw) / (r * tk)
    return rho
