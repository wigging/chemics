Dimensionless numbers
=====================

The examples below demonstrate various dimensionless number functions availabe in chemics.

Reynolds number
---------------

Use the ``reynolds()`` function to calculate the Reynolds number.

.. testcode::

   u = 2.6     # flow speed in m/s
   d = 0.025   # characteristic length or dimension in meters
   rho = 910   # density of the fluid or gas in kg/m³
   mu = 0.38   # dynamic viscosity of the fluid or gas in kg/(m⋅s)

   re = cm.reynolds(u, d, rho=rho, mu=mu)
   print(f'Reynolds number Re is {re:.2f}')

.. testoutput::

   Reynolds number Re is 155.66

The kinematic viscosity can be used as an input parameter instead of the density and dynamic viscosity.

.. testcode::

   u = 0.25      # flow speed in m/s
   d = 0.102     # characteristic length or dimension in meters
   nu = 1.4e-6   # kinematic viscosity of the fluid or gas in m²/s

   re = cm.reynolds(u, d, nu=nu)
   print(f'Reynolds number Re is {re:.2f}')

.. testoutput::

   Reynolds number Re is 18214.29
