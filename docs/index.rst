Chemics
=======

The Chemics_ package is a collection of Python functions for conducting
calculations in the field of chemical and fluidization engineering. Source code
for the package is available on GitHub_ and contributions from the community are
encouraged.

Installation
------------

The Anaconda_ distribution of Python is recommended for scientific computing.
After installing Anaconda, the Chemics package can be downloaded and installed
with the pip package manager:

.. code-block:: bash

   pip install chemics

Usage
-----

The example below imports the Chemics package then uses the :code:`rhog()`
function to calculate the density of a gas based on its molecular weight,
pressure, and temperature.

.. code-block:: python

    import chemics as cm
    cm.rhog(28, 170100, 773)

An example of calculating the terminal velocity of a particle according to the
Haider and Levenspiel 1989 paper is shown below.

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

More examples are available in the chemics-examples_ repository.

Documentation
-------------

Details about the functions available in the Chemics package are provided below.
Equations and associated references used to develop the functions are also
given.

.. toctree::
   :maxdepth: 1

   atomic_elements
   bed_expansion_factor
   bubble_velocity
   choking_velocity
   conversions
   devol_time
   gas_density
   gas_thermal_conductivity
   gas_viscosity
   geldart
   minimum_fluidization_velocity
   molecular_weight
   terminal_velocity
   transport_velocity

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
.. _chemics: https://github.com/chemics/chemics
.. _contributing: https://github.com/chemics/chemics/blob/master/CONTRIBUTING.md
.. _chemics-examples: https://github.com/chemics/chemics-examples
.. _github: https://github.com/chemics/chemics
