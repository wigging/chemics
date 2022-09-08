"""
The `ChemicalEquation` class provides product and reactant properties from a
chemical reaction equation.
"""

import chemics as cm

# Example 1
# ---------------------------------------------------------------------------

ce1 = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')

print('\n--- Example 1 ---')
print('2 HCl + 2 Na -> 2 NaCl + H2')
print(f'Equation is balanced: {ce1.balance}')
print(f'\nTotal product elements: {ce1.prod_elements}')
print(f'Total product moles: {ce1.prod_moles}')
print(f'Total product mass: {ce1.prod_mass:.4f}')
print(f'\nTotal reactant elements: {ce1.rct_elements}')
print(f'Total reactant moles: {ce1.rct_moles}')
print(f'Total reactant mass: {ce1.rct_mass:.4f}')
print('\nProduct properties:\n', ce1.prod_properties)
print('\nReactant properties:\n', ce1.rct_properties)

# Example 2
# ---------------------------------------------------------------------------

eq2 = '5 NaCl + 3 H2O -> CH4 + 2.2 CHAR + CH2OHCHO'
names2 = {'CHAR': 'C', 'CH2OHCHO': 'C2H4O2'}
ce2 = cm.ChemicalEquation(eq2, names2)

print('\n--- Example 2 ---')
print('5 NaCl + 3 H2O -> CH4 + 2.2 CHAR + CH2OHCHO')
print(f'Equation is balanced: {ce2.balance}')
print(f'\nTotal product elements: {ce2.prod_elements}')
print(f'Total product moles: {ce2.prod_moles}')
print(f'Total product mass: {ce2.prod_mass:.4f}')
print(f'\nTotal reactant elements: {ce2.rct_elements}')
print(f'Total reactant moles: {ce2.rct_moles}')
print(f'Total reactant mass: {ce2.rct_mass:.4f}')
print('\nProduct properties:\n', ce2.prod_properties)
print('\nReactant properties:\n', ce2.rct_properties)
