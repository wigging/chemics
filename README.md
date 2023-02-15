# Chemics

Chemics is a Python package for chemistry and chemical engineering applications. It is open-source and contributions from the scientific community are encouraged.

## Installation

If you don't have Python installed on your computer, the [Anaconda](https://www.anaconda.com) or [Miniconda](https://conda.io/miniconda.html) distribution of Python is recommended for scientific computing. After setting up Python, the chemics package can be downloaded and installed using the pip package manager.

```bash
$ pip install chemics
```

## Usage

The example below imports the chemics package and creates a `Gas` class to calculate the density of nitrogen gas at a pressure of 101,325 Pa and 773 K.

```python
import chemics as cm

gas = cm.Gas('N2')
rho = gas.rho(101325, 773)
print(rho)

# This prints a value of 0.4416
```

This example uses the `ChemicalEquation` class to get properties of the reactants and products from a given chemical equation.

```python
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
```

More examples are available in the `examples` directory and in the documentation.

## Documentation

Documentation for the chemics package is available at [chemics.readthedocs.io](https://chemics.readthedocs.io).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for guidelines on contributing to the Chemics package.

## License

Chemics is available under the MIT License - see the [LICENSE](LICENSE) file for more information.
