Chemical equation
=================

The ``ChemicalEquation`` class provides product and reactant properties from an equation that represents a chemical reaction.

.. doctest::

   >>> eq = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')

   # Check if atomic elements of the reactants and products are balanced
   >>> eq.is_balanced()
   True

   # Total number of atomic elements for each product
   >>> eq.prod_elements
   {'Na': 2.0, 'Cl': 2.0, 'H': 2.0}

   # Total number of moles for the products
   >>> eq.prod_moles
   3.0

   # Total mass of the products
   >>> eq.prod_mass
   118.896

   # Total number of atomic elements for each reactant
   >>> eq.rct_elements
   {'H': 2.0, 'Cl': 2.0, 'Na': 2.0}

   # Total number of moles for the reactants
   >>> eq.rct_moles
   4.0

   # Total mass of the reactants
   >>> eq.rct_mass
   118.896...

   # Properties of the products
   >>> eq.prod_properties
                 NaCl        H2
   moles          2.0       1.0
   species       NaCl        H2
   molwt        58.44     2.016
   mass        116.88     2.016
   molfrac   0.666667  0.333333
   massfrac  0.983044  0.016956

   # Properties of the reactants
   >>> eq.rct_properties
                  HCl        Na
   moles          2.0       2.0
   species        HCl        Na
   molwt       36.458     22.99
   mass        72.916     45.98
   molfrac        0.5       0.5
   massfrac  0.613275  0.386725

Names can be assigned to chemical species using the ``names`` parameter.

.. doctest::

   >>> names = {'CHAR': 'C', 'CH2OHCHO': 'C2H4O2'}
   >>> eq = cm.ChemicalEquation('5 NaCl + 3 H2O -> CH4 + 2.2 CHAR + CH2OHCHO', names)
   >>> eq.prod_elements
   {'C': 5.2, 'H': 8.0, 'O': 2.0}
