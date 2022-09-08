"""
Convert from mass fractions to mole fractions.
"""

import chemics as cm

# Parameters
# ----------------------------------------------------------------------------

# mass fractions y [-] and molecular weights mw [g/mol] for C, H, O, N
y = [0.36, 0.16, 0.20, 0.28]
mw = [12.011, 1.008, 15.999, 14.007]

# Calculate mole fractions
# ----------------------------------------------------------------------------

x = cm.massfrac_to_molefrac(y, mw)

print('x =', x.round(3))
