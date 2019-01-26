import numpy as np


def umf_coeff(dp, mu, rhog, rhos, coeff='wenyu'):
    """
    Determine minimum fluidization velocity using experimental coefficients from
    Wen and Yu, Richardson, Saxena and Vogel, Babu, Grace, and Chitester. This
    approach can be used when bed void fraction and particle sphericity are not
    known. Refer to Equation 25 and Table 4 in Chapter 3 of Kunii and Levenspiel
    [1]_.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    mu : float
        Viscosity of gas [kg/(m s)]
    rhog : float
        Density of gas [kg/m³]
    rhos : float
        Density of bed particle [kg/m³]
    coeff : string
        Keyword to determine which coefficients to use for umf calculation.
        Valid options are 'wenyu', 'rich', 'sax', 'babu', 'grace', and 'chit'.
        Default coefficients are set to 'wenyu'.

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]

    Example
    -------
    >>> umf_coeff(0.0005, 3.6e-5, 0.44, 2500, 'rich')
    0.1192

    References
    ----------
    .. [1] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
       Butterworth-Heinemann, 2nd edition, 1991.
    """

    if coeff == 'wenyu':
        # Wen and Yu coefficients [-]
        a = 33.7
        b = 0.0408
    elif coeff == 'rich':
        # Richardson coefficients [-]
        a = 25.7
        b = 0.0365
    elif coeff == 'sax':
        # Saxena and Vogel coefficients [-]
        a = 25.3
        b = 0.0571
    elif coeff == 'babu':
        # Babu coefficients [-]
        a = 25.3
        b = 0.0651
    elif coeff == 'grace':
        # Grace coefficients [-]
        a = 27.2
        b = 0.0408
    elif coeff == 'chit':
        # Chitester coefficients [-]
        a = 28.7
        b = 0.0494
    else:
        raise ValueError('Coefficient is not a valid option.')

    # g is acceleration due to gravity [m/s²], Ar is Archimedes number [-], and
    # Re is Reynolds number [-]
    g = 9.81
    Ar = (dp**3 * rhog * (rhos - rhog) * g) / (mu**2)
    Re = (a**2 + b * Ar)**0.5 - a

    # minimum fluidization velocity [m/s]
    umf = (Re * mu) / (dp * rhog)
    return umf


def umf_ergun(dp, ep, mu, phi, rhog, rhos):
    """
    Determine minimum fluidization velocity from particle and gas properties.
    This approach is based on the Ergun pressure drop equation for a bed of
    particles. Refer to Equations 18 and 19 in Chapter 3 of Kunii and Levenspiel
    [2]_,

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    ep : float
        Void fraction of the bed [-]
    mu : float
        Viscosity of gas [kg/ms]
    phi : float
        Sphericity of bed particle [-]
    rhog : float
        Density of gas [kg/m³]
    rhos : float
        Density of bed particle [kg/m³]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]

    Example
    -------
    >>> umf_ergun(0.0005, 0.46, 3.6e-5, 0.86, 0.44, 2500)
    0.1488

    References
    ----------
    .. [2] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
       Butterworth-Heinemann, 2nd edition, 1991.
    """

    # g is acceleration from gravity [m/s²]
    # K1, K2, a, b are dimensionless constants [-]
    g = 9.81
    K1 = 1.75 / (ep**3 * phi)
    K2 = 150 * (1 - ep) / (ep**3 * phi**2)
    a = K2 / (2 * K1)
    b = 1 / K1

    # Ar is Archimedes number [-], Re is Reynolds number [-], and umf is minimum
    # fluidization velocity [m/s]
    Ar = ((dp**3) * rhog * (rhos - rhog) * g) / (mu**2)
    Re = ((a**2 + b * Ar)**0.5) - a
    umf = (Re * mu) / (rhog * dp)
    return umf


def umf_reynolds(dp, ep, mu, phi, re, rhog, rhos):
    """

    Calculate minimum fluidization velocity for very small particles where
    Reynolds number < 20 and for very large particles where Reynolds number >
    1000. See Equations 21 and 22 in Chapter 3 of Kunii and Levenspiel [3]_.

    Parameters
    ----------
    dp : float
        Diameter of bed particle [m]
    ep : float
        Void fraction [-]
    mu : float
        Viscosity of gas [kg/ms]
    phi : float
        Sphericity of bed particle [-]
    re : float
        Reynolds number where Re < 20 or Re > 1000 [-]
    rhog : float
        Density of gas [kg/m³]
    rhos : float
        Density of bed particle [kg/m³]

    Returns
    -------
    umf : float
        Minimum fluidization velocity [m/s]

    Example
    -------
    For small Reynolds number where Re = 19

    >>> umf_reynolds(0.0005, 0.46, 3.6e-5, 0.86, 19, 0.44, 2500)
    0.1513

    For large Reynolds number where Re = 1001

    >>> umf_reynolds(0.0005, 0.46, 3.6e-5, 0.86, 1001, 0.44, 2500)
    1.1545

    References
    ----------
    .. [3] Daizo Kunii and Octave Levenspiel. Fluidization Engineering.
       Butterworth-Heinemann, 2nd edition, 1991.
    """

    g = 9.81    # acceleration due to gravity [m/s²]

    if re > 1000:
        umf = np.sqrt((dp * (rhos - rhog) * g * ep**3 * phi) / (1.75 * rhog))
        return umf
    elif re < 20:
        umf = ((dp**2 * (rhos - rhog) * g) / (150 * mu)) * ((ep**3 * phi**2) / (1 - ep))
        return umf
    else:
        raise ValueError('Reynolds number not in applicable range.')
