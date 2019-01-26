
def fbexp(db, dp, rhog, rhos, umf, us):
    """
    Bed expansion factor for calculating expanded bed height of a bubbling
    fluidized bed reactor. See equations 14.7 and 14.8 in Souza-Santos [1]_.

    Parameters
    ----------
    db : float
        Diameter of the bed [m]
    dp : float
        Diameter of the bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhos : float
        Density of bed particle [kg/m^3]
    umf : float
        Minimum fluidization velocity [m/s]
    us : float
        Superficial gas velocity [m/s]

    Returns
    -------
    fbx : float
        Bed expansion factor [-]

    Example
    -------
    >>> umf = 0.1157
    ... us = 3.0*umf
    ... fbexp(0.05232, 0.0004, 0.4413, 2500, 0.1157, us)
    1.4864

    References
    ----------
    .. [1] Marcio de Souza-Santos. Solid Fuels Combustion and Gasification:
       Modeling, Simulation, and Equipment Operations. CRC Press, Taylor and
       Francis Group, 2nd edition, 2010.
    """

    if db < 0.0635:
        # diameter of bed as db < 0.0635 m from Eq 14.7
        tm1 = 1.032 * ((us - umf)**0.57) * (rhog**0.083)
        tm2 = (rhos**0.166) * (umf**0.063) * (db**0.445)
        fbx = 1 + (tm1 / tm2)
    else:
        # diameter of bed as db >= 0.0635 m from Eq 14.8
        tm1 = 14.314 * ((us - umf)**0.738) * (dp**1.006) * (rhos**0.376)
        tm2 = (rhog**0.126) * (umf**0.937)
        fbx = 1 + (tm1 / tm2)

    return fbx
