"""
Tests for the elements dictionary. Updated by G.W. on 11/21/2018.
"""

import chemics as cm
from pytest import approx


# Functions to test
# ----------------------------------------------------------------------------

def test_hydrogen():
    atomic_num = cm.elements['H']['atomic_number']
    name = cm.elements['H']['name']
    atomic_wt = cm.elements['H']['atomic_weight']
    assert atomic_num == 1
    assert name == 'hydrogen'
    assert atomic_wt == approx(1.008, rel=1e-2)


def test_calcium():
    atomic_num = cm.elements['Ca']['atomic_number']
    name = cm.elements['Ca']['name']
    atomic_wt = cm.elements['Ca']['atomic_weight']
    assert atomic_num == 20
    assert name == 'calcium'
    assert atomic_wt == approx(40.078, rel=1e-2)
