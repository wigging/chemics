Bubble rise velocity
====================

The :code:`ubr_kunii()` function is from the Kunii and Levenspiel book while
the :code:`ubr_holland()` function is from the Holland and Bragg book.

Kunii and Levenspiel
--------------------

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
^^^^^^^^^^^^

| :math:`d_b` - Diameter of sphere having same volume as spherical cap bubble, effective bubble diameter (m)
| :math:`d_t` - Bed or tube diameter (m)
| :math:`g` - Acceleration due to gravity, 9.81 m/s²
| :math:`u_{br}` - Rise velocity of single bubbles in a fluidized bed (m/s)

Holland and Bragg
-----------------

In order to predict the performance of two-phase flow in vertical tubes and
fluidised beds, it is first necessary to study the rate of rise of single
bubbles.

Peebles and Garber (1953) developed a number of models based on emperical data
and theoretical equations (Stoke's Law) to fit four flow regimes of bubbles. Later
Willis (1969) added a fifth region to describe terminal rise velocity from potential
flow theory. A summary of the theory can be found in Holland and Bragg (1995) p234.

**Region 1**

Bubbles behave as buoyant solid spheres, rising vertically.

.. math::
   Re_{b} \leq 2

.. math::
   u_{b} = \frac{2 R_b^2 (\rho_l - \rho_g) g}{9 \mu_l}

**Region 2**

Bubbles raise as spheres, but the drag coefficient is slightly less than that
of a solid of the same volume.

.. math::
   2 < Re_{b} \leq 4.02 G_{1}^{-0.214}

.. math::
   u_{b} = 0.33 g^{0.76} \Bigl(\frac{\rho_l}{\mu_l}\Bigr)^{0.52} R_{b}^{1.28}

**Region 3**

Bubbles are flattened and rise in zig-zag pattern.

.. math::
   4.02 G_{1}^{-0.214} < Re_b \leq 3.10 G_{1}^{-0.25}

.. math::
   u_{b} = 1.35 \Bigl(\frac{\sigma}{\rho_{l}R_b}\Bigr)^{0.5}

**Region 4**

Bubbles rise vertically adopting a mushroom-cap shape.

.. math::
   3.10 G_{1}^{-0.25} < Re_b \leq 2.3 \sqrt{\frac{\sigma}{g \rho_l}}

.. math::
   u_{b} = 1.18 \Bigl(\frac{\sigma g}{\rho_l}\Bigr)^{0.25}

**Region 5**

Large spherical-cap bubbles.

.. math::
   Re_{b} > 2.3 \sqrt{\frac{\sigma}{g \rho_l}}

.. math::
   u_{b} = \sqrt{g R_b}

**Dimensionless Groups:**

.. math::
   Re_b = \frac{2 \rho_{l} u_{b} R_{b} }{\mu_l}

.. math::
   G_{1} = \frac{g \mu_{l}^{4}}{\rho_{l} \sigma^{3}}

Nomenclature
^^^^^^^^^^^^

| :math:`u_b` - The rise velocity (m/s)
| :math:`R_b` - The radius of a sphere having the same volume as the bubble (m)
| :math:`D_e` - The equivalent diameter where :math:`D_e = 2 R_b` (m)
| :math:`\sigma` - The surface tension (dynes/cm)
| :math:`\rho_{l / g}` - The density of the liquid or gass respectively (kg/m³)
| :math:`\mu_l` - The viscosity of the lquid (centiPoise)
| :math:`g` - Gravitational constant = 9.81 (m/s²)
| :math:`Re_b` - Reynolds Number of the bubble (dimensionless)
| :math:`G_1` - Morton Number (dimensionless)

References
----------

1. Daizo Kunii and Octave Levenspiel. Fluidization Engineering. Butterworth-Heinemann, 2nd edition, 1991.
2. F.N. Peebles and H.J. Garber, "Studies on the Motion of Gas Bubbles in Liquids, " Chem. Eng. Progr., no. 2, pp. 88-97, 1953.
3. G.B. Wallis, One-dimensional two phase flow, New York: Mc-Graw-Hill Book Company Inc., 1969.
4. F.A. Holland and R. Bragg, Fluid flow for chemical engineers, 2nd ed., London: Edward Arnold, 1995, p. 234.

Source code
-----------

.. automodule:: chemics.bubble_rise_velocity
   :members:
