# Changelog

Version numbers use calendar versioning based on `YY.MM.MICRO`. See the [CalVer](https://calver.org) website for more information about this versioning convention.

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
