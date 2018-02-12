"""
Velocity
========

See doc string and comments in each function for more details.

Terminal Velocity
-----------------
ut
ut_ganser

Choking and Transport Velocity
------------------------------
utr
uch_bifan
uch_leung
uch_matsen
uch_psri
uch_punwani
uch_yang
uch_yousfi
uch_zhang
"""

import numpy as np


def ut(cd, dp, rhog, rhos):
    """
    Terminal velocity of a single particle.

    Parameters
    ----------
    cd = drag coefficient, (-)
    dp = diameter of particle, m
    rhog = density of gas, kg/m^3
    rhos = density of solid, kg/m^3

    Return
    ------
    Ut = terminal velocity, m/s
    """
    g = 9.81  # gravity acceleration, m/s^2
    tm1 = 4*dp*(rhos - rhog)*g
    tm2 = 3*dp*cd
    Ut = (tm1/tm2)**(1/2)
    return Ut


def ut_ganser(dp, mug, rhog, rhos, sp):
    """
    Uses Ganser correlation to estimate terminal velocity of a specified
    particle in a gas with specified properties. According to the Chhabra 1999
    paper, the Ganser 1993 Cd correlation is applicable for sphericity values
    from 0.09 to 1. Cd drag coefficient from Ganser 1993 Eq. 18, Cd also
    referenced in Cui 2007 Eq. 2, and in Chhabra 1999 Eq. 6.

    Parameters
    ----------
    dp = particle diameter, m
    mug = gas viscosity, kg/(m s)
    rhog = gas density, kg/m^3
    rhos = solid particle density, kg/m^3
    sp = sphericity, -

    Returns
    -------
    Cd = particle terminal drag coefficient, (-)
    Re = particle terminal Reynolds number, (-)
    ut = particle terminal velocity, m/s

    References
    ----------
    Ganser, 1993. A rational approach to drag prediction of spherical and
    nonsperical particles. Powder Technology, 77, 143-152.

    Cui, Grace, 2007. Fluidization of biomass particles: A review of
    experimental multiphase flow aspects. Chemical Engineering Science, 62,
    45-55.

    Chhabra, Agarwal, Sinha, 1999. Drag on non-spherical particles: An
    evaluation of available methods. Powder Technology, 101, 288-295.
    """
    g = 9.81    # acceleration from gravity, m/s^2

    # shape factors
    # papers Cui 2007 and Chhabra 1999 leave out the -2.25*dv/D term
    K1 = (1/3 + 2/3*(sp**-0.5))**(-1)           # Stokes' shape factor
    K2 = 10**(1.8148*((-np.log(sp))**0.5743))   # Newton's shape factor

    # guess a range for terminal velocity, m/s
    ut = np.arange(0.001, 20, 0.001)

    # evaluate drag coefficients for range of ut
    # Re is Reynolds number, (-)
    # Cd is Ganser 1993 drag coefficient as function of Re, K1, K2 (-)
    # Cdd is drag coefficient as function of ut, etc. (-)
    Re = (dp*rhog*ut)/mug
    Cd = (24/(Re*K1))*(1 + 0.1118*((Re*K1*K2)**0.6567)) + (0.4305*K2)/(1+(3305/(Re*K1*K2)))
    Cdd = (4*g*dp*(rhos-rhog))/(3*(ut**2)*rhog)

    delta = np.abs(Cd-Cdd)  # compare difference between Cd and Cdd
    idx = np.argmin(delta)  # find index of minimum value in delta

    # select values to return based on above index
    return Cd[idx], Re[idx], ut[idx]


def utr(dp, rhog, rhos, mug):
    """
    Transport velocity of particles.

    Parameters
    ----------
    dp = diameter of particle, m
    rhog = density of gas, kg/m^3
    rhos = density of solid particle, kg/m^3
    mug = viscosity of gas, kg/(m s)

    Returns
    -------
    Utr = transport velocity, m/s

    Reference
    ---------
    Zhang, Degreve, Dewil, Baeyens, 2015. Operation diagram of Circulating
    Fluidized Beds. Procedia Engineering 102, 1092-1103.
    """
    g = 9.81  # gravitational constant, m/s^2
    Ar = ((dp**3)*rhog*(rhos-rhog)*g)/(mug**2)  # Archimedes number, (-)
    Utr = (mug/(dp*rhog))*(3.23 + 0.23*Ar)
    return Utr


def uch_bifan(Ar, dp, G, rhog):
    """
    Choking velocity from Bi and Fan 1991, also see Zhang 2015 paper.

    Parameters
    ----------
    Ar = Archimedes number, (-)
    dp = diameter of particle, m
    G = solids flux, kg/(s m^2)
    rhog = density of gas, kg/m^3

    Returns
    -------
    uch = choking velocity, m/s

    Reference
    ---------
    Bi, Fan, 1991. Regime transitions in gas-solid circulating fluidized beds.
    AIChE Annual Meeting. AIChE , Los Angeles, 17-22.
    """
    g = 9.81    # gravity constant, m/s^2
    uch = (21.6 * np.sqrt(g*dp) * (G**0.542)/(rhog**0.542) * Ar**0.105)**(1/(1+0.542))
    return uch


def uch_leung(G, rhop, ut):
    """
    Choking velocity from Leung 1971.

    Parameters
    ----------
    G = solids flux, lb/(hr ft^2) or kg/(s m^2)
    rhop = density of particle, lb/ft^3 or kg/m^3
    ut = terminal velocity of particle, ft/s or m/s

    Returns
    -------
    uch = choking velocity, ft/s or m/s

    Reference
    ---------
    Leung, Wiles, Nicklin, 1971. Correlation for Predicting Choking Flowrates
    in Vertical Pneumatic Conveying. Ind. Eng. Chem. Process Des. Develop, 10,
    2, 183-189.
    """
    uch = 32.3*(G/rhop) + 0.97*ut
    return uch


def uch_matsen(G, rhop, ut):
    """
    Choking velocity from Matsen 1982.

    Parameters
    ----------
    G = solids flux, kg/(s m^2)
    rhop = density of particle, kg/m^3
    ut = terminal velocity, m/s

    Returns
    -------
    uch = choking velocity, m/s

    Reference
    ---------
    Matsen, 1982. Mechanism of Choking and Entrainment. Powder Technology, 32, 21-33.
    """
    uch = 10.74*ut*(G/rhop)**0.227
    return uch


def uch_psri(x, dp, D, G, rhog, rhop, ut):
    """
    Choking velocity from PSRI 2016 notebook. Uses MKS units for input
    parameters but returns Uch in ft/s. Function requires SciPy fsolve to solve
    for Uch.

    Parameters
    ----------
    x = solve for Uch with SciPy fsolve
    dp = particle size, m
    D = pipe diameter, m
    G = solids mass flux, kg/(s m^2)
    rhog = density of gas, kg/m^3
    rhop = density of particle, kg/m^3
    ut = terminal velocity, m/s

    Returns
    -------
    uch = choking velocity, ft/s

    Reference
    ---------
    Notebook from PSRI 2016 workshop, pages J-20 and J-72.
    """
    uch = x                 # define variable to solve for
    g = 32.2                # gravitational constant, ft/s^2
    dp = dp * 3.28084       # convert from m to ft
    D = D * 3.28084         # convert from m to ft
    G = G * 0.204817303     # convert from kg/(s m^2) to lb/(s ft^2)
    rhog = rhog * 0.062428  # convert from kg/m^3 to lb/ft^3
    rhop = rhop * 0.062428  # convert from kg/m^3 to lb/ft^3
    ut = ut * 3.28084       # convert from m/s to ft/s
    f1 = (uch - ut)/((g*dp)**0.5) - ((G/(uch*rhog))**0.35 * (D/dp)**0.35 * (rhop/rhog)**0.1)
    return f1


