"""
Tests for the atomic_elements dictionary.
"""

import chemics as cm
from pytest import approx


# Functions to test
# ----------------------------------------------------------------------------

def test_hydrogen():
    atomic_num = cm.atomic_elements['H']['atomic_number']
    name = cm.atomic_elements['H']['name']
    atomic_wt = cm.atomic_elements['H']['atomic_weight']
    assert atomic_num == 1
    assert name == 'hydrogen'
    assert atomic_wt == approx(1.008, rel=1e-2)


def test_calcium():
    atomic_num = cm.atomic_elements['Ca']['atomic_number']
    name = cm.atomic_elements['Ca']['name']
    atomic_wt = cm.atomic_elements['Ca']['atomic_weight']
    assert atomic_num == 20
    assert name == 'calcium'
    assert atomic_wt == approx(40.078, rel=1e-2)
