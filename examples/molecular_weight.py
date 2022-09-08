"""
Determine molecular weight of an element, compound, or gas mixture.
"""

import chemics as cm

formula = 'C'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = 'Co'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = 'CH4'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(CO2)2'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = 'Ca(C2H3O2)2'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(NH4)2SO4'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(NH4)(NO3)'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '((NH4)3)'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(((H2O)4)3)8'
mw = cm.mw(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

mw_h2 = cm.mw('H2')
mw_n2 = cm.mw('N2')
mw_mix = cm.mw_mix([mw_h2, mw_n2], [0.8, 0.2])
print(f'Molecular weight of gas mix H₂, N₂ = {mw_mix:.2f} g/mol')
