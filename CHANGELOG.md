# Changelog

Version numbers use calendar versioning based on `YY.MM.MICRO`. See the [CalVer](https://calver.org) website for more information about this versioning convention. The format of this changelog follows the approach outlined on the [Keep a Changelog](https://keepachangelog.com) website.

## v19.7

#### Added

- `cp_wood()` for wood heat capacity.

## v19.6.1

#### Added

- `k_wood()` for wood thermal conductivity.
- Test and documentation for `k_wood()` function.

#### Fixed

- Fix display of the `atomic_elements` dictionary in documentation.

## v19.6

#### Added
- `mu_graham()` to calculate viscosity of a gas mixture using mole fraction and viscosity of each component.
- `mu_herning()` to calculate viscosity of a gas mixture using molecular weight, mole fraction, and viscosity of each component.

#### Changed
- Renamed `molecular_weight()` function to `mw()`.
- Input parameters for `mw_mix()` are now molecular weight and mole fraction of each gas component.

#### Removed
- Deleted the `mu_gas_mix()` function. Use the `mu_graham()` function instead.

## v19.5.2

#### Added
- Added option to plot min and max particle size on Geldart chart.

#### Changed
- Renamed `plot_geldart` function to `geldart_chart`.
- This function now returns a Matplotlib figure.

## v19.5.1

#### Added
- `massfrac_to_molefrac()` to convert from mass fractions to mole fractions.
- `molefrac_to_massfrac()` to convert from mole fractions to mass fractions.
- Tests for the mass fraction and mole fraction functions.

#### Fixed
- Correct docstring style for `slm_to_lpm()`.

## v19.5

#### Added
- Geldart particle classification.
