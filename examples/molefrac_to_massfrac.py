"""
Convert from mole fractions to mass fractions.
"""

import chemics as cm

# Parameters
# ----------------------------------------------------------------------------

# mole fractions x [-] and molecular weights mw [g/mol] for C, H, O, N
x = [0.36, 0.16, 0.20, 0.28]
mw = [12.011, 1.008, 15.999, 14.007]

# Calculate mole fractions
# ----------------------------------------------------------------------------

y = cm.molefrac_to_massfrac(x, mw)

print('y =', y.round(3))
