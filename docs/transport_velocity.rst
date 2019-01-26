Transport velocity
==================

In circulating fluidized bed reactors, particle velocities should exceed the
transport velocity to ensure circulation of solids in the system. According to
Zhang et al., the transport velocity can be calculated from the following
equation

.. math:: U_{TR} = \left( \frac{\mu}{\rho_g d_p} \right) \left(3.23 + 0.23 Ar\right)

where the Archimedes number is defined as

.. math:: Ar = \frac{d_p^3 \rho_g (\rho_s - \rho_g) g}{\mu^2}

Nomenclature
------------

| :math:`Ar` - Archimedes number (-)
| :math:`d_p` - Particle diameter (m)
| :math:`g` - Acceleration due to gravity, 9.81 m/s²
| :math:`\mu` - Gas viscosity (kg/(m s))
| :math:`\rho_g` - Gas density (kg/m³)
| :math:`\rho_s` - Solid particle density (kg/m³)

Source code
-----------

.. automodule:: chemics.transport_velocity
   :members:
