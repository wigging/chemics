# Chemics

Chemics is a Python package for developing reactor models.

:warning: This package is still under development. Official release will be announced at a later date. Public contributions will also be accepted once a more complete version of the package is available.

Questions and other feedback can be submitted on the [Issues](https://github.com/ccpcode/chemics/issues) page.

[![PyPI version](https://badge.fury.io/py/chemics.svg)](https://badge.fury.io/py/chemics) [![Anaconda-Server Badge](https://anaconda.org/wigging/chemics/badges/downloads.svg)](https://anaconda.org/wigging/chemics)

## Getting Started

### Requirements

The [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) distribution of Python is preferred for scientific applications.

- Python 3
- NumPy

### Installation and Usage

Several options are available to install the chemics package.

Download from GitHub
1. download or clone this repository from GitHub
2. copy the chemics subfolder into your Python project

Install locally with pip
1. download or clone this repository from GitHub
2. from within the chemics folder, run `pip install -e .` to install the package to your local machine

Options to install from [PyPi](https://pypi.org) via `pip` and from [Anaconda](https://anaconda.org) via `conda` will be available soon.

Functions in the chemics package are called with the usual dot syntax for accessing module features. The example below calculates the density of a gas based on its molecular weight, pressure, and temperature.

```python
import chemics as cm
cm.rhog(28, 170100, 773)
```

## Modules

**bfb** - functions for modeling bubbling fluidized bed (BFB) reactors.

**gas** - gas properties such as atmospheric pressure, density, thermal
conductivity, and viscosity.

**rtd** - functions for residence time distribution.

**util** - dimensionless numbers and other utility functions.

**vel** - terminal velocity, transport velocity, and choking velocity functions.

## Tests

Tests are implemented with the [pytest](https://docs.pytest.org/en/latest/) framework. To avoid creating cache folders, run the tests with the following command: `pytest -p no:cacheprovider`

## Documentation

[Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is used to build the documentation for the chemics package using RST files and the autodoc extension. All Sphinx files are contained in the `sphinx/` folder. After building the HTML files, run the `move_sphinx_html.sh` script. This will move the HTML to the `docs/` folder which is used by GitHub to host the documentation website.

## License

This Python package is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
