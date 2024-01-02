# Contributing to Chemics

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to the Chemics Python package. Submitted code that does not conform to these guidelines will not be merged into the package. Feel free to propose changes to this document in a Pull Request or Issue.

## Development environment

Use the `environment.yml` file to create a conda environment for developing the Chemics package. See the comments in the file for more details.

## Code style, linting, and formatting

All Python code in the Chemics package should adhere to the [PEP 8](https://peps.python.org/pep-0008/) style guide. All linting and formatting should be implemented with [ruff](https://github.com/astral-sh/ruff). Configuration for ruff is defined in the pyproject.toml file.

## Docstrings

All functions, classes, and other Python components should contain docstrings with syntax and best practices outlined by the [NumPy docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html). Within the docstring, use the references section to list references used to develop that function or method. A simple example of how to use a function or class should be included in its docstring.

## Examples

Along with an example in the docstring, please provide a complete example in the Sphinx documentation. Simple examples should also be provided in the docstrings.

## Tests

New code for the Chemics package must include associated tests in the `tests/` folder. The [pytest](https://github.com/pytest-dev/pytest) framework is used to execute the test files.

## Changelog

Don't forget to edit the changelog based on your contributions. Follow the style on the [Keep a Changelog](https://keepachangelog.com) website.

## Sphinx documentation

New source code along with examples should be documented in the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/) located in the `docs/` folder.

## Creating a pull request

All pull requests should be submitted to the `dev` branch; not to the `main` branch. The `dev` branch will be merged with the `main` branch when a new version of Chemics is ready to be released.
