# Chemics

The [Chemics][] package is a collection of Python functions for conducting
calculations in the field of chemical and fluidization engineering. Source code
for the package is available on [GitHub][] and contributions from the community
are encouraged.

## Installation

The [Anaconda][] or [Miniconda][] distribution of Python is recommended for
scientific computing. After setting up Python, the Chemics package can be
downloaded and installed with the `pip` package manager:

```bash
pip install chemics
```

## Usage

The example below imports the Chemics package then uses the `rhog()`
function to calculate the density of a gas based on its molecular weight,
pressure, and temperature.

```python
import chemics as cm
cm.rhog(28, 170100, 773)
```

An example of calculating the terminal velocity of a particle according to the
Haider and Levenspiel 1989 paper is shown below.

```python
import chemics as cm

# Parameters
dp = 0.00016    # particle diameter [m]
mu = 1.8e-5     # gas viscosity [kg/(m s)]
phi = 0.67      # particle sphericity [-]
rhog = 1.2      # gas density [kg/m^3]
rhos = 2600     # particle density [kg/m^3]

# Haider and Levenspiel terminal velocity [m/s]
ut_haider = cm.ut_haider(dp, mu, phi, rhog, rhos)
```

More examples are available in the [chemics-examples][] repository.

## Documentation

Documentation for the Chemics package is available at
[chemics.github.io](https://chemics.github.io).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for guidelines on
contributing to the Chemics package.

## License

Chemics is available under the MIT License - see the [LICENSE](LICENSE) file for
more information.


[anaconda]: https://www.anaconda.com
[chemics]: https://pypi.org/project/chemics/
[chemics-examples]: https://github.com/chemics/chemics-examples
[github]: https://github.com/chemics/chemics
[miniconda]: https://conda.io/miniconda.html
