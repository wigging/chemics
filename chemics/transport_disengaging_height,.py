import numpy as np


def tdhDecayConstant(dp):
    """
    Calculates the transport disengagement decay constant given the particle
    diameter and superficial velocity. The correlation is a curve fit to data
    in K/L Fig. 7.12. Maximum particle diameter on plot is 800 um, and maximum
    superficial velocity is 1.25 m/s.

    Parameters
    ----------
    dp : float
        Particle diameter [m]

    Returns
    -------
    a_us : float
        Transport disengagement decay constant (1/m) multiplied by the
        superficial velocity (m/s) for a product with units [1/s]
    """

    # This is the raw data that we use to fit the trend line to. It has been
    # read off the graph in a rather sophisticated manner. The graph was
    # scanned from the K/L book, and then the coordinates (in pixels) at select
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
        Transport disengagement height [m]

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


def tdhHeight(a, x):
    """
    Calculates the transport disengagement height for the specified decay
    constant and fraction of upward solids flux at that height. It assumes
    total reflux (no solids elutriation).

    Parameters
    ----------
    a : float
        Decay constant [1/m]
    x : float
        Fraction of entrained solids at the TDH [-]

    Returns
    -------
    tdh : float
        Transport disengagement height [m]
    """
    tdh = -np.log(x) / a
    return tdh
