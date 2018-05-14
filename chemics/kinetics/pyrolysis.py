"""
Pyrolysis kinetic schemes
"""

import numpy as np


def papadikis(wood, gas, tar, char, T, dt, s=1):
    """
    Primary and secondary kinetic reactions as shown in Papadikis 2010 paper.
    Also refer to the papers by Liden 1988 and Blasi 1993.

    Parameters
    ----------
    wood = wood concentration, kg/m^3
    gas = gas concentation, kg/m^3
    tar = tar concentation, kg/m^3
    char = char concentation, kg/m^3
    T = temperature, K
    dt = time step, s
    s = 1 primary reactions only, 2 primary and secondary reactions

    Returns
    -------
    nwood = new wood concentration, kg/m^3
    ngas = new gas concentration, kg/m^3
    ntar = new tar concentration, kg/m^3
    nchar = new char concentration, kg/m^3
    """

    # A = pre-factor (1/s) and E = activation energy (kJ/mol)
    A1 = 1.3e8;     E1 = 140    # wood -> gas
    A2 = 2e8;       E2 = 133    # wood -> tar
    A3 = 1.08e7;    E3 = 121    # wood -> char
    A4 = 4.28e6;    E4 = 108    # tar -> gas
    A5 = 1e6;       E5 = 108    # tar -> char
    R = 0.008314    # universal gas constant, kJ/mol*K

    # reaction rate constant for each reaction, 1/s
    K1 = A1 * np.exp(-E1 / (R * T))  # wood -> gas
    K2 = A2 * np.exp(-E2 / (R * T))  # wood -> tar
    K3 = A3 * np.exp(-E3 / (R * T))  # wood -> char
    K4 = A4 * np.exp(-E4 / (R * T))  # tar -> gas
    K5 = A5 * np.exp(-E5 / (R * T))  # tar -> char

    if s == 1:
        # primary reactions only
        rw = -(K1+K2+K3)*wood     # wood rate
        rg = K1*wood              # gas rate
        rt = K2*wood              # tar rate
        rc = K3*wood              # char rate
        nwood = wood + rw*dt        # update wood concentration
        ngas = gas + rg*dt        # update gas concentration
        ntar = tar + rt*dt        # update tar concentration
        nchar = char + rc*dt        # update char concentration
    elif s == 2:
        # primary and secondary reactions
        rw = -(K1+K2+K3)*wood         # wood rate
        rg = K1*wood + K4*tar          # gas rate
        rt = K2*wood - (K4+K5)*tar     # tar rate
        rc = K3*wood + K5*tar          # char rate
        nwood = wood + rw*dt        # update wood concentration
        ngas = gas + rg*dt        # update gas concentration
        ntar = tar + rt*dt        # update tar concentration
        nchar = char + rc*dt        # update char concentration

    # return new wood, gas, tar, char mass concentrations, kg/m^3
    return nwood, ngas, ntar, nchar
