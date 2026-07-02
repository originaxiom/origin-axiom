"""B356 -- the sigma-stability quick pair: det-lemma, mod-3 blindness, the omega chirality window."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B356_sigma_stability_scan'))
from sigma_stability import group_data, character_table, det_lemma, mod3_blindness_2T, h104_scan


def test_mod3_blindness():
    assert mod3_blindness_2T()                     # omega^k - 1 divisible by (1 - omega) in Z[omega]


def test_det_lemma_2T():
    gd = group_data("2T")
    ct = character_table(gd)                       # exact gates inside (orthonormality, FS, sum d^2)
    dl = det_lemma(gd, ct)
    fs_to_adm = sorted((d["fs"], d["sl2_admissible"]) for d in dl.values())
    assert fs_to_adm == [(-1, True), (0, False), (0, False)]   # quaternionic 2 yes; omega-twisted 2',2'' no


def test_a4_omega_window():
    sc = h104_scan("A4")
    assert sc["assemblies"] == 1089 and sc["complex_assemblies"] == 1028
    assert not sc["all_chars_real"]                # the omega characters are the window


def test_reality_theorem_groups():
    for g in ("S4", "A5"):
        sc = h104_scan(g)
        assert sc["all_chars_real"] and sc["complex_assemblies"] == 0   # closed by the reality theorem


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full 2T/2O/2I sweep ~minutes; banked counts asserted under OA_SLOW=1")
def test_full_sweep_slow():
    sc = h104_scan("2T")
    assert sc["assemblies"] == 71192 and sc["complex_assemblies"] == 70262
    for g in ("2O", "2I"):
        sc = h104_scan(g)
        assert sc["all_chars_real"] and sc["complex_assemblies"] == 0
