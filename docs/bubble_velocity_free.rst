Free Bubble Velocity
====================

In order to predict the performance of two-phase flow in vertical tubes and
fluidised beds, it is first necessary to study the rate of rise of single 
bubbles.

Peebles and Garber (1953) developed a number of models based on emperical data
and theoretical equations (Stoke's Law) to fit four flow regimes of bubbles. Later 
Willis (1969) added a fifth region to describe terminal rise velocity from potential
flow theory. A summary of the theory can be found in Holland and Bragg (1995) p234.


Region 1:
Bubbles behave as buoyant solid spheres, rising vertically.

..math::
	Re_{b} \leq 2

..math::
	u_{b} = \frac{2R_b^{2}-(\rho_l}-\rho_g)}{9\mu_l}

Region 2:
Bubbles raise as spheres, but the drag coefficient is slightly less than that
of a solid of the same volume.

..math::
	2 < Re_{b} \leq 3.10G_{1}^{-0.214}

..math::
	u_{b} = 0.33g^{0.76}(frac{\rho_l}{\mu_l})^{0.52}R_{b}^{1.28}


Region 3:
Bubbles are flattened and rise in zig-zag patter.

..math::
	4.02G_{1}^{-0.214} < Re_b\leq3.10G_{1}^{-0.25}

..math::
	u_{b} = 1.35 (\frac{\sigma}{\rho_{l}R_b})^{0.5}


Region 4:
Bubbles rise vertically adopting a mushroom-cap shape.

..math::
	Re_b < 3.10G_{1}^{-0.25}

..math::
	u_{b} = 1.53(\frac{\sigma g}{\rho_l})^{0.25}


Region 5:
Large spherical-cap bubbles.

..math::
	Re_{b} \geq 2.3 sqrt{\frac{\sigma}{g \rho_l}}

..math::
	u_{b} = sqrt{g R_b}


Dimensionless Groups:
..math::
	Re_b = \frac{2 \rho_{l} u_{b} R_{b} }{\mu_l}

..math::
	G_{1} = \frac{g \mu_{l}^{4}}{\rho_{l} \sigma^{3}}

Nomenclature
------------
| :math:`u_b` - The raise velocity (m/s)
| :math:`R_b` - The radius of a sphere having the same volume as the bubble (m)
| :math:`D_e = 2 R_b` - The equivalent diameter (m)
| :math:`\sigma` - The surface tension (dynes/cm)
| :math:`\rho_{l / g}` - The density of the liquid or gass respectively (kg/m^3)
| :math:`\mu_l` - The viscosity of the lquid (centiPoise)
| :math:`g` - Gravitational constant = 9.81 (m/s^2)
| :math:`Re_b` - Reynolds Number of the bubble (dimensionless)
| :math:`G_1` - Morton Number (dimensionless)

References
----------
[1] 	F. N. Peebles and H. J. Garber, "Studies on the Motion of Gas Bubbles in 
	Liquids, " Chem. Eng. Progr., no. 2, pp. 88-97, 1953. 

[2]	G. B. Wallis, One-dimensional two phase flow, New York: Mc-Graw-Hill 
	Book Company Inc., 1969. 

[3]	F. A. Holland and R. Bragg, Fluid flow for chemical engineers, 2nd ed.,
	London: Edward Arnold, 1995, p. 234.
    

Source code
-----------

.. automodule:: chemics.bubble_velocity_free
   :members:
