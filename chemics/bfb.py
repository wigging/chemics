"""
Bubbling Fluidized Bed (BFB)
============================

Functions for modeling bubbling fluidized bed (BFB) reactors. All references to
K/L are to Fluidization Engineering book by Kunii & Levenspiel. Lists of the
functions in this module are provided below. See the doc string in each
function for more details.

Emulsion
--------
fbexp
eexp
emf
dbMoriWen
ubMoriWen
ueGas
bubbleFraction
solidsDistribution
massTransferCoeff
solidsFluxWenChen
solidsFLuxPembNose
solidsFLuxPembWake
solidsMassFlow

Minimum Fluidization Velocity
-----------------------------
umfWenYu
umfRich
umfSaxVog
umfBabu
umfGrace
umfChit
umfErgun
umfLargeRe
umfSmallRe

Miscellaneous
-------------
uTerminal
tdhDecayConstant
tdhHeight

References
----------
[1] Kunii, Daizo, and Octave Levenspiel. Fluidization engineering. Elsevier;
Butterworth-Heinemann, 2nd edition, 1991.
[2] Marcio de Souza-Santos. Solid Fuels Combustion and Gasification: Modeling,
Simulation, and Equipment Operations. CRC Press, Taylor and Francis Group, 2nd
edition, 2010.
"""

from math import pi, exp, sqrt, log
import numpy as np


def fbexp(db, dp, rhog, rhop, umf, us):
    """
    Bed expansion factor for calculating expanded bed height of a bubbling
    fluidized bed reactor. See equations 14.7, 14.8, 14.18 in the Souza-Santos
    2010 book.

    Parameters
    ----------
    db = diameter of bed, m
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    umf = minimum fluidization velocity, m/s
    us = superficial gas velocity, m/s

    Returns
    -------
    fbx = bed expansion factor, (-)
    """
    if db < 0.0635:
        # diameter of bed as db < 0.0635 m from Eq 14.7
        tm1 = 1.032 * ((us - umf)**0.57) * (rhog**0.083)
        tm2 = (rhop**0.166) * (umf**0.063) * (db**0.445)
        fbx = 1 + (tm1 / tm2)
    else:
        # diameter of bed as db >= 0.0635 m from Eq 14.8
        tm1 = 14.314 * ((us - umf)**0.738) * (dp**1.006) * (rhop**0.376)
        tm2 = (rhog**0.126) * (umf**0.937)
        fbx = 1 + (tm1 / tm2)

    return fbx


def eexp(db, hb, rhop, mp):
    """
    Calculates the overall void fraction of the expanded bed.

    Parameters
    ----------
    db = diameter of the bed, m
    hb = height of the expanded bed, m
    rhop = mass density of the solids, kg/m^3
    mp = mass of solids in the bed, kg

    NOTE: specific mass and length units are not important, provided they are
    all self-consistent as the returned quantity is dimensionless.

    Returns
    -------
    ep_exp = overall void fraction of the expanded bed (-)
    """

    # Volume of the expanded bed
    vb = pi * (db**2 / 4.0) * hb

    # Volume due to the solids
    vp = mp / rhop

    # Overall void fraction
    ep_exp = 1.0 - float(vp) / vb

    return ep_exp


def emf(fbexp, ep_exp):
    """
    Calculate the void fraction at minimum fluidization for the specified bed.

    Parameters
    ----------
    fbexp = bed expansion factor, (-)
    ep_exp = void fraction in the expanded bed (-)

    Returns
    -------
    e_mf = void fraction at minimum fluidization
    """

    e_mf = 1 - fbexp * (1 - ep_exp)
    return e_mf


