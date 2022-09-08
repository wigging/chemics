"""
Determine the time for 95% devolatilization of a wood particle.
"""

import chemics as cm

# Calculate devolatilization time to 95% conversion
# ----------------------------------------------------------------------------

dp = 2.0        # diameter of wood particle [mm]
tbed = 773.15   # temperatue of the fluidized bed [K]

dtime = cm.devol_time(dp, tbed)  # devol. time for 95% conversion [s]

print(f'devolatilization time = {dtime:.4f} s')
