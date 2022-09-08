"""
Estimate the transport disengaging height using the `tdh_chan()` and
`tdh_horio()` equations.
"""

import chemics as cm

# Parameters
# ---------------------------------------------------------------------------

dc = 0.05   # inner diameter of fluidizing column [m]
ug = 0.3    # superficial gas velocity [m/s]

# Chan and Knowlton transport disengaging height
# ---------------------------------------------------------------------------

tdh_chan = cm.tdh_chan(0.3)

# Horio et al. transport disengaging height
# ---------------------------------------------------------------------------

tdh_horio = cm.tdh_horio(0.05, 0.3)

# Print results
# ---------------------------------------------------------------------------

print(f"""
tdh_chan = {tdh_chan:.4f} m (Chan and Knowlton)
tdh_horio = {tdh_horio:.4f} m (Horio et al.)
""")
