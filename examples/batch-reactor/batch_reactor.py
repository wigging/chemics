"""
Determine biomass composition from the C and H fractions obtained from
ultimate analysis data. Use the biomass composition in a Cantera batch reactor
model. Chemical species and reactions are defined in the `debiagi.cti` file.
"""

import cantera as ct
import matplotlib.pyplot as plt
import numpy as np
import chemics as cm

# suppress warnings about discontinuity in thermo data
ct.suppress_thermo_warnings()

# Parameters
# ----------------------------------------------------------------------------

yc = 0.534  # carbon mass fraction [-]
yh = 0.06   # hydrogen mass fraction [-]

tk = 873.15     # reactor temperature [K]
p = 101325.0    # reactor pressure [Pa]

# Determine biomass composition from C and H
# ----------------------------------------------------------------------------

bc = cm.biocomp(yc, yh, printcomp=True)

cell = bc['y_daf'][0]
hemi = bc['y_daf'][1]
ligc = bc['y_daf'][2]
ligh = bc['y_daf'][3]
ligo = bc['y_daf'][4]
tann = bc['y_daf'][5]
tgl = bc['y_daf'][6]

# Use biomass composition in a batch reactor
# ----------------------------------------------------------------------------

# time scale to evaluate reaction rates [s]
time = np.linspace(0, 2.0, 100)

# initialize gas phase
gas = ct.Solution('debiagi.cti')

y0 = {'CELL': cell, 'GMSW': hemi, 'LIGC': ligc, 'LIGH': ligh, 'LIGO': ligo, 'TANN': tann, 'TGL': tgl}
gas.TPY = tk, p, y0

# simulate batch reactor
r = ct.IdealGasReactor(gas, energy='on')

sim = ct.ReactorNet([r])
states = ct.SolutionArray(gas, extra=['t'])

for tm in time:
    sim.advance(tm)
    states.append(r.thermo.state, t=tm)

# Plot results
# ----------------------------------------------------------------------------


def config(ax, xlabel, ylabel):
    ax.grid(True, color='0.9')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    ax.set_frame_on(False)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(color='0.9')


fig, ax = plt.subplots(tight_layout=True)
ax.plot(states.t, states.T)
ax.grid(True, color='0.9')
ax.set_frame_on(False)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Temperature [K]')
ax.tick_params(color='0.9')

fig, ax = plt.subplots(tight_layout=True)
ax.plot(states.t, states('CELL').Y[:, 0], label='CELL')
ax.plot(states.t, states('GMSW').Y[:, 0], label='GMSW')
ax.plot(states.t, states('LIGC').Y[:, 0], label='LIGC')
ax.plot(states.t, states('LIGH').Y[:, 0], label='LIGH')
ax.plot(states.t, states('LIGO').Y[:, 0], label='LIGO')
ax.plot(states.t, states('TANN').Y[:, 0], label='TANN')
ax.plot(states.t, states('TGL').Y[:, 0], label='TGL')
config(ax, xlabel='Time [s]', ylabel='Mass fraction [-]')

fig, ax = plt.subplots(tight_layout=True)
ax.plot(states.t, states('CELLA').Y[:, 0], label='CELLA')
ax.plot(states.t, states('HCE1').Y[:, 0], label='HCE1')
ax.plot(states.t, states('HCE2').Y[:, 0], label='HCE2')
ax.plot(states.t, states('LIGCC').Y[:, 0], label='LIGCC')
ax.plot(states.t, states('LIGOH').Y[:, 0], label='LIGOH')
ax.plot(states.t, states('LIG').Y[:, 0], label='LIG')
config(ax, xlabel='Time [s]', ylabel='Mass fraction [-]')

species = states.species_names
ys = [states(sp).Y[:, 0][-1] for sp in species]
ypos = np.arange(len(species))

fig, ax = plt.subplots(figsize=(6.4, 8), tight_layout=True)
ax.barh(ypos, ys, align='center')
ax.set_xlabel('Mass fraction [-]')
ax.set_ylim(min(ypos) - 1, max(ypos) + 1)
ax.set_yticks(ypos)
ax.set_yticklabels(species)
ax.invert_yaxis()
ax.set_axisbelow(True)
ax.set_frame_on(False)
ax.tick_params(color='0.8')
ax.xaxis.grid(True, color='0.8')

plt.show()
