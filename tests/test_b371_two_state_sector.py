"""Locks for B371 — the minimal two-state sector (all exact).

L184 lazy-fy (B1178/R50-5): the module-level `REPORT = run()` executed ~157 s of exact
computation AT COLLECTION (the E50 shape — 88% of the whole suite's collection time in this
one file). The compute now runs once, at first test execution, via the cached getter; the
import of the frontier engine is deferred with it. Test outcomes unchanged."""

import functools
import os
import sys


@functools.lru_cache(maxsize=1)
def _report():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                    "frontier", "B371_minimal_two_state_sector"))
    from slot_verification import run
    return run()


def test_slot_invariant_and_irreducible_mechanism():
    REPORT = _report()
    assert REPORT["V1_invariant"] is True
    assert REPORT["V4_dihedral_global"] is True


def test_metallic_traces_exact():
    REPORT = _report()
    assert REPORT["V2_traces"][1] == ("1/2", "-1/2", "0", "0")   # 1 - phi
    assert REPORT["V2_traces"][4] == ("1/2", "-1/2", "0", "0")
    assert REPORT["V2_traces"][2] == ("1", "0", "0", "0")
    assert REPORT["V2_traces"][3] == ("1", "0", "0", "0")


def test_helicity_pairing():
    REPORT = _report()
    assert REPORT["V3_helicity"] is True and REPORT["V3b_square"] is True


def test_true_parity_and_weyl_identity():
    REPORT = _report()
    assert REPORT["V5_J_commutes"] is True
    assert REPORT["V5b_J_monomial_1_minus_j"] is True
    assert REPORT["E3_weyl_identity"] is True
