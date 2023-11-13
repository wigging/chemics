Chemics
=======

The Chemics_ package is a collection of Python functions for performing calculations in the field of chemical engineering. Source code for the package is available on GitHub_ and contributions from the community are encouraged.

Installation
------------

If you don't have Python installed on your computer, the Anaconda_ or Miniconda_ distribution of Python is recommended for scientific computing. After setting up Python, the Chemics package can be downloaded and installed using the pip or conda package managers.

Install Chemics using the pip package manager:

.. code-block:: bash

   $ pip install chemics

Usage
-----

The example below imports the chemics package and creates a :code:`Gas` class to calculate the density of nitrogen gas at a pressure of 101,325 Pa and 773 K.

.. code-block:: python

   import chemics as cm

   gas = cm.Gas('N2')
   rho = gas.density(101325, 773)
   print(rho)

   # This prints a value of 0.4416


This example uses the :code:`ChemicalEquation` class to get properties of the reactants and products from a given chemical equation.

.. code-block:: python

   import chemics as cm

   ce = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
   ce.balance

   # Returns True for balanced equation

   ce.rct_properties

   # Returns a dataframe of the reactant properties
   #                HCl        Na
   # moles            2         2
   # species        HCl        Na
   # molwt       36.458     22.99
   # mass        72.916     45.98
   # molfrac        0.5       0.5
   # massfrac  0.613275  0.386725

See the `examples <https://github.com/wigging/chemics>`_ directory in the GitHub repository for more examples.

.. toctree::
   :maxdepth: 1
   :caption: Examples

   examples/biomass_composition
   examples/chemical_equation
   examples/conversions
   examples/dimensionless
   examples/gas_properties
   examples/gas_mixture
   examples/analysis
   examples/pyrolysis_number
   examples/wood_properties

.. toctree::
   :maxdepth: 1
   :caption: API documentation

   api/atm_pressure
   api/atomic_elements
   api/biomass_composition
   api/chemical_equation
   api/conversions
   api/dimensionless_numbers
   api/gas
   api/gas_mixture
   api/liquid
   api/molecular_weight
   api/proximate_analysis
   api/ultimate_analysis
   api/wood

Contributing
------------

See the CONTRIBUTING_ document on GitHub for guidelines on contributing to the Chemics package.

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
