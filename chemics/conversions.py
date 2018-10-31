
def slm_to_lpm(slm, pgas, tgas):
    """
    Convert volumetric gas flow from standard liters per minute (SLM or SLPM)
    to liters per minute (LPM) where STP defined as 273.25 K and 101,325 Pa.

    Parameters
    ----------
    slm : float
        Volumetric gas flow in standard liters per minute [SLM]
    pgas : float
        Absolute gas pressure [kPa]
    tgas : float
        Gas temperature [K]

    Returns
    -------
    lpm : float
        Volumetric gas flow in liters per minute [LPM]

    Conversion
    ----------
    1 LPM = 1 SLPM * (Tgas / 273.15 K) * (14.696 psi / Pgas)

    Reference
    ---------
    Wikipedia contributors. (2018, February 8). Standard litre per minute.
    In Wikipedia online. Retrieved from
    https://en.wikipedia.org/wiki/Standard_litre_per_minute

    """
    # equation requires gas pressure as psi so convert kPa to psi
    pgas_psi = pgas * 0.1450377
    lpm = slm * (tgas / 273.15) * (14.696 / pgas_psi)
    return lpm
