"""
Compare choking velocity correlations.
"""

import chemics as cm
import numpy as np
import matplotlib.pyplot as py
from matplotlib.ticker import FormatStrFormatter
from scipy.optimize import fsolve

# Parameters
# ------------------------------------------------------------------------------

# for rounded sand from Table 3, Row 4 in Zhang 2015 paper
dp = 0.000084   # diameter of 84 um sand particle, m
rhop = 2260     # density of sand particle, kg/m^3
rhog = 1.225    # density of air, kg/m^3
ut = 0.46       # terminal velocity of particles, m/s
utr = 2.56      # transport velocity of particles, m/s
Ar = 48         # Archimedes number, -
ug = 1.983e-5   # viscosity of air, kg/(m s)
D = 0.1         # internal pipe or riser diameter about 4 inch, m

# range of solids flux to evaluate choking velocity, kg/(m^2 s)
G = np.linspace(1, 1000, 1000)

# Calculate Choking Velocities
# ------------------------------------------------------------------------------

uch_leung = cm.uch_leung(G, rhop, ut)               # Leung 1971 choking velocity
uch_yousfi = cm.uch_yousfi(dp, G, rhog, ug, ut)     # Yousfi 1974 choking velocity
uch_matsen = cm.uch_matsen(G, rhop, ut)             # Matsen 1982 choking velocity
uch_bifan = cm.uch_bifan(Ar, dp, G, rhog)           # Bi and Fan 1991 choking velocity
uch_zhang = cm.uch_zhang(Ar, dp, G, rhog)           # Zhang 2015 choking velocity

ng = len(G)     # number of solid flux to evaulate choking velocity
uch_yang = np.empty(ng)     # store choking velocity from Yang 1975
uch_punwani = np.empty(ng)  # store choking velocity from Punwani 1976
uch_psri = np.empty(ng)     # store choking velocity from PSRI 2016

for idx, g in enumerate(G):

    # Yang 1975 choking velocity
    _, uc_yang = fsolve(cm.uch_yang, [0.5, 5], (D, g, rhop, ut))
    uch_yang[idx] = uc_yang

    # Punwani 1976 choking velocity
    # this will be similar to Yang 1975 at pressures near 0.075 lb/ft^3
    _, uc_punwani = fsolve(cm.uch_punwani, [0.5, 5], (D, g, rhop, rhog * 0.062427961, ut))
    uch_punwani[idx] = uc_punwani

    # PSRI 2016 choking velocity
    uc_psri, = fsolve(cm.uch_psri, 5, (dp, D, g, rhog, rhop, ut))
    uch_psri[idx] = uc_psri * 0.3048  # convert uch in ft/s to m/s

# Plot
# ------------------------------------------------------------------------------
py.ion()
py.close('all')


def despine():
    """ remove right and top axes """
    ax = py.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    py.tick_params(bottom='off', top='off', left='off', right='off')


py.figure(1)
py.plot(uch_leung, G, lw=2, label='Leung 1971')
py.plot(uch_yousfi, G, lw=2, label='Yousfi 1974')
py.plot(uch_yang, G, lw=2, label='Yang 1975')
py.plot(uch_punwani, G, 'o', markevery=20, mew=2, mfc='none', label='Punwani 1976')
py.plot(uch_matsen, G, lw=2, label='Matsen 1982')
py.plot(uch_bifan, G, lw=2, label='Bi and Fan 1991')
py.plot(uch_zhang, G, lw=2, label='Zhang 2015')
py.plot(uch_psri, G, c='orange', lw=2, label='PSRI 2016')
py.xlabel('U, gas velocity, m/s')
py.xlim([0, 12])
py.ylim([1, 1000])
py.yscale('log')
py.ylabel('G, solids flux, $\mathregular{kg/(m^2s)}$')
py.gca().yaxis.set_tick_params(pad=8)
py.legend(loc='lower right', numpoints=1)
py.gca().yaxis.set_major_formatter(FormatStrFormatter("%g"))
py.grid(which='both')
despine()

# py.savefig('uch.pdf', bbox_inches='tight')
