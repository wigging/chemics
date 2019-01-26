def bubbleFraction(ub, us, umf, emf):
    """
    Determine the fraction of the bed that is in the bubble phase using
    Equations 6.26 through 6.29 from Kunii and Levenspiel [1]_.

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

    Returns
    -------
    delta : float
        Fraction of the total bed volume that is in bubbles [-]

    Note
    ----
    Units are not important, provided they are consistent, as the calculation
    returns a dimensionless quantity.

    References
    ----------
    .. [1] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
           Butterworth-Heinemann, 2nd edition, 1991.
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
