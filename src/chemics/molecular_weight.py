"""
Function to calculate molecular weight.
"""

import re
from .atomic_elements import atomic_elements


def _find_end(tokens):
    """
    Find tokens.

    Find index of closing parenthesis. Based on function from Rhomboid at
    https://gist.github.com/Rhomboid/5994999.

    Parameters
    ----------
    tokens : list of str
        List of strings representing molecular formula.

    Return
    ------
    idx : int
        Index of closing parenthesis.
    """
    count = 0

    for idx, t in enumerate(tokens):
        if t == ")":
            count -= 1
            if count == 0:
                return idx
        elif t == "(":
            count += 1

    raise ValueError("Unmatched parentheses")


def _parse(tokens, stack):
    """
    Parse items.

    Parse items in formula list. Get atomic weight of each item or multiply by
    number of elements. Final value is molecular weight of the formula. Based
    on function from Rhomboid at https://gist.github.com/Rhomboid/5994999.

    Parameters
    ----------
    tokens : list of str
        List of strings representing molecular formula.
    stack : list of float
        Molecular weights of each element in formula.

    Returns
    -------
    mole_weight : float
        Sum of molecular weights from molecular formula.
    """
    if len(tokens) == 0:
        mole_weight = sum(stack)
        return mole_weight

    t = tokens[0]

    if t == "(":
        end = _find_end(tokens)
        stack.append(_parse(tokens[1:end], []))
        return _parse(tokens[end + 1 :], stack)
    elif t in atomic_elements:
        stack.append(atomic_elements[t]["atomic_weight"])
    elif t.isdigit():
        stack[-1] *= int(t)

    return _parse(tokens[1:], stack)


def molecular_weight(formula):
    """
    Molecular weight.

    Tokenize a molecular formula to determine total molecular weight.
    Calculation is based on atomic weight values from IUPAC [1]_.

    Parameters
    ----------
    formula : str
        Molecular formula or element

    Returns
    -------
    mw : float
       Molecular weight of the formula or element in g/mol

    Examples
    --------
    >>> cm.molecular_weight('C')
    12.011...

    >>> cm.molecular_weight('CH4')
    16.04...

    >>> cm.molecular_weight('(NH4)2SO4')
    132.13...

    References
    ----------
    .. [1] IUPAC Periodic Table of the Elements. International Union of Pure
       and Applied Chemistry, 2016.
       https://iupac.org/what-we-do/periodic-table-of-elements/.
    """
    tokens = re.findall(r"[A-Z][a-z]*|\d+|\(|\)", formula)
    molecular_weight = _parse(tokens, [])
    return molecular_weight
