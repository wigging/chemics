import numpy as np


def ubr(db, dt):
    """
    Rise velocity of single bubbles in a fluidized bed from Equations 5.3 and
    5.4 in Kunii and Levenspiel book [1]_.

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
    >>> ubr(0.05, 0.6)
    0.4979

    References
    ----------
    .. [1] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
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
