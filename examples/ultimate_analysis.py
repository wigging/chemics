"""
Ultimate analysis values expressed as different bases. Bases are
as-determined (ad), as-received (ar), dry (d), and dry ash-free (daf).
"""

import chemics as cm

# Example 1

ult1 = cm.Ultimate([60.08, 5.44, 25.01, 0.88, 0.73, 7.86, 9.00], 'ad')
print('\nGiven ad-basis')
print(ult1)

# Example 2

ult2 = cm.Ultimate([46.86, 6.70, 39.05, 0.69, 0.57, 6.13, 29.02], 'ar')
print('\nGiven ar-basis')
print(ult2)

# Example 3

ult3 = cm.Ultimate([46.86, 3.46, 13.27, 0.69, 0.57, 6.13, 29.02], 'ar', HO=False)
print('\nGiven ar-basis, HO false')
print(ult3)

# Example 4

print(f'\nN wt. % dry value is {ult3.d_basis[3]}')
