"""
Use the Biot and pyrolysis numbers PyI and PyII to create a regime map for a
biomass particle.
"""

import chemics as cm
import matplotlib.pyplot as plt

# Parameters
# ----------------------------------------------------------------------------

h = 500         # convective heat transfer coefficient in W/(m²⋅K)
d = 0.00001     # biomass particle diameter in meters
k = 0.12        # biomass thermal conductivity in W/(m⋅K)

kr = 1.4        # reaction rate constant in 1/s
rho = 540       # biomass density in kg/m³
cp = 3092.8     # biomass heat capacity in J/(kg⋅K)

# Biot and pyrolysis numbers
# ----------------------------------------------------------------------------

r = d / 2
biot = cm.biot(h, r, k)
pyI = cm.pyroI(k, kr, rho, cp, r)
pyII = cm.pyroII(h, kr, rho, cp, r)

if biot < 1.0:
    py = pyII
else:
    py = pyI

# Print
# ----------------------------------------------------------------------------

print(f'biot = {biot:.4f}')
print(f'pyI = {pyI:.2f}')
print(f'pyII = {pyII:.2f}')

# Plot
# ----------------------------------------------------------------------------

fig, ax = plt.subplots(tight_layout=True)
ax.plot(biot, py, 'r^')
ax.set_xlabel('Biot Number, Bi [-]')
ax.set_ylabel('Pyrolysis Number, Py [-]')

ax.text(0.2, 0.91, 'kinetics limited\nisothermal', ha='center', transform=ax.transAxes)
ax.text(0.8, 0.91, 'kinetics limited\nnon-isothermal', ha='center', transform=ax.transAxes)
ax.text(0.2, 0.03, 'convection limited', ha='center', transform=ax.transAxes)
ax.text(0.8, 0.03, 'conduction limited', ha='center', transform=ax.transAxes)

ax.axvline(1, c='k', ls='-.')
ax.axvspan(10**-1, 10**1, color='0.9')
ax.axhline(1, c='k', ls='-.')
ax.axhspan(10**-1, 10**1, color='0.9')
ax.grid(color='0.9')
ax.set_frame_on(False)
ax.set_xlim(10**-4, 10**4)
ax.set_ylim(10**-4, 10**4)
ax.set_xscale('log')
ax.set_yscale('log')
ax.tick_params(color='0.9')
plt.minorticks_off()

plt.show()
