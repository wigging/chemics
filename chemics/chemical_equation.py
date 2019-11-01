import chemics as cm
import pandas as pd
import re
from collections import Counter


class ChemicalEquation:
    """
    Properties of the reactants and products in a given chemical equation.

    Parameters
    ----------
    eq : str
        Chemical equation such as A + B -> C + D
    names : dict, optional
        Names of unique species and their corresponding chemical formula.

    Attributes
    ----------
    eq : str
        Chemical equation such as A + B -> C + D
    names : dict, optional
        Names of unique species and their corresponding chemical formula.
    rct_properties : dataframe
        Number of moles, chemical species, molecular weight, mass, mole
        fraction, and mass fraction for each reactant.
    rct_elements : dict
        Total number of atomic elements on reactant side of the equation.
    rct_moles : float
        Total number of moles on reactant side of the equation.
    rct_mass : float
        Total mass of the reactants.
    prod_properties : dataframe
        Number of moles, chemical species, molecular weight, mass, mole
        fraction, and mass fraction for each product.
    prod_elements : dict
        Total number of atomic elements on product side of the equation.
    prod_moles : float
        Total number of moles on product side of the equation.
    prod_mass : float
        Total mass of the products.
    balance : bool
        Balance between atomic elements in reactants and products.

    Examples
    --------
    >>> ce = ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
    >>> ce.balance
    True

    >>> ce.rct_properties
                   HCl        Na
    moles            2         2
    species        HCl        Na
    molwt       36.458     22.99
    mass        72.916     45.98
    molfrac        0.5       0.5
    massfrac  0.613275  0.386725

    >>> ce.rct_properties.loc['massfrac']
    HCl    0.613275
    Na     0.386725

    >>> ce.rct_elements
    {'H': 2.0, 'Cl': 2.0, 'Na': 2.0}

    >>> ce.rct_moles
    4.0

    >>> ce.rct_mass
    118.896
    """

    def __init__(self, eq, names=None):
        self.eq = eq
        self.names = names
        self._parse_equation()
        self._assign_rct_attrs()
        self._assign_prod_attrs()
        self._check_balance()

    def _parse_equation(self):
        """
        Split chemical equation into reactants and products.
        """
        rct_split = self.eq.split(' -> ')[0].split(' + ')
        self._rct_items = rct_split

        prod_split = self.eq.split(' -> ')[1].split(' + ')
        self._prod_items = prod_split

    def _eq_properties(self, eq_items):
        """
        Determine properties for each item in reactants or products.
        """
        eq_names = []
        eq_moles = []
        eq_species = []
        eq_molwts = []
        eq_masses = []
        eq_elements = Counter()

        for item in eq_items:

            # number of moles and name for each item
            if item[0].isdigit():
                item = item.split()
                mol = float(item[0])
                name = item[1]
                eq_names.append(name)
                eq_moles.append(mol)
            else:
                mol = 1.0
                name = item
                eq_names.append(name)
                eq_moles.append(mol)

            # species for each item is chemical formula specified in names
            # dictonary or as chemical formula (name) in the chemical equation
            # note - species is used for the molecular weight and elements
            if (self.names is not None) and (name in self.names.keys()):
                sp = self.names[name]
                eq_species.append(sp)
            else:
                sp = name
                eq_species.append(sp)

            # masses and molecular weights for each item
            mw = cm.mw(sp)
            mass = mol * mw
            eq_molwts.append(cm.mw(sp))
            eq_masses.append(mass)

            # count elements from each chemical species
            rex = re.findall('([A-Z][a-z]?)([0-9]*)', sp)

            for r in rex:
                element = r[0]

                if r[1] == '':
                    atoms = 1.0
                else:
                    atoms = float(r[1])

                # dict where key is element and value is number of atoms such as {'C': 6.0}
                d = {element: atoms * mol}
                eq_elements.update(d)

        # sum of moles and masses
        eq_sum_moles = sum(eq_moles)
        eq_sum_masses = sum(eq_masses)

        # mole fractions and mass fractions
        eq_mol_fracs = [m / eq_sum_moles for m in eq_moles]
        eq_mass_fracs = [m / eq_sum_masses for m in eq_masses]

        # dataframe for properties
        cols = eq_names
        idx = ['moles', 'species', 'molwt', 'mass', 'molfrac', 'massfrac']

        df = pd.DataFrame(columns=cols, index=idx)
        df.loc['moles'] = eq_moles
        df.loc['species'] = eq_species
        df.loc['molwt'] = eq_molwts
        df.loc['mass'] = eq_masses
        df.loc['molfrac'] = eq_mol_fracs
        df.loc['massfrac'] = eq_mass_fracs

        return df, dict(eq_elements), eq_sum_moles, eq_sum_masses

    def _assign_rct_attrs(self):
        """
        Assign results for reactants to attributes.
        """
        df, elements, sum_moles, sum_masses = self._eq_properties(self._rct_items)
        self.rct_properties = df
        self.rct_elements = elements
        self.rct_moles = sum_moles
        self.rct_mass = sum_masses

    def _assign_prod_attrs(self):
        """
        Assign results for products to attributes.
        """
        df, elements, sum_moles, sum_masses = self._eq_properties(self._prod_items)
        self.prod_properties = df
        self.prod_elements = elements
        self.prod_moles = sum_moles
        self.prod_mass = sum_masses

    def _check_balance(self):
        """
        Check balance of atomic elements in reactants or products.
        """
        tol = 1e-4
        self.balance = True

        if self.rct_elements == self.prod_elements:
            return

        for x, y in zip(self.rct_elements.values(), self.prod_elements.values()):
            if abs(x - y) > tol:
                self.balance = False
                break
