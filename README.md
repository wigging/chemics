# Chemics

The [Chemics][] Python package is a collection of functions for conducting
calculations in the field of chemical engineering. Source code for the package
is available on [GitHub][] and contributions from the community are encouraged.

## Installation

The [Anaconda][] or [Miniconda][] distribution of Python is recommended for
scientific computing. After setting up Python, the Chemics package can be
downloaded and installed with the `pip` package manager:

```bash
pip install chemics
```

## Usage

Functions in the Chemics package are called with the usual dot syntax for
accessing module features. The example below imports the Chemics package as `cm`
then uses the `rhog()` function to calculate the density of a gas based on its
molecular weight, pressure, and temperature.

```python
import chemics as cm
cm.rhog(28, 170100, 773)
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
