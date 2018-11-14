# Contributing to Chemics

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to the Chemics Python
package. Submitted code that does not conform to these guidelines will not be
merged into the package. Feel free to propose changes to this document in a pull
request or issue.

## Code style

All code in the Chemics package should adhere to the style enforced by the
[Flake8][f8] tool. This will ensure a consistent code format throughout the
package and prevent syntax errors during development.

## Docstrings

All functions, classes, and other Python components should contain docstrings
with syntax and best practices outlined by the [NumPy docstring guide][np].

## Example code

A simple example of how to use a function or class should be included in its
docstring. Along with an example in the docstring, a complete example is to be
provided in the [chemics-examples][ce] repository.

## References

Within the docstring, a references section lists the original literature from
which the function was developed.

## Tests

New functions for the Chemics package must include associated tests in the
`tests/` folder. The [pytest][pt] framework is used to execute the test files.

## Sphinx documentation

Finally, new source code should be included in the [Sphinx documentation][sd]
located in the `docs/` folder.

[f8]: https://pypi.org/project/flake8/
[np]: https://numpydoc.readthedocs.io/en/latest/format.html
[ce]: https://github.com/chemics/chemics-examples
[sd]: http://www.sphinx-doc.org/en/stable/
[pt]: https://docs.pytest.org/en/latest/