def umfWenYu(dp, rhog, rhop, ug):
    """
    Calculate minimum fluidization velocity, Umf, according to the Wen and Yu
    coefficients. See pages 69, 70, Table 4 in Kunii and Levenspiel 1991 book.

    Parameters
    ----------
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    ep = void fraction, (-)
    phi = sphericity of bed particle, (-)
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    ep = void fraction, (-)
    phi = sphericity of bed particle, (-)
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3

    Returns
    -------
    umf = minimum fluidization velocity, m/s
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
    dp = diameter of bed particle, m
    ep = void fraction, (-)
    phi = sphericity of bed particle, (-)
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    ug = viscosity of gas, kg/ms

    Returns
    -------
    umf = minimum fluidization velocity, m/s
    """
    g = 9.81    # gravity, m/s^2
    umf = ((dp**2*(rhop-rhog)*g)/(150 * ug)) * ((ep**3 * phi**2) / (1 - ep))
    return umf


def dbMoriWen(z, us, umf, d_bed, l_or, distributor_type):
    """
    Calculates the equivalent diameter of the gas bubble in the bed, assuming
    that all of the volume in bubbles in the bed were combined into a single
    spherical bubble. This uses the Mori/Wen correlation as given in
    Fluidization Engineering by Kunii & Levenspiel (K/L), eqs. 5.15, 5.19, and
    6.5.

    Parameters
    ----------
    z = height of the bubble along the vertical axis of the bed, m
    us = superficial velocity of the gas, m/s
    umf = minimum fluidization velocity, m/s
    d_bed = bed diameter, m
    l_or = orifice spacing, m (only if perforated plate distributor used)
    distributor_type = type of distributor plate: options are
        'perf_sq' = perforated, square arrangement of orifices
        'perf_tri' = perforated, triangular arrangement of orifices
        'porous' = porous (equivalent to perforated triangular arrangement of
            tiny orifices)

    Returns
    -------
    db = equivalent bubble diameter at the specified z position, m
    """

    # Constants
    g_cgs = 981.0    # gravity, cm/s^2

    # Convert all mks units to cgs units for use with the correlation, which
    # appears in K/L in cgs units.
    z_cgs = z * 100.0
    us_cgs = us * 100.0
    umf_cgs = float(umf) * 100.0
    d_bed_cgs = d_bed * 100.0
    l_or_cgs = l_or * 100.0

    # Maximum bubble diameter, cm
    db_max = 0.65 * (pi / 4 * d_bed_cgs**2 * (us_cgs - umf_cgs))**0.4

    # Minimum bubble diameter, cm for high flow rate/large bubble sizes at
    # distributor plate. Also works for porous distributors.
    db_min_high = 2.78 / g_cgs * (us_cgs - umf_cgs)**2

    if distributor_type == 'perf_sq':

        # Minimum bubble diameter, cm for low flow rate/small bubble sizes at
        # distributor plate
        db_min_low = 1.3 / (g_cgs**0.2) * ((us_cgs - umf_cgs) * l_or_cgs**2)**0.4

        # Set the minimum bubble diameter based on the orifice spacing
        if db_min_low <= l_or_cgs:
            db_min = db_min_low
        else:
            db_min = db_min_high

    elif distributor_type == 'perf_tri':

        # Minimum bubble diameter, cm for low flow rate/small bubble sizes at
        # distributor plate
        db_min_low = 1.3 / (g_cgs**0.2) * ((us_cgs - umf_cgs) *
                                           l_or_cgs**2 * sqrt(3)/2)**0.4

        # Set the minimum bubble diameter based on the orifice spacing
        if db_min_low <= l_or_cgs:
            db_min = db_min_low
        else:
            db_min = db_min_high

    elif distributor_type == 'porous':

        # Just use the high flow rate equation at the distributor
        db_min = db_min_high

    else:
        raise NotImplementedError("Unknown distributor type " +
                                  str(distributor_type) + " in Mori/Wen bubble diameter calculation.")

    # Equivalent bubble diameter, cm
    db = db_max - (db_max - db_min) * exp(-0.3 * z_cgs / d_bed_cgs)

    # Constrain to 80% of the diameter of the column
    db = min(0.8*d_bed*100.0, db)

    # Return the bubble diameter, m
    return db / 100.0


