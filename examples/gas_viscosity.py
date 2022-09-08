"""
Determine viscosity of a gas at temperature or for a range of temperatures.
"""

import chemics as cm
import matplotlib.pyplot as plt
import numpy as np

# Determine viscosity of gas at temperature [K]
# ----------------------------------------------------------------------------

mu_h2 = cm.mu_gas('H2', 773.15)
mu_n2 = cm.mu_gas('N2', 773.15)
mu_ch4 = cm.mu_gas('CH4', 773.15)

# Determine viscosity of a gas mixture
# ----------------------------------------------------------------------------

mu_mix = cm.mu_graham([mu_h2, mu_n2, mu_ch4], [0.4, 0.1, 0.5])

# Use coefficients to plot viscosity for range of temperatures [K]
# ----------------------------------------------------------------------------

results = cm.mu_gas('CH4', 833, full=True)

mu_ch4 = results[0]
tmin = results[2]
tmax = results[3]
a, b, c, d = results[4:]

tk = np.arange(tmin, tmax + 1)
mu_ch4_tk = a + b * tk + c * (tk**2) + d * (tk**3)

# Print results
# ----------------------------------------------------------------------------

print(f'mu_n2 = {mu_n2:.2f} µP')
print(f'mu_n2 = {mu_n2/1e7:.5g} kg/(m s)')
print(f'mu_mix = {mu_mix:.2f} µP')

# Plot results
# ----------------------------------------------------------------------------

fig, ax = plt.subplots(tight_layout=True)
ax.plot(tk, mu_ch4_tk)
ax.set_xlabel('Temperature [K]')
ax.set_ylabel(r'Gas Viscosity [µP]')
ax.set_title(r'Plot of CH$_4$ viscosity vs temperature')

plt.show()
