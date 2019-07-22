import numpy as np


def tdh_chan(ug):
    """
    Calculate transport disengaging height (TDH) based on the Chan and Knowlton
    correlation [1]_. This function is based on the equation presented in the
    Cahyadi [2]_ review article

    .. math:: TDH = 0.85\\,{U_g}^{1.2} (7.33 - 1.2 \\log U_g)

    where :math:`U_g` is superficial gas velocity. According to Table 1 in the
    Cahyadi review paper, this corrleation is relevant for Geldart A and B sand
    particles with a density of 2595 kg/m³, mean particle size of 37-420 µm,
    and an inner diameter fluidizing column of 0.3 m.

    Parameters
    ----------
    ug : float
        Superficial gas velocity [m/s]

    Returns
    -------
    tdh : float
        Transport disengaging height [m]

    Example
    -------
    >>> tdh_chan(0.3)
    1.7587

    References
    ----------
    .. [1] I.H. Chan and T.M. Knowlton. The effect of system pressure on the
       transport disengaging height (TDH) above bubbling gas-fluidized beds.
       AIChE Symp. Ser., vol. 80, no. 241, 1984.
    .. [2] Andy Cahyadi, Anthony H. Neumayer, Christine M. Hrenya, Ray A. Cocco,
       and Jia Wei Chew. Comparative study of Transport Disengaging Height (TDH)
       correlations in gas–solid fluidization. Powder Technology, vol. 275,
       pp. 220-238, 2015.
    """
    tdh = 0.85 * (ug**1.2) * (7.33 - 1.2 * np.log(ug))
    return tdh


def tdh_horio(dc, ug):
    """
    Calculate transport disengaging height (TDH) based on the Horio et al.
    correlation [3]_. This function is based on the equation presented in the
    Cahyadi [4]_ review article

    .. math:: TDH = (2.7\\, {D_c}^{-0.36} - 0.7) D_c\\, \\textrm{exp}(0.74\\, U_g\\, D_c^{-0.23})

    where :math:`D_c` is inner diameter of the fluidizing column and
    :math:`U_g` is superifical gas velocity. According to Table 1 in the
    Cahyadi review paper, this corrleation is relevant for Geldart group A
    particles.

    Parameters
    ----------
    dc : float
        Inner diameter of fluidizing column [m]
    ug : float
        Superficial gas velocity [m/s]

    Returns
    -------
    tdh : float
        Transport disengaging height [m]

    Example
    -------
    >>> tdh_horio(0.05, 0.3)
    0.563

    References
    ----------
    .. [3] M. Horio, T. Shibata, and I. Muchi. Design criteria for the fluidized
       bed freeboard. 4th International Conference on Fluidization in Kashikojima,
       Japan, 1983.
    .. [4] Andy Cahyadi, Anthony H. Neumayer, Christine M. Hrenya, Ray A. Cocco,
       and Jia Wei Chew. Comparative study of Transport Disengaging Height (TDH)
       correlations in gas–solid fluidization. Powder Technology, vol. 275,
       pp. 220-238, 2015.
    """
    tdh = ((2.7 * dc**-0.36) - 0.7) * dc * np.exp(0.74 * ug * dc**-0.23)
    return tdh
