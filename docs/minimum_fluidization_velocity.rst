Minimum fluidization velocity
=============================

For a bed of particles, the minimum fluidization velocity is the gas velocity at
which the drag force of the upward moving gas equals the weight of the
particles. As discussed in Chapter 3 of the Kunnii and Levenspiel book, the
minimum fluidization velocity (:math:`u_{mf}`) can be calculated from the
equation shown below. This formula is based on the Ergun pressure drop equation
for a bed of particles.

.. math:: \frac{1.75}{\epsilon_{mf}^3 \phi} \left( \frac{d_p u_{mf} \rho_g}{\mu} \right)^2 + \frac{150(1-\epsilon_{mf})}{\epsilon_{mf}^3 \phi^2} \left( \frac{d_p u_{mf} \rho_g}{\mu} \right) = \frac{d_p^3 \rho_g (\rho_s - \rho_g) g}{\mu^2}

The above equation can be written in terms of the Reynolds and Archimedes
numbers as follows

.. math:: \frac{1.75}{\epsilon_{mf}^3 \phi} Re_{p, mf}^2 + \frac{150 (1 - \epsilon_{mf})}{\epsilon_{mf}^3 \phi^2} Re_{p, mf} = Ar

where

.. math:: Ar = \frac{d_p^3 \rho_g (\rho_s - \rho_g) g}{\mu^2}

.. math:: Re_{p,mf} = \frac{d_p u_{mf} \rho_g}{\mu}

Kunii and Levenspiel further simplify the equation to the following form

.. math:: K_1 Re_{p,mf}^2 + K_2 Re_{p,mf} = Ar

where

.. math:: K_1 = \frac{1.75}{\epsilon_{mf}^3 \phi}

.. math:: K_2 = \frac{150(1-\epsilon_{mf})}{\epsilon_{mf}^3 \phi^2}

Solving for the Reynolds number provides

.. math:: Re_{p,mf} = \left( a^2 + b Ar \right)^{1/2} - a

where

.. math:: a = \frac{K_2}{2 K_1}

.. math:: b = \frac{1}{K_1}

Finally, the minimum fluidization velocity can be calculated from the above
Reynolds number as

.. math:: u_{mf} = \frac{Re_{p,mf} \mu}{d_p \rho_g}

For very small particles where Re < 20, the above equation can be simplified to

.. math:: u_{mf} = \frac{d_p^2 (\rho_s - \rho_g) g}{150 \mu} \frac{\epsilon_{mf}^3 \phi^2}{1 - \epsilon_{mf}}

and for large particles where Re > 1000, the following equation can be used

.. math:: u_{mf}^2 = \frac{d_p (\rho_s - \rho_g) g}{175 \rho_g} \epsilon_{mf}^3 \phi

When void fraction and sphericity are not known, values for :math:`a` and
:math:`b` from Table 4 in Chapter 3 of Kunii and Levenspiel can be used to
estimate :math:`u_{mf}`.

Nomenclature
------------

| :math:`a`, :math:`b` - dimensionless constants (-)
| :math:`Ar` - Archimedes number (-)
| :math:`d_p` - Particle diameter (m)
| :math:`\epsilon_{mf}` - Bed void fraction at minimum fluidizing conditions (-)
| :math:`g` - Acceleration due to gravity, 9.81 m/s²
| :math:`K_1`, :math:`K_2` - dimensionless constants (-)
| :math:`\mu` - Gas viscosity (kg/(m s))
| :math:`\phi` - Sphericity of a particle (-)
| :math:`\rho_g` - Gas density (kg/m³)
| :math:`\rho_s` - Solid particle density (kg/m³)

Source code
-----------

.. automodule:: chemics.minimum_fluidization_velocity
   :members:
