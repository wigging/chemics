Bed expansion factor
====================

The bed expansion factor can be used to estimate the expanded bed height of a
bubbling fluidized bed reactor. Two equations are given in the Souza-Santos book
based on the diameter of the bed.

For :math:`d_D < 0.0635` m:

.. math:: f_{bexp} = 1 + \frac{1.032\,(U-U_{mf})^{0.57}\;\rho_{GA}^{0.083}}{\rho_p^{0.166}\,U_{mf}^{0.063}\,d_D^{0.445}}

For :math:`d_D \geq 0.0635` m:

.. math:: f_{bexp} = 1 + \frac{14.314\,(U-U_{mf})^{0.738}\;d_p^{1.006}\,\rho_p^{0.376}}{\rho_{GA}^{0.126}\;U_{mf}^{0.937}}

Nomenclature
------------

| :math:`d_D` - Diameter of the bed (m)
| :math:`d_p` - Diameter of the bed particle (m)
| :math:`f_{bexp}` - Bed expansion factor (-)
| :math:`\rho_{GA}` - Gas density (kg/m³)
| :math:`\rho_p` - Particle density (kg/m³)
| :math:`U` - Gas superficial velocity (m/s)
| :math:`U_{mf}` - Minimimum fluidization velocity (m/s)

Source code
-----------

.. automodule:: chemics.bed_expansion_factor
   :members:
