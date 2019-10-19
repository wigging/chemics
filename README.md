# Chemics

The [Chemics][] package is a collection of Python functions for conducting calculations in the field of chemical and fluidization engineering. Source code for the package is available on [GitHub][] and contributions from the community are encouraged.

## Installation

The [Anaconda][] or [Miniconda][] distribution of Python is recommended for scientific computing. After setting up Python, the Chemics package can be downloaded and installed with the `pip` package manager:

```bash
pip install chemics
```

## Usage

The example below imports the Chemics package then uses the `rhog()` function to calculate the density of a gas based on its molecular weight, pressure, and temperature.

```python
import chemics as cm
cm.rhog(28, 101325, 773)    # returns 0.4414
```

The `ut()` function calculates the terminal velocity of a particle according to the Haider and Levenspiel 1989 paper as shown below.

```python
import chemics as cm

# Parameters
dp = 0.00016    # particle diameter [m]
mu = 1.8e-5     # gas viscosity [kg/(m s)]
phi = 0.67      # particle sphericity [-]
rhog = 1.2      # gas density [kg/m^3]
rhos = 2600     # particle density [kg/m^3]

# Haider and Levenspiel terminal velocity [m/s]
# this assigns a value of 0.8857 to `ut_haider`
ut_haider = cm.ut_haider(dp, mu, phi, rhog, rhos)
```

Use the `ChemicalEquation` class to get properties of the reactants and products from a given chemical equation.

```python
import chemics as cm

ce = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')

ce.balance          # returns True for balanced equation
ce.rct_mol_fracs    # returns [0.5, 0.5] for mole fractions of reactants

print(ce)
# prints properties of reactants and products to screen as
# eq                 2 HCl + 2 Na -> 2 NaCl + H2
# names              None
# balance            True
#
# reactants          ['2 HCl', '2 Na']
# rct_species        ['HCl', 'Na']
# rct_moles          [2. 2.]
# rct_mw             [36.458 22.99 ]
# rct_mass           [72.916 45.98 ]
# rct_elements       {'H': 2.0, 'Cl': 2.0, 'Na': 2.0}
# rct_sum_moles      4.0
# rct_sum_mass       118.8960
# rct_mol_fracs      [0.5 0.5]
# rct_mass_fracs     [0.61327547 0.38672453]
#
# products           ['2 NaCl', 'H2']
# prod_species       ['NaCl', 'H2']
# prod_moles         [2. 1.]
# prod_mw            [58.44   2.016]
# prod_mass          [116.88    2.016]
# prod_elements      {'Na': 2.0, 'Cl': 2.0, 'H': 2.0}
# prod_sum_moles     3.0
# prod_sum_mass      118.896
# prod_mol_fracs     [0.66666667 0.33333333]
# prod_mass_fracs    [0.983044 0.016956]

ce.reactant_props('Na')
# returns properties for the reactant `Na`
# {'moles': 2.0,
#  'mw': 22.99,
#  'mass': 45.98,
#  'mol_frac': 0.5,
#  'mass_frac': 0.3867}

ce.product_props('NaCl')
# returns properties for the product `NaCl`
# {'moles': 2.0,
#  'mw': 58.44,
#  'mass': 116.88,
#  'mol_frac': 0.66,
#  'mass_frac': 0.983}
```

More examples are available in the [chemics-examples][] repository.

## Documentation

Documentation for the Chemics package is available at [chemics.github.io](https://chemics.github.io).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for guidelines on contributing to the Chemics package.

## License

Chemics is available under the MIT License - see the [LICENSE](LICENSE) file for more information.


[anaconda]: https://www.anaconda.com
[chemics]: https://pypi.org/project/chemics/
[chemics-examples]: https://github.com/chemics/chemics-examples
[github]: https://github.com/chemics/chemics
[miniconda]: https://conda.io/miniconda.html
