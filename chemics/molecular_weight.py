import math
import numpy as np
import re
from .atomic_elements import atomic_elements

__all__ = ['molecular_weight', 'mw_mix']


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
    mw : float
        Sum of molecular weights from molecular formula.
    """
    if len(tokens) == 0:
        mw = sum(stack)
        return mw

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


def molecular_weight(formula):
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
    >>> molecular_weight('C')
    12.011

    >>> molecular_weight('CH4')
    16.04

    >>> molecular_weight('(NH4)2SO4')
    132.13

    References
    ----------
    .. [1] IUPAC Periodic Table of the Elements. International Union of Pure
       and Applied Chemistry, 2016.
       https://iupac.org/what-we-do/periodic-table-of-elements/.
    """
    tokens = re.findall(r'[A-Z][a-z]*|\d+|\(|\)', formula)
    mw = _parse(tokens, [])
    return mw


def mw_mix(mix, wts):
    """
    Molecular weight of a gas mixture calculated as a weighted mean.

    Parameters
    ----------
    mix : list of str
        Components of the gas mixture
    wts : list of float
        Weight fraction of each gas component, sums to 1.0

    Returns
    -------
    mw_mix : float
        Molecular weight of a gas mixture [g/mol]

    Examples
    --------
    >>> mw_mix(['H2', 'N2'], [0.8, 0.2])
    7.2156

    >>> mw_mix(['H2', 'N2', 'CH4'], [0.4, 0.1, 0.5])
    11.6293
    """
    if len(mix) != len(wts):
        raise ValueError('Number of components in mixture must be same as weights')
    if not math.isclose(sum(wts), 1):
        raise ValueError('Weights must sum to 1.0')

    mw_gases = []
    for gas in mix:
        mw = molecular_weight(gas)
        mw_gases.append(mw)

    mw_mix = np.average(mw_gases, weights=wts)
    return mw_mix
