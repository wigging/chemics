"""
Comparison of different correlations to calculate the minimum fluidization
velocity of particles in a fluidized bed using the `umf_coeff`, `ufm_ergun`,
and `umf_reynolds` functions.
"""

import chemics as cm

# Parameters
# ----------------------------------------------------------------------------

# particle properties
dp = 0.0005   # diameter of bed particle [m]
rhos = 2500   # density of bed particle [kg/m³]

# air properties at T=300K and P=1atm -> rho=1.17 kg/m^3, ug=1.85e-5 kg/ms
# N2 properties at T=773K and P=1atm -> rho=0.44 kg/m^3, ug=3.6e-5 kg/ms
mu = 3.6e-5     # dynamic viscosity of gas [kg/ms]
rhog = 0.44     # density of gas [kg/m³]

# void fraction and sphericity for the Ergun equation
ep = 0.46    # void fraction [-]
phi = 0.86   # sphericity [-]

# Umf calculations
# ----------------------------------------------------------------------------

# Wen and Yu, Richardson, Saxena and Vogel, Babu, Grace, and Chitester
umf_wenyu = cm.umf_coeff(dp, mu, rhog, rhos)
umf_rich = cm.umf_coeff(dp, mu, rhog, rhos, 'rich')
umf_sax = cm.umf_coeff(dp, mu, rhog, rhos, 'sax')
umf_babu = cm.umf_coeff(dp, mu, rhog, rhos, 'babu')
umf_grace = cm.umf_coeff(dp, mu, rhog, rhos, 'grace')
umf_chit = cm.umf_coeff(dp, mu, rhog, rhos, 'chit')

# Ergun function
umf_ergun = cm.umf_ergun(dp, ep, mu, phi, rhog, rhos)

# Small particles where Re < 20
umf_small_re = cm.umf_reynolds(dp, ep, mu, phi, 19, rhog, rhos)

# Large particles where Re > 1000
umf_large_re = cm.umf_reynolds(dp, ep, mu, phi, 1001, rhog, rhos)

# Print results
# ----------------------------------------------------------------------------

print(f"""
Umf = {umf_wenyu:.4f} m/s \tWen and Yu
Umf = {umf_rich:.4f} m/s \tRichardson
Umf = {umf_sax:.4f} m/s \tSaxena and Vogel
Umf = {umf_babu:.4f} m/s \tBabu
Umf = {umf_grace:.4f} m/s \tGrace
Umf = {umf_chit:.4f} m/s \tChitester
Umf = {umf_ergun:.4f} m/s \tErgun
Umf = {umf_small_re:.4f} m/s \tSmall Re
Umf = {umf_large_re:.4f} m/s \tLarge Re
""")
