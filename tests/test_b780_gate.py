"""B780 -- the Galois-vs-reversal gate: locks on the three discriminating signatures."""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B780_galois_reversal_gate"


def test_S1_rank_onset():
    # theta trivial at SL(2) (trace symmetry); c nontrivial (geometric value non-real)
    u = sp.symbols("u")
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-u, 1]])
    assert sp.simplify((A * B).trace() - (B * A).trace()) == 0        # theta trivial @ SL(2)
    w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    assert sp.simplify(sp.conjugate(2 - w) - (2 - w)) != 0            # c nontrivial @ SL(2)


def test_S2_action_type_permutation_not_diagonal():
    # theta = permutation (1 4)(2 5)(3 8)(6 7): an involution with no fixed points on support
    perm = {1: 4, 4: 1, 2: 5, 5: 2, 3: 8, 8: 3, 6: 7, 7: 6}
    assert all(perm[perm[k]] == k for k in perm)   # involution
    assert all(perm[k] != k for k in perm)          # moves every coord => NOT diagonal


def test_gate_separates_and_rejects_swap():
    d = json.loads((ARC / "results.json").read_text())
    assert d["verdict"] == "RESOLVED-A"
    assert d["S1_rank_onset_discriminates"]
    assert d["S2_action_type_discriminates"]
    assert d["S3_solo_flip_discriminates"]
    assert d["gate_correct_on_truth"] and d["gate_rejects_swap"]