def ubMoriWen(us, umf, db):
    """
    Estimates the velocity of a bubble in a manner consistent with the Mori/Wen
    correlation. This is eq. <> in Kunii & Levenspiel.

    Parameters
    ----------
    us = superficial gas velocity, m/s
    umf = minimum fluidization velocity, m/s
    db = bubble diameter, m

    Returns
    -------
    ub = bubble rise velocity, m/s
    """

    # Constants
    g = 981.0 # cm/s^2

    # Convert everything to cgs
    us_cgs = us * 100.0
    umf_cgs = umf * 100.0
    db_cgs = db * 100.0

    ub_cgs = (us_cgs - umf_cgs) + 0.711 * sqrt(g * db_cgs)

    return ub_cgs / 100.0


def ueGas(ub, umf, emf, delta, fw):
    """
    This function calculates the velocity of the gas in the emulsion phase with
    K/L eqs. 6.39-6.40.

    Parameters
    ----------
    ub = bubble rise velocity (m/s)
    umf = minimum fluidization velocity (m/s)
    emf = void fraction at minimum fluidization
    delta = fraction of bed volume in bubbles (-)
    fw = ratio of wake volume to bubble volume (-)

    Returns
    -------
    ue = emulsion gas velocity (m/s)
    """

    ue = umf / emf - fw * delta * ub / (1 - delta - fw * delta)
    return ue


def bubbleFraction(ub, us, umf, emf):
    """
    Calculates the fraction of the bed that is in the bubble phase using K/L
    eqs. 6.26-6.29.

    Parameters
    ----------
    ub = bubble rise velocity (m/s, cm/s, etc.)
    us = superficial gas velocity (m/s, cm/s, etc.)
    umf = minimum fluidization velocity (m/s, cm/s, etc.)
    emf = minimum fluidization void fraction (-)

    NOTE: Units are not important, provided they are consistent, as the
    calculation returns a dimensionless quantity.

    Returns
    -------
    delta = the fraction of the total bed volume that is in bubbles.
    """

    # Velocity of gas in the emulsion -- used to decide which regime we are in
    ue = umf / emf

    # Ratio of velocities. This ratio determines which regime we are in.
    ub_ue_ratio = float(ub) / float(ue)

    # Calculate delta
    if ub_ue_ratio < 1:     # Slow bubbles
        delta = (us - umf) / (ub + 2*umf)
    elif ub_ue_ratio > 10:  # Very fast bubbles
        delta = us / ub
    elif ub_ue_ratio > 5:   # Fast Bubbles
        delta = (us - umf) / (ub - umf)
    elif ub_ue_ratio < 3:   # Slower intermediate bubbles
        delta = (us - umf) / (ub + umf)
    else:                   # Faster intermediate bubbles
        delta = (us - umf) / ub

    return delta


def solidsDistribution(delta, emf, umf, ub, fw):
    """
    Calculates the distribution of solids in the bubble, cloud/wake, and
    emulsion phases using K/L eqs. 6.35-6.37.

    Parameters
    ----------
    delta = volume fraction of gas in the bubbles (-)
    emf = void fraction at minimum fluidization (-)
    umf = minimum fluidization velocity (m/s)
    ub = bubble rise velocity (m/s)
    fw = ratio of the wake volume to the bubble volume

    Returns
    -------
    gamma_b = volume of solids in the bubble divided by the bubble volume
    gamma_c = volume of solids in the cloud/wake divided by the bubble volume
    gamma_e = volume of solids in the emulsion divided by the bubble volume

    NOTE: gamma_b is for the moment a hard-coded constant. See K/L eq. 6.37.
    """

    gamma_b = 0.005
    gamma_c = (1.0 - emf) * (3.0/(ub * float(emf) / umf - 1.0) + fw)
    gamma_e = (1.0 - emf) * (1.0 - delta) / delta - gamma_b - gamma_c
    return gamma_b, gamma_c, gamma_e


