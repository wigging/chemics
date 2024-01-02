Gas properties
==============

Gas properties such as molecular weight, density, heat capacity, thermal conductivity, and viscosity can be calculated using the ``Gas`` class. The example given below calculates nitrogen gas properties at 773 K and 101,325 Pa which is the default pressure.

.. testcode::

   import chemics as cm

   gas = cm.Gas('N2', 773)
   mw = gas.molecular_weight
   rho = gas.density()
   cp = gas.heat_capacity()
   k = gas.thermal_conductivity()
   mu = gas.viscosity()

   print('Nitrogen gas properites')
   print(f'molecular weight      {mw:.2f} g/mol')
   print(f'density               {rho:.3f} kg/m³')
   print(f'heat capacity         {cp:.2f} J/(mol⋅K)')
   print(f'thermal conductivity  {k:.3f} W/(m⋅K)')
   print(f'viscosity             {mu:.2f} microPoise (μP)')

This prints the output shown below.

.. testoutput::

   Nitrogen gas properites
   molecular weight      28.01 g/mol
   density               0.442 kg/m³
   heat capacity         31.24 J/(mol⋅K)
   thermal conductivity  0.054 W/(m⋅K)
   viscosity             363.82 microPoise (μP)
