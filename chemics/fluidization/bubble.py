"""
Bubble
------

This module contains functions for calculating bubble diameter and bubble
velocity.
"""

from math import exp, pi, sqrt


def dbMoriWen(z, us, umf, d_bed, l_or, distributor_type):
    """
    Calculates the equivalent diameter of the gas bubble in the bed, assuming
    that all of the volume in bubbles in the bed were combined into a single
    spherical bubble. This uses the Mori/Wen correlation as given in
    Fluidization Engineering by Kunii & Levenspiel (K/L), eqs. 5.15, 5.19, and
    6.5.

    Parameters
    ----------
    z : float
        Height of the bubble along the vertical axis of the bed [m]
    us : float
        Superficial velocity of the gas [m/s]
    umf : float
        Minimum fluidization velocity [m/s]
    d_bed : float
        Bed diameter [m]
    l_or : float
        Orifice spacing [m] (only if perforated plate distributor used)
    distributor_type : string
        Type of distributor plate
        Options are
        'perf_sq' = perforated, square arrangement of orifices
        'perf_tri' = perforated, triangular arrangement of orifices
        'porous' = porous (equivalent to perforated triangular arrangement of tiny orifices)

    Returns
    -------
    db : float
        Equivalent bubble diameter at the specified z position [m]
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
    us : float
        Superficial gas velocity [m/s]
    umf : float
        Minimum fluidization velocity [m/s]
    db : float
        Bubble diameter [m]

    Returns
    -------
    ub : float
        Bubble rise velocity [m/s]
    """

    # Constants
    g = 981.0   # cm/s^2

    # Convert everything to cgs
    us_cgs = us * 100.0
    umf_cgs = umf * 100.0
    db_cgs = db * 100.0

    ub_cgs = (us_cgs - umf_cgs) + 0.711 * sqrt(g * db_cgs)

    return ub_cgs / 100.0


def bubbleFraction(ub, us, umf, emf):
    """
    Calculates the fraction of the bed that is in the bubble phase using K/L
    eqs. 6.26-6.29.

    Parameters
    ----------
    ub : float
        Bubble rise velocity [m/s, cm/s, etc.]
    us : float
        Superficial gas velocity [m/s, cm/s, etc.]
    umf : float
        Minimum fluidization velocity [m/s, cm/s, etc.]
    emf : float
        Minimum fluidization void fraction [-]

    Note
    ----
    Units are not important, provided they are consistent, as the calculation
    returns a dimensionless quantity.

    Returns
    -------
    delta : float
     Fraction of the total bed volume that is in bubbles [-]
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
