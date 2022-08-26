# Changelog

Version numbers use calendar versioning based on `YY.MM.MICRO`. See the [CalVer](https://calver.org) website for more information about this versioning convention. The format of this changelog follows the approach outlined on the [Keep a Changelog](https://keepachangelog.com) website.

## 22.8

#### Fixed

- Fix CAS numbers for cp liquid organic
- Fix CAS number for cp liquid inorganic
- Fix CAS numbers for cp gas organic
- Fix CAS numbers in cp gas inorganic

#### Changed

- Use dictionary for Umf coefficients

## 21.10

#### Added

- `cp_liquid()` function to calculate liquid heat capacity
- Tests and documentation for the `cp_liquid()` function

#### Removed

- Unused code in gas heat capacity module

## 21.7

#### Added

- `Proximate` and `Ultimate` analysis classes
- Tests and documentation for the above classes

#### Removed

- Deleted `proximate_bases()` and `ultimate_bases()` functions

## 21.5

#### Added

- Mass transfer correlations
- Peclet (Pe), Schmidt (Sc), and Sherwood (Sh) dimensionless numbers
- Function to calculate pressure drop using Ergun equation

#### Changed

- Updated contributing guidelines

## v21.4

#### Added

- `cp_gas()` function to calculate gas heat capacity
- Tests and documentation for the above function

#### Fixed

- Fix dp in docstring for Archimedes function

## v20.9

#### Added

- `archimedes()` function to calculate Archimedes number

#### Fixed

- Imports for remaining choking velocity functions

## v20.8

#### Added

- `dimensionless_numbers` module
- `biot()` function to calculate Biot number
- `pyroI()` function to calculate Pyrolysis number I
- `pyroII()` function to calculate Pyrolysis number II
- `reynolds()` function to calculate Reynolds number

#### Changed

- Moved prandtl function to `dimensionless_numbers` module

## v20.7

#### Added

- `prandtl()` function to calculate dimensionless Prandtl number

## v20.5

#### Added

 - `ubr_holland()` function to calculate bubble rise velocity
 - `proximate_bases()` function for proximate analysis bases
 - `ultimate_bases()` function for ultimate analysis bases
 - Tests and documentation for the functions mentioned above

#### Changed

- Renamed `bubble_velocity` module to `bubble_rise_velocity`
- Renamed `ubr()` function to `ubr_kunii()`

## v20.4

#### Added

- `biocomp()` function to calculate biomass composition from ultimate analysis
- `plot_biocomp()` function to create a Matplotlib figure of the biomass composition results
- Tests for the `biocomp()` function
- Documentation for the `biocomp()` and `plot_biocomp()` functions

## v19.10

#### Added

- `ChemicalEquation()` class to determine properties of the reactants and products in a given chemical reaction equation
- Tests for chemical equation class
- Documentation for the chemical equation class

## v19.8

#### Added

- `tdh_chan()` and `tdh_horio()` functions for transport disengaging height
- Tests for the TDH functions
- Added math equations to terminal velocity doc strings

#### Changed

- Use terminal velocity from Newton's law to determine max value for guess in `ut_ganser()` function
- `ut_ganser()` now returns a scalar, not a tuple as in previous versions

## v19.7

#### Added

- `cp_wood()` for wood heat capacity

## v19.6.1

#### Added

- `k_wood()` for wood thermal conductivity
- Test and documentation for `k_wood()` function

#### Fixed

- Fix display of the `atomic_elements` dictionary in documentation

## v19.6

#### Added
- `mu_graham()` to calculate viscosity of a gas mixture using mole fraction and viscosity of each component
- `mu_herning()` to calculate viscosity of a gas mixture using molecular weight, mole fraction, and viscosity of each component

#### Changed
- Renamed `molecular_weight()` function to `mw()`
- Input parameters for `mw_mix()` are now molecular weight and mole fraction of each gas component

#### Removed
- Deleted the `mu_gas_mix()` function. Use the `mu_graham()` function instead

## v19.5.2

#### Added
- Added option to plot min and max particle size on Geldart chart

#### Changed
- Renamed `plot_geldart` function to `geldart_chart`
- This function now returns a Matplotlib figure

## v19.5.1

#### Added
- `massfrac_to_molefrac()` to convert from mass fractions to mole fractions
- `molefrac_to_massfrac()` to convert from mole fractions to mass fractions
- Tests for the mass fraction and mole fraction functions

#### Fixed
- Correct docstring style for `slm_to_lpm()`

## v19.5

#### Added
- Geldart particle classification
