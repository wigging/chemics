import numpy as np


def ubr_holland(db, rho_l, rho_g, sig, mu_l):
    """
    Bubble rise velocity in a liquid for a range of applicability. This
    velocity is related to the terminal rise velocity correlations for a
    single bubble in a liquid as given in Table 7.1 in the Holland and Bragg
    book [1]_.

    Parameters
    ----------
    db : float
        Diameter of sphere having same volume as spherical cap bubble,
        referred to as the effective bubble diameter [m]
    rho_l : float
        Density of the liquid [kg/m^3]
    rho_g : float
        Density of the gas [kg/m^3]
    sig : float
        Surface tension [dynes/cm]
    mu_l : float
        Dynamic viscosity of the liquid [centiPoise]

    Returns
    -------
    ub : float
        Bubble (terminal) rise velocity [m/s]

    Example
    -------
    >>> ubr_holland(0.00003, 998, 0, 72.75, 1.21)
    0.0004046

    References
    ----------
    .. [1] F.A. Holland and R. Bragg. Fluid Flow for Chemical Engineers.
           Butterworth-Heinemann, 2nd edition, p. 234, 1995.
    """

    # Constants
    g = 9.81    # acceleration due to gravity [m/s^2]

    # Convert all given parameters to mks units
    r_b_mks = db / 2        # [m]
    sig_mks = sig / 1000    # [N/m]
    mu_l_mks = mu_l / 1000  # [Pa s]

    # bubble Reynolds number [-]
    def Re(ub):
        return 2 * rho_l * ub * r_b_mks / mu_l_mks

    # Morton Number [-]
    G1 = (g * mu_l_mks**4) / (rho_l * sig_mks**3)

    # Region 1: Bubbles behave as bouyant spheres, rising vertically.
    ub = (2 * (r_b_mks**2) * (rho_l - rho_g) * g) / (9 * mu_l_mks)

    if Re(ub) <= 2:
        return ub

    # Region 2: Bubbles raise as spheres, but the drag coefficient slightly
    #           less than that of a solids of the same volume.
    ub = 0.33 * (g**0.76) * ((rho_l / mu_l_mks)**0.52) * (r_b_mks**1.28)

    if Re(ub) > 2 and Re(ub) <= 4.02 * (G1**-0.214):
        return ub

    # Region 3: Bubbles are flattened and rise in zig-zag pattern.
    ub = 1.35 * (sig_mks / (rho_l * r_b_mks))**0.5

    if Re(ub) > 4.02 * (G1**-0.214) and Re(ub) <= 3.10 * (G1**-0.25):
        return ub

    # Region 4: Bubbles rise vertically adopting a mushroom-cap shape.
    ub = 1.18 * ((sig * g / rho_l)**0.25)

    if Re(ub) > 3.10 * G1**-0.25 and Re(ub) <= 2.3 * (sig / (g * rho_l))**0.5:
        return ub

    # Region 5: Large spherical-cap bubbles.
    ub = (g * r_b_mks)**0.5

    return ub


def ubr_kunii(db, dt):
    """
    Rise velocity of single bubbles in a fluidized bed from Equations 5.3 and
    5.4 in Kunii and Levenspiel book [2]_.

    Parameters
    ----------
    db : float
        Diameter of sphere having same volume as spherical cap bubble,
        referred to as the effective bubble diameter [m]
    dt : float
        Bed or tube diameter [m]

    Returns
    -------
    ubr : float
        Rise velocity of single bubbles in fluidized bed [m/s]

    Example
    -------
    >>> ubr_kunii(0.05, 0.6)
    0.4979

    References
    ----------
    .. [2] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
           Butterworth-Heinemann, 2nd edition, 1991.
    """
    g = 9.81    # acceleration of gravity [m/s^2]

    if db / dt < 0.125:
        ubr = 0.711 * (g * db)**(1 / 2)
    elif 0.125 <= db / dt < 0.6:
        ubr = (0.711 * (g * db)**(1 / 2)) * 1.2 * np.exp(-1.49 * db / dt)
    else:
        raise ValueError('Bed is considered slugging at db/dt > 0.6')

    return ubr
