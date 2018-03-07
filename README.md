# Chemics

Chemics is a Python package for developing reactor models.

:warning: This software is still under development. Official release will be announced at a later date. Public contributions will also be accepted once a more complete version of the package is available.

Questions and other feedback can be submitted on the [Issues](https://github.com/ccpcode/chemics/issues) page.

## Installation

Copy the `chemics/` folder to your Python project then import the module with `import chemics as cm`. Functions in the module are called with the usual syntax such as `cm.rhog(28, 170100, 773)`.

## Modules

**bfb** - functions for modeling bubbling fluidized bed (BFB) reactors.

**gas** - gas properties such as atmospheric pressure, density, thermal
conductivity, and viscosity.

**rtd** - functions for residence time distribution.

**util** - dimensionless numbers and other utility functions.

**vel** - terminal velocity, transport velocity, and choking velocity functions.