Wood properties
===============

The example below uses the ``cp_wood()`` function to calculate heat capacity of wood with 12% moisture content at a temperature of 340 Kelvin.

.. doctest::

   >>> cp = cm.cp_wood(12, 340)
   >>> print(f'cp is {cp:.4f} kJ/(kg⋅K)')
   cp is 1.9146 kJ/(kg⋅K)

This example estimates thermal conductivity of wood with a basic specific gravity of 0.54, volumetric shrinkage of 12.3%, and 10% moisture content.

.. doctest::

   >>> k = cm.k_wood(0.54, 12.3, 10)
   >>> print(f'k is {k:.4f} W/(m⋅K)')
   k is 0.1567 W/(m⋅K)