def massTransferCoeff(umf, emf, db, ub, diff, approx=True, method=None):
    """
    Calculates the rate constant for gas exchange between the bubble and the
    emulsion. See K/L eqs. 10.27, 10.34, and 10.36.

    Parameters
    ----------
    umf = minimum fluidization velocity (m/s)
    emf = void fraction at minimum fluidization (-)
    db = bubble diameter (m)
    ub = bubble rise velocity (m/s)
    diff = diffusion coefficient (m^2/s)
    approx = boolean controlling whether to use a simpler expression that does
        not employ the diffusion coefficient
    method = correlation to use -- either 'KL' (Kunii-Levenspiel) or 'SG'
        (Sit-Grace)

    Returns
    -------
    kbe = the rate constant (s^-1) for exchanging gas between the bubble and the
        emulsion
    """

    # Constants
    g = 9.81 # m/s^2

    if method == 'KL':
        # First check the bubbling regime
        if approx and (1 < ub / (umf / emf) < 5):
            # Intermediate bubbling, use a simpler approximation that doesn't
            # require the (poorly known) diffusion coefficient. See K/L eq.
            # 12.47.
            kbe = 4.5 * umf / db
            return kbe
        else:
            # We should use the full equation.

            # Bubble/cloud exchange (10.27)
            kbc = 4.5 * (umf / db) + 5.85 * (sqrt(diff) * g**0.25 / db**1.25) # s^-1

            # Cloud/emulsion exchange (10.34)
            kce = 6.77 * sqrt(diff * emf * ub / db**3)

            # Overall rate
            inv_kbe = 1.0/kbc + 1.0/kce
            kbe = 1.0/inv_kbe

            return kbe

    elif method == 'SG':

        kbe = 2*umf/db + 12.0/db**1.5 * sqrt(diff*emf*ub/pi)
        return kbe

    else:

        raise NotImplementedError(
            'Unknown mass transfer coefficient estimation method ' +
            str(method))


def uTerminal(dp, rhog, rhop, ug, phi):
    """
    Calculates the terminal velocity of a solid particle from K/L eqs.
    3.31-3.33.

    Parameters
    ----------
    dp = diameter of the particle (m)
    rhog = gas mass density (kg/m^3)
    rhop = particle mass density (kg/m^3)
    ug = gas dynamic viscosity (kg/m/s)
    phi = particle sphericity (-)

    NOTE: This calculation is only valid if 0.5 < phi < 1

    Returns
    -------
    ut = terminal velocity (m/s) of the particle
    """

    # Constants
    g = 9.81    # m/s^2

    # Calculate the dimensionless particle diameter (the cube root of the
    # Archimedes number)
    Ar = (g* (dp**3) * rhog * (rhop - rhog)) / (ug**2)   # Ar = Archimedes number, (-)
    d_star = Ar**(1.0 / 3)  # K/L eq. 3.31

    # Calculate the dimensionless terminal velocity, K/L eq. 3.33
    ut_star_inv = 18.0 / (d_star**2) + (2.335 - 1.744 * phi) / sqrt(d_star)
    ut_star = 1.0 / ut_star_inv

    # Calculate the terminal velocity
    ut = ut_star * ((ug * (rhop - rhog) * g) / (rhog**2))**(1.0 / 3)

    return ut


def solidsFluxWenChen(db, dt, umf, us, rhog, ug):
    """
    Calculates the solids flux at the surface of the bubbling bed according to
    the method of Wen and Chen (AIChE J, 28, 1, pp. 117-128) with a correction
    recommended by Wells, Kulver, and Krishnan in ORNL/TM-7847 (TVA AFBC
    Simulation Interim Annual Report, Dec. 1980) for large bed diameters.

    Parameters
    ----------
    db = bubble diameter (m)
    dt = bed/tank diameter (m)
    umf = minimum fluidization velocity (m/s)
    us = superficial velocity (m/s)
    rhog = gas mass density (kg/m^3)
    ug = gas viscosity (kg/m/s)

    Returns
    -------
    F0 = the mass flux of entrained solids (kg/m^2/s)
    """

    g = 9.81    # m/s^2

    # Tube cross-sectional area, m^2
    ac = pi * dt**2 / 4

    # Solids flux
    F0 = 3.07e-9 * (ac * db * (us - umf)**2.5 * rhog**2.5 * sqrt(g)) / (ug**2.5 * umf)

    # Correction for small aspect ratio beds (wider than it is deep)
    if float(db) / dt < 1:
        F0 *= (float(db) / dt)**2

    return F0


