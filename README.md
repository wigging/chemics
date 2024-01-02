# Chemics

Chemics is a Python package for chemistry and chemical engineering applications. It is open-source and contributions from the scientific community are encouraged.

## Installation

If you don't have Python installed on your computer, the [Anaconda](https://www.anaconda.com) or [Miniconda](https://conda.io/miniconda.html) distribution of Python is recommended for scientific computing. After setting up Python, the Chemics package can be downloaded and installed using the pip package manager.

```bash
$ pip install chemics
```

## Usage

The example below imports the Chemics package and uses the `Gas` class to calculate the density and viscosity of nitrogen gas at a temperature of 773 K and pressure of 101,325 Pa.

```python
import chemics as cm

gas = cm.Gas("N2", 773)
rho = gas.density()
mu = gas.viscosity()

print("Nitrogen gas properties at 773 K and 101,325 Pa")
print(f"density    {rho:.4f} kg/m³")
print(f"viscosity  {mu:.2f} μP")
```

This prints the following:

```
Nitrogen gas properties at 773 K and 101,325 Pa
density    0.4416 kg/m³
viscosity  363.82 μP
```

This example uses the `ChemicalEquation` class to get properties of the reactants and products from a given chemical equation.

```python
import chemics as cm

ce = cm.ChemicalEquation("2 HCl + 2 Na -> 2 NaCl + H2")
ce.is_balanced()
# This returns True for balanced equation

ce.rct_properties
# This returns a dataframe of the reactant properties
#                HCl        Na
# moles            2         2
# species        HCl        Na
# molwt       36.458     22.99
# mass        72.916     45.98
# molfrac        0.5       0.5
# massfrac  0.613275  0.386725
```

More examples are available in the documentation.

## Documentation

Documentation for the Chemics package is available at [chemics.readthedocs.io](https://chemics.readthedocs.io).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for guidelines on contributing to the Chemics package.

## License

Chemics is available under the MIT License - see the [LICENSE](LICENSE) file for more information.
