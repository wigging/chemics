Chemics
=======

The Chemics_ package is a collection of Python functions for performing
calculations in the field of chemical and fluidization engineering. Source
code for the package is available on GitHub_ and contributions from the
community are encouraged.

Installation
------------

If you don't have Python installed on your computer, the Anaconda_ or
Miniconda_ distribution of Python is recommended for scientific computing.
After setting up Python, the Chemics package can be downloaded and installed
using the pip or conda package managers.

Install Chemics using the pip package manager:

.. code-block:: bash

   $ pip install chemics

Install Chemics using the conda package manager:

.. code-block:: bash

   $ conda config --add channels conda-forge
   $ conda install chemics

Usage
-----

The example below imports the Chemics package then uses the :code:`rhog()`
function to calculate the density of a gas based on its molecular weight,
pressure, and temperature.

.. code-block:: python

    import chemics as cm

    cm.rhog(28, 170100, 773)

The :code:`ut()` function calculates the terminal velocity of a particle
according to the Haider and Levenspiel 1989 paper as shown below.

.. code-block:: python

    import chemics as cm

    # Parameters
    dp = 0.00016    # particle diameter [m]
    mu = 1.8e-5     # gas viscosity [kg/(m s)]
    phi = 0.67      # particle sphericity [-]
    rhog = 1.2      # gas density [kg/m^3]
    rhos = 2600     # particle density [kg/m^3]

    # Haider and Levenspiel terminal velocity [m/s]
    ut_haider = cm.ut_haider(dp, mu, phi, rhog, rhos)

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

More examples are available in the `chemics-examples`_ repository.

Documentation
-------------

Details about the functions available in the Chemics package are provided below.
Equations and associated references used to develop the functions are also
given.

.. toctree::
   :maxdepth: 1

   atomic_elements
   bed_expansion_factor
   biomass_composition
   bubble_rise_velocity
   chemical_equation
   choking_velocity
   conversions
   devol_time
   dimensionless_numbers
   gas_density
   gas_heat_capacity
   gas_thermal_conductivity
   gas_viscosity
   geldart
   minimum_fluidization_velocity
   molecular_weight
   pressure_drop
   proximate_bases
   terminal_velocity
   transport_disengaging_height
   transport_velocity
   ultimate_bases
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
.. _contributing: https://github.com/chemics/chemics/blob/master/CONTRIBUTING.md
.. _chemics-examples: https://github.com/chemics/chemics-examples
.. _github: https://github.com/chemics/chemics
.. _miniconda: https://conda.io/miniconda.html