def solidsFluxPembNose(dp, db, emf, umf, us):
    """
    Calculates the solids entrainment flux for the surface of a bubbling bed
    with the bubble nose ejection model of Pemberton and Davidsion (Chem. Eng.
    Sci., 1986, 41, pp. 243-251). This model is suitable if there is a single
    bubble in the bed.

    Parameters
    ----------
    dp = particle diameter (m)
    db = bubble diameter (m)
    emf = void fraction at minimum fluidization (-)
    umf = minimum fluidization velocity (m/s)
    us = superficial gas velocity (m/s)

    Returns
    -------
    F0 = solids entrainment flux at the top of the bed (kg/m^2/s)
    """

    F0 = 3.0 * dp / db * (1 - emf) * (us - umf)
    return F0


def solidsFluxPembWake(rhop, emf, umf, us):
    """
    Calculates the solids entrainment flux for the surface of a bubbling bed
    with the bubble wake ejection model of Pemberton and Davidsion (Chem. Eng.
    Sci., 1986, 41, pp. 243-251). This model is suitable if multiple bubbles
    coalesce at the surface before bursting.

    Parameters
    ----------
    rhop = mass density of the particles
    emf = void fraction at minimum fluidization (-)
    umf = minimum fluidization velocity (m/s)
    us = superficial gas velocity (m/s)

    Returns
    -------
    F0 = solids entrainment flux at the top of the bed (kg/m^2/s)
    """

    F0 = 0.1 * rhop * (1 - emf) * (us - umf)
    return F0


def solidsMassFlow(F0, A):
    """
    Calculates the solids mass flow rate for the specified flux and
    cross-sectional area.

    Parameters
    ----------
    F0 = mass flux (kg/m^2/s)
    A = cross-sectional area (m^2)

    Returns
    -------
    mdot = mass flow rate (kg/s)
    """

    mdot = F0 * A
    return mdot


def tdhDecayConstant(dp):
    """
    Calculates the transport disengagement decay constant given the particle
    diameter and superficial velocity. The correlation is a curve fit to data in
    K/L Fig. 7.12. Maximum particle diameter on plot is 800 um, and maximum
    superficial velocity is 1.25 m/s.

    Parameters
    ----------
    dp = particle diameter (m)

    Returns
    -------
    a_us = the transport disengagement decay constant (1/m) multiplied by the
        superficial velocity (m/s) for a product with units (1/s)
    """

    # This is the raw data that we use to fit the trend line to. It has been
    # read off the graph in a rather sophisticated manner. The graph was scanned
    # from the K/L book, and then the coordinates (in pixels) at select
    # locations along the curve were noted and transformed into particle
    # diameters and a*u values according to the linear transform relating the
    # pixel coordinates and the graph scales.
    # dp_data = [34.0, 162.0, 302.0, 487.0, 616.0, 800.0] # um
    # au_data = [0.39, 1.17, 1.70, 2.29, 2.67, 3.16] # 1/s

    # Power law fit to the data. Current R^2 value is larger than 0.99.
    # Make sure to update this if the dataset changes!
    coeff = 0.03918
    power = 0.65883

    # Calculate a*us. Note that the particle diameter for the fit is in um, not
    # m.
    a_us = coeff * (dp / 1e-6)**power

    return a_us


def tdhHeight(a, x):
    """
    Calculates the transport disengagement height for the specified decay
    constant and fraction of upward solids flux at that height. It assumes total
    reflux (no solids elutriation).

    Parameters
    ----------
    a = decay constant (1/m)
    x = fraction of entrained solids at the TDH (-)

    Returns
    -------
    tdh = transport disengagement height (m)
    """

    tdh = -log(x) / a

    return tdh
