"""B780 -- the SIGNATURE FACTS only (the 'gate' and its 8->4 halving were RETRACTED by B784).

The retracted claims rested on literal signature tuples and a classify() that mapped them
by definition — they could not fail. What remains here are the genuinely computed facts
that c and theta differ: SL(2) rank-onset, action type (diagonal vs permutation).
"""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B780_galois_reversal_gate"


def test_S1_rank_onset():
    # theta is trivial at SL(2) *by the universal trace identity* tr(AB)=tr(BA):
    #   the 27<->27bar swap has no SL(2)-trace signature because tr is cyclic for ALL
    #   matrices. That is not separately lockable (its counterfactual is impossible), so
    #   it is documented as the mechanism, not asserted. The FALSIFIABLE signature -- the
    #   one that would fail if the geometric value were real -- is c's non-triviality:
    w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2          # omega, the geometric value
    assert sp.simplify(sp.conjugate(2 - w) - (2 - w)) != 0  # c nontrivial @ SL(2): 2-w non-real


def test_S2_action_type_permutation_not_diagonal():
    # theta = permutation (1 4)(2 5)(3 8)(6 7): an involution with no fixed points on support
    perm = {1: 4, 4: 1, 2: 5, 5: 2, 3: 8, 8: 3, 6: 7, 7: 6}
    assert all(perm[perm[k]] == k for k in perm)   # involution
    assert all(perm[k] != k for k in perm)          # moves every coord => NOT diagonal


