Gas mixture properties
======================

This example calculates the molecular weight and viscosity of a gas mixture using the ``GasMixture`` class. The gas mixture is initialized with a list of ``Gas`` objects and their associated mole fractions.

.. testcode::

   import chemics as cm

   gas1 = cm.Gas('H2', 773)
   gas2 = cm.Gas('N2', 773)
   gas3 = cm.Gas('CH4', 825)

   gas_mixture = cm.GasMixture([gas1, gas2, gas3], [0.4, 0.1, 0.5])
   mw = gas_mixture.molecular_weight()
   mu = gas_mixture.viscosity()

   print('Gas mixture properties')
   print(f'molecular weight  {mw:.2f} g/mol')
   print(f'viscosity         {mu:.2f} microPoise (μP)')

This prints the output shown below.

.. testoutput::

   Gas mixture properties
   molecular weight  11.63 g/mol
   viscosity         226.75 microPoise (μP)
