Chemics
=======

The Chemics_ Python package is a collection of functions for conducting
calculations in the field of chemical engineering. Source code for the package
is available on GitHub_ and contributions from the community are encouraged.


Installation
------------

The Anaconda_ distribution of Python is recommended for scientific computing.
After installing Anaconda, the Chemics package can be downloaded and installed
with the pip package manager:

.. code-block:: bash

   pip install chemics

Usage
-----

Functions in the Chemics package are called with the usual dot syntax for
accessing module features. The example below imports the Chemics package then
uses the :code:`rhog()` function to calculate the density of a gas based on its
molecular weight, pressure, and temperature.

.. code-block:: python

    import chemics as cm
    cm.rhog(28, 170100, 773)

Documentation
-------------

Details about the functions available in the Chemics package are provided at the
pages listed below. Equations and associated references used to develop the
functions are also given.

.. toctree::
   :maxdepth: 1

   conversions
   elements
   gas-density
   gas-thermal-conductivity
   gas-viscosity
   molecular-weight

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
.. _github: https://github.com/chemics/chemics
