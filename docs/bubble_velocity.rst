Bubble velocity (Kunii)
=======================

As stated in the Kunii and Levenspiel book, the bubble rise velocity in a dense
bed can be calculated as

.. math::
   u_{br} = 0.711(g d_b)^{1/2} \quad \text{where} \quad d_b/d_t < 0.125

Wall effects can slow the rise of bubbles when :math:`d_b/d_t > 0.125`;
as such, the rise velocity is calculated as

.. math::
   u_{br} = \left[0.711(g d_b)^{1/2}\right]1.2\,exp\left(-1.49
   \frac{d_b}{d_t}\right) \quad \text{where} \quad 0.125 < d_b/d_t < 0.6

For conditions where :math:`d_b/d_t > 0.6`, the fluidized bed is considered to
be slugging.

Nomenclature
------------

| :math:`d_b` - Diameter of sphere having same volume as spherical cap bubble, effective bubble diameter (m)
| :math:`d_t` - Bed or tube diameter (m)
| :math:`g` - Acceleration due to gravity, 9.81 m/s²
| :math:`u_{br}` - Rise velocity of single bubbles in a fluidized bed (m/s)

Source code
-----------

.. automodule:: chemics.bubble_velocity
   :members:
