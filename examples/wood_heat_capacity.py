"""
Determine heat capacity of wood.
"""

import chemics as cm

# Parameters
# ---------------------------------------------------------------------------

x = 12      # Moisture content [%]
tk = 340    # Temperature [K]

# Wood heat capacity
# ---------------------------------------------------------------------------

cp = cm.cp_wood(x, tk)

print(f'cp = {cp:.4f} kJ/(kg K)')
