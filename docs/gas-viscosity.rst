Gas viscosity
=============

Viscosity of gas as a function of temperature can be calculated from the
following equation:

.. math:: \mu_{gas} = A + B\,T + C\,T^2 + D\,T^3

where coefficients A, B, C, and D are obtained from tables in the Yaws' Handbook
for inorganic and organic compounds. The :code:`mu_gas_inorganic` function in
the Chemics package supports 372 gas species while the :code:`mu_gas_organic`
function supports 7,031 species. At a minimum, the functions require formula
name and temperature as input parameters; however, the CAS number is also needed
as an input if more than one form of a species exists.

Nomenclature
------------

| :math:`\mu_{gas}` - Viscosity of gas (:math:`\mu P`)
| :math:`A, B, C, D` - Coefficients from Yaws' Handbook (-)
| :math:`T` - Temperature (K)

Source code
-----------

.. automodule:: chemics.gas_viscosity
   :members:
