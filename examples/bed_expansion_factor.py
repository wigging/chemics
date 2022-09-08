"""
Example of using the `fbexp()` function to calculate the bed expansion factor
to estimate the expanded bed height and expanded void fraction of a bubbling
fluidized bed reactor.
"""

import chemics as cm

# Parameters
# ----------------------------------------------------------------------------

db = 0.05232    # bed diameter [m]
dp = 0.0004     # diameter of bed particle [m]
emf = 0.46      # void fraction at minimum fluidization [-]
rhog = 0.4413   # density of gas [kg/m³]
rhos = 2500     # density of bed particle [kg/m³]
zmf = 0.1016    # bed height at minimum fluidizaiton [m]

umf = 0.1157    # minimum fluidization velocity [m/s]
us = 3.0 * umf  # superficial gas velocity [m/s]

# Bed expansion
# ----------------------------------------------------------------------------

# bed expansion factor [-]
fbexp = cm.fbexp(db, dp, rhog, rhos, umf, us)

# fluidized bed height [m]
zf = zmf * fbexp

# fluidized void fraction of bed from Eq 14.18, ef (-)
ef = 1 - (1 - emf) / fbexp

# Print results
# ----------------------------------------------------------------------------

print(f"""
--- Parameters ----
zmf = {zmf:.4f} m
emf = {emf:.4f}

--- Results ---
fbexp = {fbexp:.4f}
zf = {zf:.4f} m
ef = {ef:.4f}
""")
