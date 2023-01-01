"""
Determine viscosity of a gas at temperature or for a range of temperatures.
"""

import chemics as cm

# Determine viscosity of gas at temperature [K]
# ----------------------------------------------------------------------------

mu_h2 = cm.mu_gas('H2', 773.15)
mu_n2 = cm.mu_gas('N2', 773.15)
mu_ch4 = cm.mu_gas('CH4', 773.15)

# Determine viscosity of a gas mixture
# ----------------------------------------------------------------------------

mu_mix = cm.mu_graham([mu_h2, mu_n2, mu_ch4], [0.4, 0.1, 0.5])

# Print results
# ----------------------------------------------------------------------------

print(f'mu_n2 = {mu_n2:.2f} µP')
print(f'mu_n2 = {mu_n2/1e7:.5g} kg/(m s)')
print(f'mu_mix = {mu_mix:.2f} µP')
