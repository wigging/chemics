Conversions
===========

Convert a list of mass fractions ``y`` to mole fractions where ``mw`` is the molecular weight in g/mol for each component. In this example, the components represent C, H, O, and N.

.. doctest::

   >>> y = [0.36, 0.16, 0.20, 0.28]
   >>> mw = [12.011, 1.008, 15.999, 14.007]
   >>> cm.massfrac_to_molefrac(y, mw)
   array([0.135..., 0.717..., 0.0565..., 0.0903...])

Convert a list of mole fractions ``x`` to mass fractions.

.. doctest::

   >>> x = [0.36, 0.16, 0.20, 0.28]
   >>> mw = [12.011, 1.008, 15.999, 14.007]
   >>> cm.molefrac_to_massfrac(x, mw)
   array([0.372..., 0.0138..., 0.275..., 0.337...])
