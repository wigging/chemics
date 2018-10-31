import numpy as np


def patm(alt):
    """
    Determine atmospheric pressure at altitudes up to 51 km. Based on article
    by Roland Stull [#stull]_.

    Parameters
    ----------
    alt : float
        Altitude or elevation above sea level [m]

    Returns
    -------
    Patm : float
        Atmospheric pressure [Pa]

    References
    ----------
    .. [#stull] Practical Meteorology: An Algebra-based Survey of Atmospheric
       Science by Roland Stull.
    """
    alt = alt/1000              # convert altitude from meters to kilometers
    Ro = 6356.766               # average radius of the Earth, km
    H = (Ro * alt)/(Ro + alt)   # geopotential height, km

    Patm = None     # initiate pressure variable

    if H <= 11:
        T = 288.15 - (6.5 * H)
        Patm = 101325 * (288.15 / T) ** (-5.255877)
    elif H <= 20:
        T = 216.65
        Patm = 22632 * np.exp(-0.1577 * (H - 11))
    elif H <= 32:
        T = 216.65 + (H - 20)
        Patm = 5474.9 * (216.65 / T) ** (34.16319)
    elif H <= 47:
        T = 228.65 + 2.8 * (H - 32)
        Patm = 868 * (228.65 / T) ** 12.2011
    elif H <= 51:
        T = 270.65
        Patm = 110.9 * np.exp(-0.1262 * (H - 47))
    else:
        raise ValueError('geopotential height must be less than 51 km')

    # return atmospheric pressure at altitude, Pa
    return Patm
