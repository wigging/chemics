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
