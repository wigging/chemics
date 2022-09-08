"""
Estimate thermal conductivity of wood based on basic specific gravity,
volumetric shrinkage and moisture content.
"""

import chemics as cm

# Parameters
# ---------------------------------------------------------------------------

gb = 0.54   # basic specific gravity [-]
so = 12.3   # volumetric shrinkage [%]
x = 10      # moisture content [%]

# Wood thermal conductivity
# ---------------------------------------------------------------------------

k = cm.k_wood(0.54, 12.3, 10)

print(f'k = {k:.4f} W/mK')
