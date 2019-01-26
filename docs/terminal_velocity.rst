Terminal velocity
=================

An individual particle can be carried by a stream of gas when the gas velocity
exceeds the termnial velocity :math:`u_t` of the particle. However, in
fluidized bed reactors, entrainment of particles out of the bed may require a
gas velocity many times higher than the terminal velocity. The sections below
discuss different approaches for calculating :math:`u_t`.

Kunii and Levenspiel 1991
-------------------------

Kunii and Levenspiel provide an expression for the terminal velocity of a
particle as shown below where :math:`C_D` is an experimentally determined drag
coefficient.

.. math:: u_t = \left( \frac{4 d_p\, (\rho_s - \rho_g) g}{3 \rho_g\, C_D} \right)^{1/2}

Haider and Levenspiel 1989
--------------------------

To determine the terminal velocity for a range of particle sphericities, Haider
and Levenspiel first define two dimensionless quantities

.. math:: d_{*} = d_p \left[ \frac{g\, \rho_g (\rho_s - \rho_g)}{\mu^2} \right]^{1/3}

.. math:: u_* = \left[ \frac{18}{d{_*}^2} + \frac{2.3348 - 1.7439\, \phi}{d{_*}^{0.5}} \right]^{-1}

where :math:`0.5 \leq \phi \leq 1` and particle diameter :math:`d_p` is an
equivalent spherical diameter, the diameter of a sphere having the same volume
as the particle. The relationship between :math:`u_*` and :math:`u_t` is given
by

.. math:: u_* = u_t \left[ \frac{\rho{_g}^2}{g\, \mu\, (\rho_s - \rho_g)} \right]^{1/3}

The terminal velocity of the particle can finally be determined by rearranging
the above equation such that

.. math:: u_t = u_* \left[ \frac{g\, \mu\, (\rho_s - \rho_g)}{\rho{_g}^2} \right]^{1/3}

Ganser 1993
-----------

The Ganser paper proposed a drag coefficient for spherical and nonspherical
particles

.. math::
   C_d &= \frac{24}{Re\, K_1} \left( 1 + 0.1118 (Re\, K_1 K_2)^{0.6567} \right) + \frac{0.4305 K_2}{1 + \frac{3305}{Re\, K_1 K_2}} \\
   K_1 &= \left( \frac{1}{3} + \frac{2}{3}\phi \right) \\
   K_2 &= 10^{1.8148 (-log\, \phi)^{0.5743}}

where K₁ is Stokes' shape factor and K₂ is Newton's shape factor. The Cui 2007
and Chhabra 1999 papers leave out the :math:`-2.25*d_v/D` term in the shape
factor equations. According to Chhabra 1999, the Ganser drag correlation is
applicable to :math:`0.09 \leq \phi \leq 1`.

The Reynolds number and drag coefficient can be written in terms of the
terminal velocity of the particle. Finally, by comparing the drag coefficient
equations for a range of terminal velocities, :math:`u_t` can be estimated from
the system of equations.

.. math::
   Re &= \frac{d_p\, \rho_g\, u_t}{\mu} \\
   C_d &= \frac{4\, d_p\, g\, (\rho_s - \rho_g)}{3\, {u_t}^2\, \rho_g}

Nomenclature
------------

| :math:`d_*` - Dimensionless particle diameter (-)
| :math:`d_p` - Diameter of the particle or equivalent spherical diameter (m)
| :math:`g` - Gravitational constant as 9.81 m/s²
| :math:`\mu` - Viscosity of the fluid (kg/(m s))
| :math:`\phi` - Sphericity of the particle (-)
| :math:`\rho_g` - Density of the gas (kg/m³)
| :math:`\rho_s` - Density of the particle (kg/m³)
| :math:`u_*` - Dimensionless particle velocity (-)
| :math:`u_t` - Terminal velocity of a particle (m/s)

Source code
-----------

.. automodule:: chemics.terminal_velocity
   :members:
