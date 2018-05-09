# Chemics :alembic:

Chemics is a Python package for developing reactor models.

:warning: This package is still under development. Official release will be announced at a later date. Public contributions will also be accepted once a more complete version of the package is available.

Questions and other feedback can be submitted on the [Issues](https://github.com/ccpcode/chemics/issues) page.

[![PyPI version](https://badge.fury.io/py/chemics.svg)](https://badge.fury.io/py/chemics) [![Anaconda-Server Badge](https://anaconda.org/wigging/chemics/badges/downloads.svg)](https://anaconda.org/wigging/chemics)

## Requirements

The only requirements for the chemics package are Python 3 and Numpy. The [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) tools provide an easy way to install Python on Mac, Linux, and Windows computers.

## Installation and Usage

Several methods are available to install the chemics package. Options to install from [PyPi](https://pypi.org) via `pip` and from [Anaconda](https://anaconda.org) via `conda` will be available soon.

Download from GitHub
1. download or clone this repository from GitHub
2. copy the chemics subfolder into your Python project

Install locally with pip
1. download or clone this repository from GitHub
2. from within the chemics folder, run `pip install -e .` to install the package to your local machine

Functions in the chemics package are called with the usual dot syntax for accessing module features. The example below calculates the density of a gas based on its molecular weight, pressure, and temperature.

```python
import chemics as cm
cm.rhog(28, 170100, 773)
```

## Documentation

Documentation for the chemics package is available online at [ccpcode.github.io/chemics](https://ccpcode.github.io/chemics/).

## Contributing

Please read the following sections if you would like to contribute to the chemics package.

### Style Guide

Coding style should adhere to [Flake8](http://flake8.pycqa.org/en/latest/) standards. Linter plugins that enforce this style are available for various text editors and IDEs. 

### Tests

Tests are implemented with the [pytest](https://docs.pytest.org/en/latest/) framework. To avoid creating cache folders, run the tests with the following command: `pytest -p no:cacheprovider`

### Sphinx Documentation

[Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is used to build the documentation for the chemics package using RST files and the autodoc extension. All Sphinx files are contained in the `sphinx/` folder. After building the HTML files, run the `move_sphinx_html.sh` script. This will move the HTML to the `docs/` folder which is used by GitHub to host the documentation website.

## License

This Python package is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
