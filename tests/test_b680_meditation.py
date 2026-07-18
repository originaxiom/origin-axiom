"""B680 locks — the volume-as-being-L-value + inert-5."""
import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B680_arithmetic_meditation"))
from verify import volume_is_being_L_value, inert_5_in_eisenstein  # noqa


def test_volume_is_being_character_L_value():
    V, P = volume_is_being_L_value(dps=40)
    assert abs(V - P) < mp.mpf(10)**-38
    assert abs(V - mp.mpf('2.029883212819307250')) < 1e-18


def test_five_inert_in_eisenstein():
    inert, ram, ine, lvl = inert_5_in_eisenstein()
    assert inert and ram == 3 and ine == 5 and lvl == 15
