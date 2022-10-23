Chemics
=======

The Chemics_ package is a collection of Python functions for performing
calculations in the field of chemical engineering. Source code for the
package is available on GitHub_ and contributions from the community are
encouraged.

Installation
------------

If you don't have Python installed on your computer, the Anaconda_ or
Miniconda_ distribution of Python is recommended for scientific computing.
After setting up Python, the Chemics package can be downloaded and installed
using the pip or conda package managers.

Install Chemics using the pip package manager:

.. code-block:: bash

   $ pip install chemics

Usage
-----

The example below imports the Chemics package then uses the :code:`rhog()`
function to calculate the density of a gas based on its molecular weight,
pressure, and temperature.

.. code-block:: python

    import chemics as cm

    cm.rhog(28, 170100, 773)

Use the :code:`ChemicalEquation` class to get properties of the reactants and
products from a given chemical equation.

.. code-block:: python

    import chemics as cm

    ce = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')

    ce.balance
    # returns True for balanced equation

    ce.rct_properties
    # returns a dataframe of the reactant properties
    #                HCl        Na
    # moles            2         2
    # species        HCl        Na
    # molwt       36.458     22.99
    # mass        72.916     45.98
    # molfrac        0.5       0.5
    # massfrac  0.613275  0.386725

See the `examples <https://github.com/wigging/chemics>`_ directory in the GitHub repository for more examples.

Documentation
-------------

Details about the functions available in the Chemics package are provided below.
Equations and associated references used to develop the functions are also
given.

.. toctree::
   :maxdepth: 1

   atomic_elements
   biomass_composition
   chemical_equation
   conversions
   dimensionless_numbers
   gas_density
   gas_heat_capacity
   gas_thermal_conductivity
   gas_viscosity
   liquid_heat_capacity
   molecular_weight
   proximate_analysis
   ultimate_analysis
   wood_heat_capacity
   wood_thermal_conductivity

Contributing
------------

See the CONTRIBUTING_ document on GitHub for guidelines on contributing to the
Chemics package.

Package index and modules
-------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _anaconda: https://www.anaconda.com
.. _chemics: https://pypi.org/project/chemics/
.. _contributing: https://github.com/wigging/chemics/blob/main/CONTRIBUTING.md
.. _github: https://github.com/wigging/chemics
.. _miniconda: https://conda.io/miniconda.html
