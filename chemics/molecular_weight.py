import numpy as np
import re
from .atomic_elements import atomic_elements

__all__ = ['mw', 'mw_mix']


def _find_end(tokens):
    """
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
        if t == ')':
            count -= 1
            if count == 0:
                return idx
        elif t == '(':
            count += 1

    raise ValueError('Unmatched parentheses')


def _parse(tokens, stack):
    """
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

    if t == '(':
        end = _find_end(tokens)
        stack.append(_parse(tokens[1:end], []))
        return _parse(tokens[end + 1:], stack)
    elif t in atomic_elements:
        stack.append(atomic_elements[t]['atomic_weight'])
    elif t.isdigit():
        stack[-1] *= int(t)

    return _parse(tokens[1:], stack)


def mw(formula):
    """
    Tokenize a molecular formula to determine total molecular weight.
    Calculation is based on atomic weight values from IUPAC [1]_.

    Parameters
    ----------
    formula : str
        Molecular formula or element.

    Returns
    -------
    mw : float
       Molecular weight of the formula or element [g/mol]

    Examples
    --------
    >>> mw('C')
    12.011

    >>> mw('CH4')
    16.04

    >>> mw('(NH4)2SO4')
    132.13

    References
    ----------
    .. [1] IUPAC Periodic Table of the Elements. International Union of Pure
       and Applied Chemistry, 2016.
       https://iupac.org/what-we-do/periodic-table-of-elements/.
    """
    tokens = re.findall(r'[A-Z][a-z]*|\d+|\(|\)', formula)
    molecular_weight = _parse(tokens, [])
    return molecular_weight


def mw_mix(mws, xs):
    """
    Molecular weight of a gas mixture calculated as a weighted mean.

    Parameters
    ----------
    mws : list, tuple, or array
        Molecular weight of each gas component [g/mol]
    xs : list, tuple, or array
        Mole fraction of each gas component [-]

    Returns
    -------
    mw_mix : float
        Molecular weight of a gas mixture [g/mol]

    Raises
    ------
    ValueError
        If sum of mole fractions does not equal 1.0

    Examples
    --------
    >>> mw_h2 = cm.mw('H2')
    ... mw_n2 = cm.mw('N2')
    ... mw_mix([mw_h2, mw_n2], [0.8, 0.2])
    7.2156

    >>> mw_h2 = cm.mw('H2')
    ... mw_n2 = cm.mw('N2')
    ... mw_ch4 = cm.mw('CH4')
    ... mw_mix([mw_h2, mw_n2, mw_ch4], [0.4, 0.1, 0.5])
    11.6293
    """
    mws = np.asarray(mws)
    xs = np.asarray(xs)
    if not np.isclose(xs.sum(), 1.0):
        raise ValueError('Sum of mole fractions must be 1.0')
    molwt_mix = np.average(mws, weights=xs)
    return molwt_mix
