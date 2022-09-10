# Chemics

The chemics package is a collection of Python functions for performing calculations in the field of chemical reactor engineering. Source code for the package is available on GitHub and contributions from the community are encouraged.

## Installation

If you don't have Python installed on your computer, the [Anaconda](https://www.anaconda.com) or [Miniconda](https://conda.io/miniconda.html) distribution of Python is recommended for scientific computing. After setting up Python, the chemics package can be downloaded and installed using the pip package manager.

```bash
$ pip install chemics
```

## Usage

The example below imports the chemics package then uses the `rhog()` function to calculate the density of a gas based on its molecular weight, pressure, and temperature.

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
```

More examples are available in the `examples` directory.

## Documentation

Documentation for the chemics package is available at [chemics.readthedocs.io](https://chemics.readthedocs.io).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for guidelines on contributing to the Chemics package.

## License

Chemics is available under the MIT License - see the [LICENSE](LICENSE) file for more information.
