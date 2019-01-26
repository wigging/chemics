import numpy as np


def eexp(db, hb, rhop, mp):
    """
    Calculates the overall void fraction of the expanded bed.

    Parameters
    ----------
    db : float
        Diameter of the bed [m]
    hb : float
        Height of the expanded bed [m]
    rhop : float
        Mass density of the solids [kg/m^3]
    mp : float
        Mass of solids in the bed [kg]

    Note
    ----
    Specific mass and length units are not important, provided they are
    all self-consistent as the returned quantity is dimensionless.

    Returns
    -------
    ep_exp : float
        Overall void fraction of the expanded bed [-]
    """

    # Volume of the expanded bed
    vb = np.pi * (db**2 / 4.0) * hb

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
    fbexp : float
        Bed expansion factor [-]
    ep_exp : float
        Void fraction in the expanded bed [-]

    Returns
    -------
    e_mf : float
        Void fraction at minimum fluidization [-]
    """

    e_mf = 1 - fbexp * (1 - ep_exp)
    return e_mf


def ueGas(ub, umf, emf, delta, fw):
    """
    This function calculates the velocity of the gas in the emulsion phase with
    K/L eqs. 6.39-6.40.

    Parameters
    ----------
    ub : float
        Bubble rise velocity [m/s]
    umf : float
        Minimum fluidization velocity [m/s]
    emf : float
        Void fraction at minimum fluidization [-]
    delta : float
        Fraction of bed volume in bubbles [-]
    fw : float
        Ratio of wake volume to bubble volume [-]

    Returns
    -------
    ue : float
        Emulsion gas velocity [m/s]
    """

    ue = umf / emf - fw * delta * ub / (1 - delta - fw * delta)
    return ue


def solidsDistribution(delta, emf, umf, ub, fw):
    """
    Calculates the distribution of solids in the bubble, cloud/wake, and
    emulsion phases using K/L eqs. 6.35-6.37.

    Parameters
    ----------
    delta : float
        Volume fraction of gas in the bubbles [-]
    emf : float
        Void fraction at minimum fluidization [-]
    umf : float
        Minimum fluidization velocity [m/s]
    ub : float
        Bubble rise velocity [m/s]
    fw : float
        Ratio of the wake volume to the bubble volume [-]

    Note
    ----
    gamma_b is for the moment a hard-coded constant. See K/L eq. 6.37.

    Returns
    -------
    gamma_b : float
        Volume of solids in the bubble divided by the bubble volume
    gamma_c : float
        Volume of solids in the cloud/wake divided by the bubble volume
    gamma_e : float
        Volume of solids in the emulsion divided by the bubble volume
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
    umf : float
        Minimum fluidization velocity [m/s]
    emf : float
        Void fraction at minimum fluidization [-]
    db : float
        Bubble diameter [m]
    ub : float
        Bubble rise velocity [m/s]
    diff : float
        Diffusion coefficient [m^2/s]
    approx : boolean
        Control whether to use a simpler expression that does not employ the
        diffusion coefficient
    method : string
        Correlation to use as either KL for Kunii-Levenspiel or SG for
        Sit-Grace method

    Returns
    -------
    kbe : float
        Rate constant (s^-1) for exchanging gas between the bubble and the
        emulsion
    """

    # Constants
    g = 9.81    # m/s^2

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

            # Bubble/cloud exchange (10.27) in units of [1/s]
            kbc = 4.5 * (umf / db) + 5.85 \
                * (np.sqrt(diff) * g**0.25 / db**1.25)

            # Cloud/emulsion exchange (10.34)
            kce = 6.77 * np.sqrt(diff * emf * ub / db**3)

            # Overall rate
            inv_kbe = 1.0/kbc + 1.0/kce
            kbe = 1.0/inv_kbe

            return kbe

    elif method == 'SG':

        kbe = 2*umf/db + 12.0/db**1.5 * np.sqrt(diff*emf*ub/np.pi)
        return kbe

    else:

        raise NotImplementedError(
            'Unknown mass transfer coefficient estimation method ' +
            str(method))


def solidsFluxWenChen(db, dt, umf, us, rhog, ug):
    """
    Calculates the solids flux at the surface of the bubbling bed according to
    the method of Wen and Chen (AIChE J, 28, 1, pp. 117-128) with a correction
    recommended by Wells, Kulver, and Krishnan in ORNL/TM-7847 (TVA AFBC
    Simulation Interim Annual Report, Dec. 1980) for large bed diameters.

    Parameters
    ----------
    db : float
        Bubble diameter [m]
    dt : float
        Bed/tank diameter [m]
    umf : float
        Minimum fluidization velocity [m/s]
    us : float
        Superficial velocity [m/s]
    rhog : float
        Gas mass density [kg/m^3]
    ug : float
        Gas viscosity [kg/m/s]

    Returns
    -------
    F0 : float
        Mass flux of entrained solids [kg/m^2/s]
    """

    g = 9.81    # m/s^2

    # Tube cross-sectional area, m^2
    ac = np.pi * dt**2 / 4

    # Solids flux
    F0 = 3.07e-9 * (ac * db * (us - umf)**2.5 * rhog**2.5 * np.sqrt(g)) \
        / (ug**2.5 * umf)

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
    dp : float
        Particle diameter [m]
    db : float
        Bubble diameter [m]
    emf : float
        Void fraction at minimum fluidization [-]
    umf : float
        Minimum fluidization velocity [m/s]
    us : float
        Superficial gas velocity [m/s]

    Returns
    -------
    F0 : float
        Solids entrainment flux at the top of the bed [kg/m^2/s]
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
    rhop : float
        Mass density of the particles
    emf : float
        Void fraction at minimum fluidization [-]
    umf : float
        Minimum fluidization velocity [m/s]
    us : float
        Superficial gas velocity [m/s]

    Returns
    -------
    F0 : float
        Solids entrainment flux at the top of the bed [kg/m^2/s]
    """

    F0 = 0.1 * rhop * (1 - emf) * (us - umf)
    return F0
