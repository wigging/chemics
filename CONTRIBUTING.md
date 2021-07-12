# Contributing to Chemics

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to the Chemics Python package. Submitted code that does not conform to these guidelines will not be merged into the package. Feel free to propose changes to this document in a Pull Request or Issue.

## Code style

All code in the Chemics package should adhere to the style enforced by the [Flake8](https://pypi.org/project/flake8/) tool. This will ensure a consistent code format throughout the package and prevent syntax errors during development. For the Flake8 style settings, ignore the E501, W503, W605 errors and warnings.

## Docstrings

All functions, classes, and other Python components should contain docstrings with syntax and best practices outlined by the [NumPy docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html).

## Examples

A simple example of how to use a function or class should be included in its docstring. Along with an example in the docstring, please provide a complete example in the [examples](https://github.com/chemics/examples) repository.

## References

Within the docstring, a references section lists the original literature from which the function was developed.

## Tests

New functions for the Chemics package must include associated tests in the `tests/` folder. The [pytest](https://docs.pytest.org/en/latest/) framework is used to execute the test files.

## Changelog

Don't forget to edit the changelog based on your contributions. Follow the style on the [Keep a Changelog](https://keepachangelog.com) website.

## Sphinx documentation

Finally, new source code should be included in the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/) located in the `docs/` folder.

## Creating a Pull Request

All Pull Requests should be submitted to the `dev` branch; not to the `main` branch. When a new version is ready to be released the `dev` branch will be merged with the `main` branch.
