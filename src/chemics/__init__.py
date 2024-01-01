"""
Chemics package for chemical engineering.
"""

from .atm_pressure import patm
from .atomic_elements import atomic_elements

from .biomass_composition import biocomp
from .biomass_composition import plot_biocomp

from .chemical_equation import ChemicalEquation

from .conversions import slm_to_lpm
from .conversions import massfrac_to_molefrac
from .conversions import molefrac_to_massfrac

from .dimensionless_numbers import archimedes
from .dimensionless_numbers import biot
from .dimensionless_numbers import peclet
from .dimensionless_numbers import prandtl
from .dimensionless_numbers import pyrolysis_one
from .dimensionless_numbers import pyrolysis_two
from .dimensionless_numbers import reynolds
from .dimensionless_numbers import schmidt
from .dimensionless_numbers import sherwood
from .dimensionless_numbers import flow_regime

from .gas import Gas
from .gas_mixture import GasMixture

from .liquid import Liquid

from .molecular_weight import molecular_weight

from .proximate_analysis import Proximate
from .ultimate_analysis import Ultimate

from .wood import cp_wood
from .wood import k_wood

__all__ = [
    "patm",
    "atomic_elements",
    "biocomp",
    "plot_biocomp",
    "ChemicalEquation",
    "slm_to_lpm",
    "massfrac_to_molefrac",
    "molefrac_to_massfrac",
    "archimedes",
    "biot",
    "peclet",
    "prandtl",
    "pyrolysis_one",
    "pyrolysis_two",
    "reynolds",
    "schmidt",
    "sherwood",
    "flow_regime",
    "Gas",
    "GasMixture",
    "Liquid",
    "molecular_weight",
    "Proximate",
    "Ultimate",
    "cp_wood",
    "k_wood",
]
