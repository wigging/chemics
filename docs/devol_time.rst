Devolatilization time
=====================

A correlation to estimate the conversion time of cylindrical beech wood
particles in a sand bed fluidized by nitrogen gas was developed by Colomba Di
Blasi and Carmen Branca. The correlation is an empirical power-law relation
corresponding to a conversion of 95% (also referred to as a devolatilization
time of 95%). It was developed from experiments conducted at fast pyrolysis
conditions where bed temperatures varied from 712-1107 K and particle diameters
ranged from 2-10 mm. According to the Di Blasi and Carmen article, similar
correlations exist for coal particles.

.. math:: t_v = 0.8\,e^{1525 / T_r} d^{1.2}

Nomenclature
------------

| :math:`t_v` - conversion time, devolatilization time of 95% (s)
| :math:`T_r` - Temperature of fluidized bed (K)
| :math:`d` - Diameter of wood particle (mm)

Source code
-----------

.. automodule:: chemics.devol_time
   :members:
