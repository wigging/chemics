"""
Dictionary containing atomic number, name, and atomic weight of elements in the
periodic table. Conventional atomic weight is used for atomic weight where
applicable. Values taken from IUPAC.

References
----------
IUPAC Periodic Table of the Elements. International Union of Pure and Applied
Chemistry, 2016. https://iupac.org/what-we-do/periodic-table-of-elements/.
"""

elements = {
    'H': {'atomic_number': 1, 'name': 'hydrogen', 'atomic_weight': 1.008},
    'He': {'atomic_number': 2, 'name': 'helium', 'atomic_weight': 4.0026},
    'Li': {'atomic_number': 3, 'name': 'lithium', 'atomic_weight': 6.94},
    'Be': {'atomic_number': 4, 'name': 'beryllium', 'atomic_weight': 9.0122},
    'B': {'atomic_number': 5, 'name': 'boron', 'atomic_weight': 10.81},
    'C': {'atomic_number': 6, 'name': 'carbon', 'atomic_weight': 12.011},
    'N': {'atomic_number': 7, 'name': 'nitrogen', 'atomic_weight': 14.007},
    'O': {'atomic_number': 8, 'name': 'oxygen', 'atomic_weight': 15.999},
    'F': {'atomic_number': 9, 'name': 'fluorine', 'atomic_weight': 18.998},
    'Ne': {'atomic_number': 10, 'name': 'neon', 'atomic_weight': 20.180},
    'Na': {'atomic_number': 11, 'name': 'sodium', 'atomic_weight': 22.990},
    'Mg': {'atomic_number': 12, 'name': 'magnesium', 'atomic_weight': 24.305},
    'Al': {'atomic_number': 13, 'name': 'aluminium', 'atomic_weight': 26.982},
    'Si': {'atomic_number': 14, 'name': 'silicon', 'atomic_weight': 28.085},
    'P': {'atomic_number': 15, 'name': 'phosphorus', 'atomic_weight': 30.974},
    'S': {'atomic_number': 16, 'name': 'sulfur', 'atomic_weight': 32.06},
    'Cl': {'atomic_number': 17, 'name': 'chlorine', 'atomic_weight': 35.45},
    'Ar': {'atomic_number': 18, 'name': 'argon', 'atomic_weight': 39.948},
    'K': {'atomic_number': 19, 'name': 'potassium', 'atomic_weight': 39.098},
    'Ca': {'atomic_number': 20, 'name': 'calcium', 'atomic_weight': 40.078},
    'Sc': {'atomic_number': 21, 'name': 'scandium', 'atomic_weight': 44.956},
    'Ti': {'atomic_number': 22, 'name': 'titanium', 'atomic_weight': 47.867},
    'V': {'atomic_number': 23, 'name': 'vanadium', 'atomic_weight': 50.942},
    'Cr': {'atomic_number': 24, 'name': 'chromium', 'atomic_weight': 51.996},
    'Mn': {'atomic_number': 25, 'name': 'manganese', 'atomic_weight': 54.938},
    'Fe': {'atomic_number': 26, 'name': 'iron', 'atomic_weight': 55.845},
    'Co': {'atomic_number': 27, 'name': 'cobalt', 'atomic_weight': 58.933},
    'Ni': {'atomic_number': 28, 'name': 'nickel', 'atomic_weight': 58.693},
    'Cu': {'atomic_number': 29, 'name': 'copper', 'atomic_weight': 63.546},
    'Zn': {'atomic_number': 30, 'name': 'zinc', 'atomic_weight': 65.38},
    'Ga': {'atomic_number': 31, 'name': 'gallium', 'atomic_weight': 69.723},
    'Ge': {'atomic_number': 32, 'name': 'germanium', 'atomic_weight': 72.630},
    'As': {'atomic_number': 33, 'name': 'arsenic', 'atomic_weight': 74.922},
    'Se': {'atomic_number': 34, 'name': 'selenium', 'atomic_weight': 78.971},
    'Br': {'atomic_number': 35, 'name': 'bromine', 'atomic_weight': 79.904},
    'Kr': {'atomic_number': 36, 'name': 'krypton', 'atomic_weight': 83.798},
    'Rb': {'atomic_number': 37, 'name': 'rubidium', 'atomic_weight': 85.468},
    'Sr': {'atomic_number': 38, 'name': 'strontium', 'atomic_weight': 87.62},
    'Y': {'atomic_number': 39, 'name': 'yttrium', 'atomic_weight': 88.906},
    'Zr': {'atomic_number': 40, 'name': 'zirconium', 'atomic_weight': 91.224},
    'Nb': {'atomic_number': 41, 'name': 'niobium', 'atomic_weight': 92.906},
    'Mo': {'atomic_number': 42, 'name': 'molybdenum', 'atomic_weight': 95.95},
    'Tc': {'atomic_number': 43, 'name': 'technetium', 'atomic_weight': None},
    'Ru': {'atomic_number': 44, 'name': 'ruthenium', 'atomic_weight': 101.07},
    'Rh': {'atomic_number': 45, 'name': 'rhodium', 'atomic_weight': 102.91},
    'Pd': {'atomic_number': 46, 'name': 'palladium', 'atomic_weight': 106.42},
    'Ag': {'atomic_number': 47, 'name': 'silver', 'atomic_weight': 107.87},
    'Cd': {'atomic_number': 48, 'name': 'cadmium', 'atomic_weight': 112.41},
    'In': {'atomic_number': 49, 'name': 'indium', 'atomic_weight': 114.82},
    'Sn': {'atomic_number': 50, 'name': 'tin', 'atomic_weight': 118.71},
    'Sb': {'atomic_number': 51, 'name': 'antimony', 'atomic_weight': 121.76},
    'Te': {'atomic_number': 52, 'name': 'tellurium', 'atomic_weight': 127.60},
    'I': {'atomic_number': 53, 'name': 'iodine', 'atomic_weight': 126.90},
    'Xe': {'atomic_number': 54, 'name': 'xenon', 'atomic_weight': 131.29},
    'Cs': {'atomic_number': 55, 'name': 'caesium', 'atomic_weight': 132.91},
    'Ba': {'atomic_number': 56, 'name': 'barium', 'atomic_weight': 137.33},
    'La': {'atomic_number': 57, 'name': 'lanthanum', 'atomic_weight': 138.91},
    'Ce': {'atomic_number': 58, 'name': 'cerium', 'atomic_weight': 140.12},
    'Pr': {'atomic_number': 59, 'name': 'praseodymium', 'atomic_weight': 140.91},
    'Nd': {'atomic_number': 60, 'name': 'neodymium', 'atomic_weight': 144.24},
    'Pm': {'atomic_number': 61, 'name': 'promethium', 'atomic_weight': None},
    'Sm': {'atomic_number': 62, 'name': 'samarium', 'atomic_weight': 150.36},
    'Eu': {'atomic_number': 63, 'name': 'europium', 'atomic_weight': 151.96},
    'Gd': {'atomic_number': 64, 'name': 'gadolinium', 'atomic_weight': 157.25},
    'Tb': {'atomic_number': 65, 'name': 'terbium', 'atomic_weight': 158.93},
    'Dy': {'atomic_number': 66, 'name': 'dysprosium', 'atomic_weight': 162.50},
    'Ho': {'atomic_number': 67, 'name': 'holmium', 'atomic_weight': 164.93},
    'Er': {'atomic_number': 68, 'name': 'erbium', 'atomic_weight': 167.26},
    'Tm': {'atomic_number': 69, 'name': 'thulium', 'atomic_weight': 168.93},
    'Yb': {'atomic_number': 70, 'name': 'ytterbium', 'atomic_weight': 173.05},
    'Lu': {'atomic_number': 71, 'name': 'lutetium', 'atomic_weight': 174.97},
    'Hf': {'atomic_number': 72, 'name': 'hafnium', 'atomic_weight': 178.49},
    'Ta': {'atomic_number': 73, 'name': 'tantalum', 'atomic_weight': 180.95},
    'W': {'atomic_number': 74, 'name': 'tungsten', 'atomic_weight': 183.84},
    'Re': {'atomic_number': 75, 'name': 'rhenium', 'atomic_weight': 186.21},
    'Os': {'atomic_number': 76, 'name': 'osmium', 'atomic_weight': 190.23},
    'Ir': {'atomic_number': 77, 'name': 'iridium', 'atomic_weight': 192.22},
    'Pt': {'atomic_number': 78, 'name': 'platinum', 'atomic_weight': 195.08},
    'Au': {'atomic_number': 79, 'name': 'gold', 'atomic_weight': 196.97},
    'Hg': {'atomic_number': 80, 'name': 'mercury', 'atomic_weight': 200.59},
    'Tl': {'atomic_number': 81, 'name': 'thallium', 'atomic_weight': 204.38},
    'Pb': {'atomic_number': 82, 'name': 'lead', 'atomic_weight': 207.2},
    'Bi': {'atomic_number': 83, 'name': 'bismuth', 'atomic_weight': 208.98},
    'Po': {'atomic_number': 84, 'name': 'polonium', 'atomic_weight': None},
    'At': {'atomic_number': 85, 'name': 'astatine', 'atomic_weight': None},
    'Rn': {'atomic_number': 86, 'name': 'radon', 'atomic_weight': None},
    'Fr': {'atomic_number': 87, 'name': 'francium', 'atomic_weight': None},
    'Ra': {'atomic_number': 88, 'name': 'radium', 'atomic_weight': None},
    'Ac': {'atomic_number': 89, 'name': 'actinium', 'atomic_weight': None},
    'Th': {'atomic_number': 90, 'name': 'thorium', 'atomic_weight': 232.04},
    'Pa': {'atomic_number': 91, 'name': 'protactinium', 'atomic_weight': 231.04},
    'U': {'atomic_number': 92, 'name': 'uranium', 'atomic_weight': 238.03},
    'Np': {'atomic_number': 93, 'name': 'neptunium', 'atomic_weight': None},
    'Pu': {'atomic_number': 94, 'name': 'plutonium', 'atomic_weight': None},
    'Am': {'atomic_number': 95, 'name': 'americium', 'atomic_weight': None},
    'Cm': {'atomic_number': 96, 'name': 'curium', 'atomic_weight': None},
    'Bk': {'atomic_number': 97, 'name': 'berkelium', 'atomic_weight': None},
    'Cf': {'atomic_number': 98, 'name': 'californium', 'atomic_weight': None},
    'Es': {'atomic_number': 99, 'name': 'einsteinium', 'atomic_weight': None},
    'Fm': {'atomic_number': 100, 'name': 'fermium', 'atomic_weight': None},
    'Md': {'atomic_number': 101, 'name': 'mendelevium', 'atomic_weight': None},
    'No': {'atomic_number': 102, 'name': 'nobelium', 'atomic_weight': None},
    'Lr': {'atomic_number': 103, 'name': 'lawrencium', 'atomic_weight': None},
    'Rf': {'atomic_number': 104, 'name': 'rutherfordium', 'atomic_weight': None},
    'Db': {'atomic_number': 105, 'name': 'dubnium', 'atomic_weight': None},
    'Sg': {'atomic_number': 106, 'name': 'seaborgium', 'atomic_weight': None},
    'Bh': {'atomic_number': 107, 'name': 'bohrium', 'atomic_weight': None},
    'Hs': {'atomic_number': 108, 'name': 'hassium', 'atomic_weight': None},
    'Mt': {'atomic_number': 109, 'name': 'meitnerium', 'atomic_weight': None},
    'Ds': {'atomic_number': 110, 'name': 'darmstadtium', 'atomic_weight': None},
    'Rg': {'atomic_number': 111, 'name': 'roentgenium', 'atomic_weight': None},
    'Cn': {'atomic_number': 112, 'name': 'copernicium', 'atomic_weight': None},
    'Nh': {'atomic_number': 113, 'name': 'nihonium', 'atomic_weight': None},
    'Fl': {'atomic_number': 114, 'name': 'flerovium', 'atomic_weight': None},
    'Mc': {'atomic_number': 115, 'name': 'moscovium', 'atomic_weight': None},
    'Lv': {'atomic_number': 116, 'name': 'livermorium', 'atomic_weight': None},
    'Ts': {'atomic_number': 117, 'name': 'tennessine', 'atomic_weight': None},
    'Og': {'atomic_number': 118, 'name': 'oganesson', 'atomic_weight': None}
}