def uch_punwani(xy, D, G, rhop, rhog, ut):
    """
    Provide functions to solve for voidage and choking velocity based on
    equations from Punwani 1976. Requires SciPy fsolve function.

    Parameters
    ----------
    xy = solves for ep and uc using SciPy fsolve
         where ep = voidage, (-)
               uch = choking velocity, m/s
    G = solids flux, kg/(s m^2)
    d = internal pipe diameter, m
    rhop = density of particle, kg/m^3
    rhog = density of gas, must be in units of lb/ft^3
    ut = terminal velocity, m/s

    Returns
    -------
    f1, f2 = functions to solve for ep and uch

    Reference
    ---------
    Punwani, Modi, Tarman, 1976. A Generalized Correlation for Estimating
    Choking Velocity in Vertical Solids Transport. Institute of Gas Technology,
    Chicago, IL, 1-14.
    """
    ep, uc = xy     # define variables
    g = 9.81        # accelerationg of gravity, m/s^2

    f1 = 2*g*D*((ep**-4.7) - 1) - (0.074*rhog**0.77)*(uc/ep - ut)**2
    f2 = (G/rhop)/(1 - ep) - (uc/ep) + ut
    return f1, f2


def uch_yang(xy, D, G, rhop, ut):
    """
    Provide functions to solve for voidage and choking velocity based on
    equations from Yang 1975. Requires SciPy fsolve function.

    Parameters
    ----------
    xy = solve for voidage ep (-) and choking velocity uc (m/s) using SciPy fsolve
    G = solids flux, kg/(s m^2)
    D = internal pipe diameter, m
    rhop = density of particle, kg/m^3
    ut = terminal velocity, m/s

    Returns
    -------
    f1, f2 = functions to solve for ep and uch

    Reference
    ---------
    Yang, 1975. A Mathematical Definition of Choking Phenomenon and a
    Mathematical Model for Predicting Choking Velocity and Choking Voidage.
    AIChE Journal, 21, 5, 1013-1015.
    """
    ep, uc = xy     # define variables
    g = 9.81        # acceleration due to gravity, m/s^2

    f1 = 2*g*D*((ep**-4.7) - 1) - 0.01*(uc/ep - ut)**2
    f2 = G - (uc/ep - ut)*rhop*(1 - ep)
    return f1, f2


def uch_yousfi(dp, G, rhog, mug, ut):
    """
    Choking velocity from Yousfi 1974, also see Zhang 2015 paper.

    Parameters
    ----------
    dp = particle diameter, ft or m
    G = solids flux, lb/(hr ft^2) or kg/(s m^2)
    rhog = gas density, lb/ft^3 or kg/m^3
    mug = gas viscosity, lb/(ft s) or kg/(s m)
    ut = terminal velocity of particle, ft/s or m/s

    Returns
    -------
    uch = choking velocity, ft/s or m/s

    Reference
    ---------
    Yousfi, Gau, 1974. Aerodynamique De L'Ecoulement Verical De Suspensions
    Concentrees Gaz-Solides I. Regimes D'Ecoulement Et Stabilite Aerodynamique.
    Chemical Engineering Science, 29, 1939-1946.
    """
    g = 9.81                    # accelaration due to gravity, m/s^2
    Re = (dp*rhog*ut) / mug     # Reynolds number at terminal velocity
    uch = (32 * np.sqrt(g*dp) * (Re**-0.06) * (G**0.28/rhog**0.28))**(1/(1+0.28))
    return uch


def uch_zhang(Ar, dp, G, rhog):
    """
    Choking velocity from Zhang 2015.

    Parameters
    ----------
    Ar = Archimedes number, (-)
    dp = diameter of particle, m
    G = solids flux, kg/(s m^2)
    rhog = density of gas, kg/m^3

    Returns
    -------
    uch = choking velocity, m/s

    Reference
    ---------
    Zhang, Degreve, Dewil, Baeyens, 2015. Operation diagram of Circulating
    Fluidized Beds (CFBs). Procedia Engineering, 102, 1092-1103.
    """
    g = 9.81    # gravity constant, m/s^2
    uch = (14.6 * np.sqrt(g*dp) * (G**0.542)/(rhog**0.542) * Ar**0.105)**(1/(1+0.542))
    return uch


