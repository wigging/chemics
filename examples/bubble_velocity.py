"""
Example of using the bubble rise velocity function `ubr()` to determine the
rise velocity of single bubbles in a fluidized bed.
"""

import chemics as cm

# Parameters
# ----------------------------------------------------------------------------

db = 0.05   # effective bubble diameter [m]
dt = 0.6    # fluidized bed diameter [m]

# Bubble rise velocity
# ----------------------------------------------------------------------------

ubr = cm.ubr(db, dt)
ubr2 = cm.ubr(db, 0.1)  # where db/dt = 0.5

# Print results
# ----------------------------------------------------------------------------

print(f"""
--- Parameters ----
db = {db:.2f} m
dt = {dt:.2f} m

--- Results ---
ubr = {ubr:.4f} m/s
ubr = {ubr * 100:.4f} cm/s
ubr2 = {ubr2:.4f} m/s
ubr2 = {ubr2 * 100:.4f} cm/s
""")
