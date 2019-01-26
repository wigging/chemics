import numpy as np


def uch_bifan(ar, dp, gs, rhog):
    """
    Choking velocity from Bi and Fan [1]_, also see Zhang 2015 paper.

    Parameters
    ----------
    ar : float
        Archimedes number [-]
    dp : float
        Diameter of particle [m]
    gs : float
        Solids flux [kg/(s m^2)]
    rhog : float
        Density of gas [kg/m^3]

    Returns
    -------
    uch : float
        Choking velocity [m/s]

    References
    ----------
    .. [1] Bi, Fan, 1991. Regime transitions in gas-solid circulating fluidized
       beds. AIChE Annual Meeting. AIChE, Los Angeles, pp. 17-22, 1991.
    """
    g = 9.81    # gravity constant, m/s^2
    uch = (21.6 * np.sqrt(g * dp) * (gs**0.542) / (rhog**0.542) * ar**0.105)**(1 / (1 + 0.542))
    return uch


def uch_leung(us, ut):
    """
    Choking velocity based on Equation 6 from Leung [2]_. All parameters must
    be in units of ft/s or in units of m/s.

    Parameters
    ----------
    us : float
        Solids velocity [ft/s or m/s]
    ut : float
        Terminal velocity of a single particle [ft/s or m/s]

    Returns
    -------
    uch : float
        Choking velocity [ft/s or m/s]

    References
    ----------
    .. [2] L.S. Leung, Robert J. Wiles, and Donald J. Nicklin. Correlation for
       Predicting Choking Flowrates in Vertical Pneumatic Conveying. Ind. Eng.
       Chem. Process Des. Develop., vol. 10, no. 2, pp. 183-189, 1971.
    """
    uch = 32.3 * us + 0.97 * ut
    return uch


def uch_matsen(gs, rhos, ut):
    """
    Choking velocity from the Matsen paper [3]_.

    Parameters
    ----------
    gs : float
        Solids flux [kg/(s m^2)]
    rhos : float
        Density of particle [kg/m^3]
    ut : float
        Terminal velocity [m/s]

    Returns
    -------
    uch : float
        Choking velocity [m/s]

    References
    ----------
    .. [3] Matsen, 1982. Mechanism of Choking and Entrainment. Powder
       Technology, 32, 21-33.
    """
    uch = 10.74 * ut * (gs / rhos)**0.227
    return uch


def uch_psri(x, dp, d_pipe, gs, rhog, rhos, ut):
    """
    Choking velocity from PSRI 2016 notebook. Uses MKS units for input
    parameters but returns Uch in ft/s. Function requires SciPy fsolve to solve
    for Uch.

    Parameters
    ----------
    x : float
        Solve for Uch with SciPy fsolve
    dp : float
        Particle size [m]
    d_pipe : float
        Pipe diameter [m]
    gs : float
        Solids mass flux [kg/(s m^2)]
    rhog : float
        Density of gas [kg/m^3]
    rhos : float
        Density of particle [kg/m^3]
    ut : float
        Terminal velocity [m/s]

    Returns
    -------
    uch : float
        Choking velocity [ft/s]

    References
    ----------
    Notebook from PSRI 2016 workshop, pages J-20 and J-72.
    """
    uch = x                     # define variable to solve for
    g = 32.2                    # gravitational constant, ft/s^2
    dp = dp * 3.28084           # convert from m to ft
    d_pipe = d_pipe * 3.28084   # convert from m to ft
    gs = gs * 0.204817303       # convert from kg/(s m^2) to lb/(s ft^2)
    rhog = rhog * 0.062428      # convert from kg/m^3 to lb/ft^3
    rhos = rhos * 0.062428      # convert from kg/m^3 to lb/ft^3
    ut = ut * 3.28084           # convert from m/s to ft/s
    f1 = (uch - ut) / ((g * dp)**0.5) - ((gs / (uch * rhog))**0.35 * (d_pipe / dp)**0.35 * (rhos / rhog)**0.1)
    return f1


