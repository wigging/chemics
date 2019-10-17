import chemics as cm
import numpy as np
import re
import textwrap
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
    balance : bool
        Balance between atomic elements in reactants and products.
    reactants : list
        Reactants in the chemical equation.
    rct_species : list
        Chemical species from reactants list. Uses the `names` dictionary if needed.
    rct_moles : array
        Number of moles for each chemical species in reactants.
    rct_mw : array
        Molecular weight for each chemical species in reactants.
    rct_mass : array
        Molecular weight for each chemical species in reactants.
    rct_elements : dict
        Number of atomic elements in reactants.
    rct_sum_moles : float
        Total number of moles for reactants.
    rct_sum_mass : float
        Total mass of reactants.
    rct_mol_fracs : array
        Mole fractions of each chemical species in reactants.
    rct_mass_fracs : array
        Mass fractions of each chemical species in reactants.
    products : list
        Products in the chemical equation.
    prod_species : list
        Chemical species from products list. Uses the `names` dictionary if needed.
    prod_moles : array
        Number of moles for each chemical species in products.
    prod_mw : array
        Molecular weight for each chemical species in products.
    prod_mass : array
        Molecular weight for each chemical species in products.
    prod_elements : dict
        Number of atomic elements in products.
    prod_sum_moles : float
        Total number of moles for products.
    prod_sum_mass : float
        Total mass of products.
    prod_mol_fracs : array
        Mole fractions of each chemical species in products.
    prod_mass_fracs : array
        Mass fractions of each chemical species in products.

    Examples
    --------
    >>> ce = ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
    >>> ce.balance
    True

    >>> ce.rct_mol_fracs
    [0.5 0.5]

    >>> print(ce)
    # this prints all attributes to the screen
    """

    def __init__(self, eq, names=None):

        self.eq = eq
        self.names = names
        self._parse_equation()
        self._assign_rct_attrs()
        self._assign_prod_attrs()
        self._check_balance()

    def __str__(self):

        desc = f"""
        {'eq':18} {self.eq}
        {'names':18} {self.names}
        {'balance':18} {self.balance}

        {'reactants':18} {self.reactants}
        {'rct_species':18} {self.rct_species}
        {'rct_moles':18} {self.rct_moles}
        {'rct_mw':18} {self.rct_mw}
        {'rct_mass':18} {self.rct_mass}
        {'rct_elements':18} {self.rct_elements}
        {'rct_sum_moles':18} {self.rct_sum_moles}
        {'rct_sum_mass':18} {self.rct_sum_mass}
        {'rct_mol_fracs':18} {self.rct_mol_fracs}
        {'rct_mass_fracs':18} {self.rct_mass_fracs}

        {'products':18} {self.products}
        {'prod_species':18} {self.prod_species}
        {'prod_moles':18} {self.prod_moles}
        {'prod_mw':18} {self.prod_mw}
        {'prod_mass':18} {self.prod_mass}
        {'prod_elements':18} {self.prod_elements}
        {'prod_sum_moles':18} {self.prod_sum_moles}
        {'prod_sum_mass':18} {self.prod_sum_mass}
        {'prod_mol_fracs':18} {self.prod_mol_fracs}
        {'prod_mass_fracs':18} {self.prod_mass_fracs}"""

        return textwrap.dedent(desc)

    def _parse_equation(self):
        """
        Split chemical equation into reactants and products.
        """
        rcts = self.eq.split('->')[0].split('+')
        self.reactants = [r.strip() for r in rcts]

        prods = self.eq.split('->')[1].split('+')
        self.products = [p.strip() for p in prods]

    def _equation_properties(self, comps):
        """
        Determine properties for each chemical component in reactants or
        products.
        """
        nc = len(comps)
        element_counter = Counter()

        species = []
        moles = np.zeros(nc)
        molwt = np.zeros(nc)
        mass = np.zeros(nc)

        for i, c in enumerate(comps):

            # --- moles and chemical species ---

            if c[0].isdigit():
                c = c.split()
                mol = float(c[0])
                sp = c[1]
            else:
                mol = 1.0
                sp = c

            if (self.names is not None) and (sp in self.names.keys()):
                sp = self.names[sp]

            species.append(sp)
            moles[i] = mol

            # --- mass and molecular weight ---

            mw = cm.mw(sp)
            molwt[i] = mw
            mass[i] = mol * mw

            # --- count elements from each chemical species ---

            rex = re.findall('([A-Z][a-z]?)([0-9]+)?', sp)

            for r in rex:
                element = r[0]

                if r[1] == '':
                    atoms = 1.0
                else:
                    atoms = float(r[1])

                # dict where key is element and value is number of atoms such as {'C': 6.0}
                d = {element: atoms * mol}
                element_counter.update(d)

        sum_moles = sum(moles)
        sum_mass = sum(mass)
        mol_fracs = moles / sum_moles
        mass_fracs = mass / sum_mass

        properties = dict(
            species=species,
            moles=moles,
            molwt=molwt,
            mass=mass,
            element_counter=element_counter,
            sum_moles=sum_moles,
            sum_mass=sum_mass,
            mol_fracs=mol_fracs,
            mass_fracs=mass_fracs)

        return properties

    def _assign_rct_attrs(self):
        """
        Assign results for reactants to attributes.
        """
        rct_properties = self._equation_properties(self.reactants)
        self.rct_species = rct_properties['species']
        self.rct_moles = rct_properties['moles']
        self.rct_mw = rct_properties['molwt']
        self.rct_mass = rct_properties['mass']
        self.rct_elements = dict(rct_properties['element_counter'])
        self.rct_sum_moles = rct_properties['sum_moles']
        self.rct_sum_mass = rct_properties['sum_mass']
        self.rct_mol_fracs = rct_properties['mol_fracs']
        self.rct_mass_fracs = rct_properties['mass_fracs']

    def _assign_prod_attrs(self):
        """
        Assign results for products to attributes.
        """
        prod_properties = self._equation_properties(self.products)
        self.prod_species = prod_properties['species']
        self.prod_moles = prod_properties['moles']
        self.prod_mw = prod_properties['molwt']
        self.prod_mass = prod_properties['mass']
        self.prod_elements = dict(prod_properties['element_counter'])
        self.prod_sum_moles = prod_properties['sum_moles']
        self.prod_sum_mass = prod_properties['sum_mass']
        self.prod_mol_fracs = prod_properties['mol_fracs']
        self.prod_mass_fracs = prod_properties['mass_fracs']

    def _check_balance(self):
        """
        Check balance of atomic elements in reactants or products.
        """
        tol = 1e-4
        self.balance = True

        for x, y in zip(self.rct_elements.values(), self.prod_elements.values()):
            if abs(x - y) > tol:
                self.balance = False
                break

    def reactant_props(self, species):
        """
        Properties for a given reactant.

        Parameters
        ----------
        species : str
            Name of species in reactants.

        Returns
        -------
        rct_props : dict
            Reactant properties defined as `moles`, `mol_wt`, `mass`,
            `mol_frac`, and `mass_frac` keys.

        Example
        -------
        >>> ce = ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
        >>> ce.reactant_props('Na')
        {'moles': 2.0,
         'mol_wt': 22.99,
         'mass': 45.98,
         'mol_frac': 0.5,
         'mass_frac': 0.3867}
        """
        idx = self.rct_species.index(species)
        moles = self.rct_moles[idx]
        mol_wt = self.rct_mw[idx]
        mass = self.rct_mass[idx]
        mol_frac = self.rct_mol_fracs[idx]
        mass_frac = self.rct_mass_fracs[idx]
        rct_props = dict(moles=moles, mol_wt=mol_wt, mass=mass, mol_frac=mol_frac, mass_frac=mass_frac)
        return rct_props

    def product_props(self, species):
        """
        Properties for a given product.

        Parameters
        ----------
        species : str
            Name of species in products.

        Returns
        -------
        prod_props : dict
            Product properties defined as `moles`, `mol_wt`, `mass`,
            `mol_frac`, and `mass_frac` keys.

        Example
        -------
        >>> ce = ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
        >>> ce.product_props('NaCl')
        {'moles': 2.0,
         'mol_wt': 58.44,
         'mass': 116.88,
         'mol_frac': 0.66,
         'mass_frac': 0.983}
        """
        idx = self.prod_species.index(species)
        moles = self.prod_moles[idx]
        mol_wt = self.prod_mw[idx]
        mass = self.prod_mass[idx]
        mol_frac = self.prod_mol_fracs[idx]
        mass_frac = self.prod_mass_fracs[idx]
        prod_props = dict(moles=moles, mol_wt=mol_wt, mass=mass, mol_frac=mol_frac, mass_frac=mass_frac)
        return prod_props
