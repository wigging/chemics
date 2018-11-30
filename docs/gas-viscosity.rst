Gas viscosity
=============

Gas viscosity as a function of temperature can be calculated from the following
equation:

.. math:: \mu_{gas} = A + B\,T + C\,T^2 + D\,T^3

where coefficients A, B, C, and D are obtained from tables in the Yaws' Handbook
for inorganic and organic compounds. The Chemics function supports 372 inorganic
gas species and 7,031 organic gas species. At a minimum, the function requires
the formula name and temperature as input parameters; however, the CAS number
may be needed as an input if more than one form of a species exists.

Nomenclature
------------

| :math:`\mu_{gas}` - Viscosity of gas (:math:`\mu P`)
| :math:`A, B, C, D` - Coefficients from Yaws' Handbook (-)
| :math:`T` - Temperature (K)

Source code
-----------

.. automodule:: chemics.gas_viscosity
   :members:
