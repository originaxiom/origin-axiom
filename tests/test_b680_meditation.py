"""B680 locks — the volume-as-being-L-value + inert-5."""
import os
import sys

import mpmath as mp

# Import under a UNIQUE module name: a bare `import verify` here collides with
# sys.modules['verify'] already claimed at collection time by test_b440 (B440's verify.py),
# which broke collection of the whole suite (E12 family, module-name dimension).
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "b680_verify", os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B680_arithmetic_meditation", "verify.py"))
_b680_verify = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_b680_verify)
volume_is_being_L_value = _b680_verify.volume_is_being_L_value
inert_5_in_eisenstein = _b680_verify.inert_5_in_eisenstein


def test_volume_is_being_character_L_value():
    V, P = volume_is_being_L_value(dps=40)
    assert abs(V - P) < mp.mpf(10)**-38
    assert abs(V - mp.mpf('2.029883212819307250')) < 1e-18


def test_five_inert_in_eisenstein():
    inert, ram, ine, lvl = inert_5_in_eisenstein()
    assert inert and ram == 3 and ine == 5 and lvl == 15
