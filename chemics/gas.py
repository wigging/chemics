"""
Gas Properties
==============

See doc string and comments in each function for more details.

Functions
---------
k_n2
k_o2
mug_n2
patm
rhog
"""

import numpy as np


def k_n2(T):
    """
    Equation for thermal conductivity of nitrogen gas, N2, as a function of
    temperature based on formula from Yaw's online reference. Valid at
    temperatures from 63-1500 K.

    k_N2 = A + B*T + C*T^2 + D*T^3

    Parameters
    ----------
    T = temperature of N2 gas, K

    Returns
    -------
    k = thermal conductivity of N2 gas, W/mK

    Reference
    ---------
    Yaw's Transport Properties of Chemicals and Hydrocarbons
    """
    A = -0.000226779
    B = 0.000102746
    C = -6.01514e-8
    D = 2.23319E-11
    k = A + B*T + C*(T**2) + D*(T**3)
    return k


def k_o2(T):
    """
    Equation for thermal conductivity of oxygen gas, O2, as a function of
    temperature based on formula from Yaw's online reference. Valid at
    temperatures from 80-2000 K.

    k_O2 = A + B*T + C*T^2 + D*T^3

    Parameters
    ----------
    T = temperature of O2 gas, K

    Returns
    -------
    k = thermal conductivity of O2 gas, W/mK

    Reference
    ---------
    Yaw's Transport Properties of Chemicals and Hydrocarbons
    """
    A = 0.000154746
    B = 9.41534E-05
    C = -2.75292E-08
    D = 5.20693E-12
    k = A + B*T + C*(T**2) + D*(T**3)
    return k


def mug_n2(T):
    """
    Equation for viscosity of nitrogen gas, N2, as a function of temperature.
    Valid at temperatures from 150-1500 K.

    mug_N2 = A + B*T + C*T^2

    Parameter
    ---------
    T = tempreature of gas, K

    Returns
    -------
    mug = viscosity of gas, uP (micropoise)

    Reference
    ---------
    Ludwig's Applied Process Design for Chemical and Petrochemical Plants,
    Volume 1, 4th Edition.
    """
    A = 42.606
    B = 4.75e-1
    C = -9.88e-5
    mug = A + B*T + C*T**2
    return mug


def patm(alt):
    """
    Determine atmospheric pressure at altitudes up to 51 km.

    Parameters
    ----------
    alt = altitude or elevation above sea level, m

    Returns
    -------
    Patm = atmospheric pressure, Pa

    Reference
    ---------
    Practical Meteorology: An Algebra-based Survey of Atmospheric Science by
    Roland Stull.
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


def rhog(mw, Pgas, Tgas):
    """
    Calculate gas density from molecular weight, pressure, and temperature.

    Equation
    --------
    rho = (P * MW) / (R * T)

    Parameters
    ----------
    mw = molecular weight of gas, g/mol
    Pgas = pressure of the gas, Pa
    Tgas = temperature of the gas, K

    Returns
    -------
    rho = density of gas, kg/m^3
    """
    mw = mw / 1000  # convert g/mol to kg/mol
    R = 8.3145      # ideal gas constant, (m^3 Pa)/(K mol)
    rho = (Pgas*mw) / (R*Tgas)
    return rho