def uch_punwani(xy, d_pipe, gs, rhog, rhos, ut):
    """
    Provide functions to solve for voidage and choking velocity based on
    equations from Punwani 1976. Requires SciPy fsolve function.

    Parameters
    ----------
    xy
        Solves for ep and uch using SciPy fsolve where
        ep = voidage [-] and uch = choking velocity [m/s]
    d_pipe : float
        Internal pipe diameter [m]
    gs : float
        Solids flux [kg/(s m^2)]
    rhog : float
        Density of gas, must be in units of lb/ft^3
    rhos : float
        Density of particle [kg/m^3]
    ut : float
        Terminal velocity [m/s]

    Returns
    -------
    f1, f2 : functions
        Functions to solve for ep and uch

    References
    ----------
    Punwani, Modi, Tarman, 1976. A Generalized Correlation for Estimating
    Choking Velocity in Vertical Solids Transport. Institute of Gas Technology,
    Chicago, IL, 1-14.
    """
    ep, uc = xy     # define variables
    g = 9.81        # accelerationg of gravity, m/s^2

    f1 = 2 * g * d_pipe * ((ep**-4.7) - 1) - (0.074 * rhog**0.77) * (uc / ep - ut)**2
    f2 = (gs / rhos) / (1 - ep) - (uc / ep) + ut
    return f1, f2


def uch_yang(xy, d_pipe, gs, rhos, ut):
    """
    Provide functions to solve for voidage and choking velocity based on
    equations from Yang 1975. Requires SciPy fsolve function.

    Parameters
    ----------
    xy
        Solve for ep and uch using SciPy fsolve where
        ep = voidage [-] and uch = choking velocity [m/s]
    d_pipe : float
        Internal pipe diameter [m]
    gs : float
        Solids flux [kg/(s m^2)]
    rhos : float
        Density of particle [kg/m^3]
    ut : float
        Terminal velocity [m/s]

    Returns
    -------
    f1, f2 : fuctions
        Functions to solve for ep and uch

    References
    ----------
    Yang, 1975. A Mathematical Definition of Choking Phenomenon and a
    Mathematical Model for Predicting Choking Velocity and Choking Voidage.
    AIChE Journal, 21, 5, 1013-1015.
    """
    ep, uch = xy     # define variables
    g = 9.81        # acceleration due to gravity, m/s^2

    f1 = 2 * g * d_pipe * ((ep**-4.7) - 1) - 0.01 * (uch / ep - ut)**2
    f2 = gs - (uch / ep - ut) * rhos * (1 - ep)
    return f1, f2


def uch_yousfi(dp, gs, rhog, mu, ut):
    """
    Choking velocity from Yousfi 1974, also see Zhang 2015 paper.

    Parameters
    ----------
    dp : float
        Particle diameter [ft or m]
    gs : float
        Solids flux [lb/(hr ft^2) or kg/(s m^2)]
    rhog : float
        Gas density [lb/ft^3 or kg/m^3]
    mu : float
        Gas viscosity [lb/(ft s) or kg/(s m)]
    ut : float
        Terminal velocity of particle [ft/s or m/s]

    Returns
    -------
    uch : float
        Choking velocity [ft/s or m/s]

    References
    ----------
    Yousfi, Gau, 1974. Aerodynamique De L'Ecoulement Verical De Suspensions
    Concentrees Gaz-Solides I. Regimes D'Ecoulement Et Stabilite Aerodynamique.
    Chemical Engineering Science, 29, 1939-1946.
    """
    g = 9.81                    # accelaration due to gravity, m/s^2
    re = (dp * rhog * ut) / mu      # Reynolds number at terminal velocity
    uch = (32 * np.sqrt(g * dp) * (re**-0.06) * (gs**0.28 / rhog**0.28))**(1 / (1 + 0.28))
    return uch


def uch_zhang(ar, dp, gs, rhog):
    """
    Choking velocity from Zhang 2015.

    Parameters
    ----------
    ar : float
        Archimedes number [-]
    dp : float
        Diameter of particle [m]
    gs : float
        Solids flux [kg/(s m^2)]
    rhog : float
        Density of gas [kg/m^3]

    Returns
    -------
    uch : float
        Choking velocity [m/s]

    Reference
    ---------
    Zhang, Degreve, Dewil, Baeyens, 2015. Operation diagram of Circulating
    Fluidized Beds (CFBs). Procedia Engineering, 102, 1092-1103.
    """
    g = 9.81    # gravity constant, m/s^2
    uch = (14.6 * np.sqrt(g * dp) * (gs**0.542) / (rhog**0.542) * ar**0.105)**(1 / (1 + 0.542))
    return uch
