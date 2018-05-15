"""
Minimum fluidization velocity
-----------------------------

Description goes here.
"""

import numpy as np


def umfWenYu(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, according to the Wen and Yu
    coefficients. See pages 69, 70, Table 4 in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    a1 = 33.7       # a1 coefficient, (-)
    a2 = 0.0408     # a2 coefficient, (-)
    g = 9.81        # gravity, m/s^2

    # Ar = Archimedes number, (-)
    # Re = Reynolds number, (-)
    # umf = minimum fluidization velocity, m/s
    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug) / (dp * rhog)
    return umf


def umfRich(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, from the Richardson
    coefficients. See pages 69, 70, Table 4 in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    a1 = 25.7       # a1 coefficient, (-)
    a2 = 0.0365     # a2 coefficient, (-)
    g = 9.81        # gravity, m/s^2

    # Ar = Archimedes number, (-)
    # Re = Reynolds number, (-)
    # umf = minimum fluidization velocity, m/s
    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug) / (dp * rhog)
    return umf


def umfSaxVog(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, from the Saxena and Vogel
    coefficients. See pages 69, 70, Table 4 in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    a1 = 25.3       # a1 coefficient, (-)
    a2 = 0.0571     # a2 coefficient, (-)
    g = 9.81        # gravity, m/s^2

    Ar = (g*dp**3*rhog*(rhop-rhog)) / (ug**2)   # Ar = Archimedes number, (-)
    Re = (a1**2 + a2 * Ar)**0.5 - a1            # Re = Reynolds number, (-)
    umf = (Re * ug)/(dp * rhog)             # minimum fluidization velocity, m/s
    return umf


def umfBabu(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, using the Babu coefficients.
    See pages 69, 70, Table 4 in the Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    a1 = 25.3       # a1 coefficient, (-)
    a2 = 0.0651     # a2 coefficient, (-)
    g = 9.81        # gravity, m/s^2

    Ar = (g*dp**3*rhog*(rhop-rhog)) / (ug**2)   # Ar = Archimedes number, (-)
    Re = (a1**2 + a2 * Ar)**0.5 - a1            # Re = Reynolds number, (-)
    umf = (Re * ug)/(dp * rhog)             # minimum fluidization velocity, m/s
    return umf


def umfGrace(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, using the Grace coefficients.
    See pages 69, 70, Table 4 in the Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    a1 = 27.2       # a1 coefficient, (-)
    a2 = 0.0408     # a2 coefficient, (-)
    g = 9.81        # gravity, m/s^2

    Ar = (g*dp**3*rhog*(rhop-rhog)) / (ug**2)   # Ar = Archimedes number, (-)
    Re = (a1**2 + a2 * Ar)**0.5 - a1            # Re = Reynolds number, (-)
    umf = (Re * ug)/(dp * rhog)             # minimum fluidization velocity, m/s
    return umf


def umfChit(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, according to the Chitester
    coefficients. See pages 69, 70, Table 4 in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    a1 = 28.7       # a1 coefficient, (-)
    a2 = 0.0494     # a2 coefficient, (-)
    g = 9.81        # gravity, m/s^2

    Ar = (g*dp**3*rhog*(rhop-rhog)) / (ug**2)   # Ar = Archimedes number, (-)
    Re = (a1**2 + a2 * Ar)**0.5 - a1            # Re = Reynolds number, (-)
    umf = (Re * ug)/(dp * rhog)             # minimum fluidization velocity, m/s
    return umf


def umfErgun(dp, ep, phi, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, based on the Ergun equation.
    See pages 69 and 70 in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    ep : float
        Void fraction [-]
    phi : float
        Sphericity of bed particle [-]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    g = 9.81                                # gravity, m/s^2
    K1 = 1.75 / (ep**3 * phi)               # K1 term, (-)
    K2 = 150*(1 - ep) / (ep**3 * phi**2)    # K2 term, (-)
    a = K2/(2*K1)                           # a term, (-)
    b = 1/K1                                # b term, (-)

    Ar = ((dp**3)*rhog*(rhop-rhog)*g) / (ug**2)     # Ar = Archimedes number, (-)
    Re = ((a**2 + b*Ar)**0.5) - a                   # Re = Reynolds number, (-)
    umf = (Re * ug) / (rhog * dp)       # minimum fluidization velocity, m/s
    return umf


def umfLargeRe(dp, ep, phi, rhog, rhop):
    """
    Calculate minimum fluidization velocity, Umf, for large Reynolds number
    where Re > 1000. See pages 70, equation 22, in Kunii and Levenspiel 1991
    book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    ep : float
        Void fraction [-]
    phi : float
        Sphericity of bed particle [-]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    g = 9.81    # gravity, m/s^2
    umf = np.sqrt((dp * (rhop - rhog) * g * ep**3 * phi) / (1.75 * rhog))
    return umf


def umfSmallRe(dp, ep, phi, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, for small Reynolds number
    where Re < 20. See page 69, equation 21, in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    ep : float
        Void fraction [-]
    phi : float
        Sphericity of bed particle [-]
    rhog : float
        Density of gas [kg/m^3]
    rhop : float
        Density of bed particle [kg/m^3]
    ug : float
        Viscosity of gas [kg/ms]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]
    """
    g = 9.81    # gravity, m/s^2
    umf = ((dp**2*(rhop-rhog)*g)/(150 * ug)) * ((ep**3 * phi**2) / (1 - ep))
    return umf
