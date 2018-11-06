Gas thermal conductivity
========================

Thermal conductivity of gas as a function of temperature is calculated from the
following equation:

.. math:: k_{gas} = A + B\,T + C\,T^2 + D\,T^3

where coefficients A, B, C, and D are obtained from tables in the Yaws' Handbook
for inorganic and organic compounds. The equation should not be used for
temperatures outside the range specified for a particular gas species.

Nomenclature
------------

| :math:`k_{gas}` - Thermal conductivity of gas [W/(m K)]
| :math:`A, B, C, D` - Coefficients from Yaws' Handbook (-)
| :math:`T` - Temperature (K)

Source code
-----------

.. automodule:: chemics.gas_thermal_conductivity
   :members:
