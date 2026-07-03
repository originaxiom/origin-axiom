"""Locks for B371 — the minimal two-state sector (all exact)."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B371_minimal_two_state_sector"))

from slot_verification import run

REPORT = run()


def test_slot_invariant_and_irreducible_mechanism():
    assert REPORT["V1_invariant"] is True
    assert REPORT["V4_dihedral_global"] is True


def test_metallic_traces_exact():
    assert REPORT["V2_traces"][1] == ("1/2", "-1/2", "0", "0")   # 1 - phi
    assert REPORT["V2_traces"][4] == ("1/2", "-1/2", "0", "0")
    assert REPORT["V2_traces"][2] == ("1", "0", "0", "0")
    assert REPORT["V2_traces"][3] == ("1", "0", "0", "0")


def test_helicity_pairing():
    assert REPORT["V3_helicity"] is True and REPORT["V3b_square"] is True


def test_true_parity_and_weyl_identity():
    assert REPORT["V5_J_commutes"] is True
    assert REPORT["V5b_J_monomial_1_minus_j"] is True
    assert REPORT["E3_weyl_identity"] is True
