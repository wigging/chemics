Installation
============

If you don't have Python installed on your computer, the `Anaconda <https://www.anaconda.com>`_ or `Miniconda <https://conda.io/miniconda.html>`_ distribution of Python is recommended for scientific computing. After setting up Python, the Chemics package can be downloaded and installed using the pip package manager.

Install Chemics using the pip package manager:

.. code-block:: bash

   pip install chemics

Usage
=====

The example below imports the chemics package and creates a ``Gas`` class to calculate the density of nitrogen gas at a pressure of 101,325 Pa and 773 K.

.. code-block:: python

   import chemics as cm

   gas = cm.Gas('N2')
   rho = gas.density(101325, 773)
   print(rho)
   # This prints a value of 0.4416


This example uses the ``ChemicalEquation`` class to get properties of the reactants and products from a given chemical equation.

.. code-block:: python

   import chemics as cm

   ce = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
   ce.balance
   # The returns True for balanced equation

   ce.rct_properties
   # This returns a dataframe of the reactant properties
   #                HCl        Na
   # moles            2         2
   # species        HCl        Na
   # molwt       36.458     22.99
   # mass        72.916     45.98
   # molfrac        0.5       0.5
   # massfrac  0.613275  0.386725

See the **Examples** section for more ways to use Chemics.
