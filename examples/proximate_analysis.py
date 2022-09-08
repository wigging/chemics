"""
Proximate analysis values expressed as different bases. Bases are
as-determined (ad), as-received (ar), dry (d), and dry ash-free (daf).
"""

import chemics as cm

# Example 1

prox1 = cm.Proximate([47.26, 40.05, 4.46, 8.23], 'ad')
print('\nGiven ad-basis')
print(prox1)

# Example 2

prox2 = cm.Proximate([39.53, 33.50, 3.73, 23.24], 'ar')
print('\nGiven ar-basis')
print(prox2)

# Example 3

print(f'\nFC wt. % daf value is {prox2.daf_basis[0]}')
