def molecular_diffusion_coeff(mw, T, mu, Vc, phi=1.0):
    """
    Estimate the molecular diffusion coefficient using the Wilke-Chang
    equation.

    .. math::  D_m = \\frac{7.4 \\times 10^{-8} (\\phi M)^{0.5} T}{\\mu V_{bp}^{0.6}}

    where:

    .. math::  V_{bp} = 0.285 \\times V_c^{1.048}

    Parameters
    ----------
    mw : float
        Molecular weight weight of solute [g/mol]
    T : float
        Temperature [K]
    mu : float
        Viscosity of the solvent [cP]
    Vc : float
        Critical volume of the solvent [cm^3/mol]
    phi : float, optional
        Association factor [-]. phi is 2.26 for water, 1.9 for methanol, 1.5
        for ethanol and 1.0 for an unassociated solvent.

    Returns
    -------
    Dm : float
        Molecular diffusion coefficient [cm^2/s]

    Example
    -------
    >>> molecular_diffusion_coeff(32.04, 298.2, 0.386, 173.0, phi=1.9)
    3.708e-5

    References
    ----------
    C.R. Wilke and P. Chang. Correlation of diffusion coefficients in dilute
    solutions. AIChE J., 1955, 1, 264–270.
    """
    Vbp = 0.285 * Vc**1.048
    Dm = 7.4e-8 * (phi * mw)**0.5 * T / (mu * Vbp**0.6)
    return Dm


def convective_mt_coeff(Dm, dp, epsilon, Re, Sc):
    """
    Estimate the convective mass transfer coefficient in packed beds using the
    Wilson and Geankoplis correlation.

    .. math::  k_f = \\frac{Sh D_m}{d_p}

    where

    .. math::  Sh = 1.09 \\varepsilon^{-1} Re^{0.33} Sc^{0.33}, \\quad 0.0015 < Re < 55
    .. math::  Sh = 0.25 \\varepsilon^{-1} Re^{0.69} Sc^{0.33}, \\quad 55 < Re < 1050

    Parameters
    ----------
    Dm : float
        Molecular diffusion coefficient [m^2/s]
    dp : float
        Particle diameter [m]
    epsilon : float
        Bed porosity [-]
    Re : float
        Reynolds number [-]
    Sc : float
        Schmidt number [-]

    Returns
    -------
    kf : float
        Convective mass transfer coefficient [m/s]

    Raises
    ------
    ValueError
        If Re is not in range 0.0015 - 1050.

    Example
    -------
    >>> convective_mt_coeff(4.79e-10, 5e-6, 0.335, 7.21e-3, 1452.0)
    6.77e-4

    References
    ----------
    E.J. Wilson, and C.J. Geankoplis. Liquid mass transfer at very low
    Reynolds numbers in packed beds. Ind. Eng. Chem. Fund., 1966, 5 (1), 9.

    D.M Ruthven. Principles of Adsorption and Adsorption Processes.
    John Wiley & Sons, Inc., New York, 1984.
    """
    if 0.0015 < Re < 55:
        Sh = 1.09 * epsilon**-1 * Re**0.33 * Sc**0.33
    elif 55 <= Re < 1050:
        Sh = 0.25 * epsilon**-1 * Re**0.69 * Sc**0.33
    else:
        raise ValueError(
            f'Correlation not applicable in the given conditions. \n'
            f'Re must be in rage 0.0015 < Re < 1050. It is {Re}. \n'
        )
    kf = Sh * Dm / dp
    return kf


def axial_dispersion_coeff(Dm, dp, ui):
    """
    Estimate the axial dispersion coefficient in packed beds using the Edwards
    and Richardson correlation.

    .. math:: D_{ax} = 0.73 D_m + 0.5 d_p u_i

    Parameters
    ----------
    Dm : float
        Molecular diffusion coefficient [m^2/s]
    dp : float
        Particle diameter [m]
    ui : float
        Interstitial velocity [m/s]

    Returns
    -------
    Dax : float
        Axial dispersion coefficient [m^2/s]

    Example
    -------
    >>> axial_dispersion_coeff(4.7e-9, 5.0e-6, 3.0e-3)
    1.0931e-8

    References
    ----------
    M.F. Edwards and J.F. Richardson. Correlation of axial dispersion data.
    J. Chem. Eng., 1970, 48 (4) 466, 1970.
    """
    Dax = 0.73 * Dm + 0.5 * dp * ui
    return Dax


def axial_dispersion_coeff_sc(Dm, epsilon, Re, Sc):
    """
    Estimate the axial dispersion coefficient in packed beds under supercritical
    conditions using the correlation of Funazukuri et al.

    .. math:: D_{ax} = \\frac{D_m}{\\varepsilon} 1.317 (\\varepsilon Re Sc)^{1.392}

    Valid for:

    .. math:: \\varepsilon Re Sc > 0.3, 3.9 < Sc < 665

    Parameters
    ----------
    Dm : float
        Molecular diffusion coefficient [m^2/s]
    epsilon : float
        Bed porosity [-]
    Re : float
        Reynolds number [-]
    Sc : float
        Schmidt number [-]

    Returns
    -------
    Dax : float
        Axial dispersion coefficient [m^2/s]

    Raises
    ------
    ValueError
        If epsilon*Re*Sc is not > 0.3 or Sc in not in range 3.9 - 665

    Example
    -------
    >>> axial_dispersion_coeff_sc(4.7e-9, 0.4, 1100.0, 135.0)
    0.06835

    References
    ----------
    T. Funazukuri, C. Kong, and S. Kagei. Effective axial dispersion
    coefficients in packed beds under supercritical conditions.
    J. Supercrit. Fluid, 1998, 13 (1–3), 169–175.
    """
    if (epsilon * Re * Sc > 0.3) and (3.9 < Sc < 665):
        Dax = Dm / epsilon * 1.317 * (epsilon * Re * Sc)**1.392
    else:
        raise ValueError(
            f'Correlation not applicable in the given conditions. \n'
            f'epsilon * Re * Sc must be > 0.3. It is {epsilon * Re * Sc:.2f}. \n'
            f'Sc must be in range 3.9 - 665. It is {Sc:.2f}. \n'
        )
    return Dax
