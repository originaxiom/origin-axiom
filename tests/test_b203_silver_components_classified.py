"""B203 -- the 4 silver SL(3) components are all irreducible & cusped-type (V196). Fast pyenv locks.

Loads the shipped reps (frontier/B203_silver_components_classified/comps.json), one per component
(incl. the new comp3): each is IRREDUCIBLE (Burnside dim 9) with A of INFINITE order (continuous
trace) -- i.e. cusped-type, NOT a finite-order-A Dehn-filling component (cf. figure-eight W1:
A=diag(1,i,-i), order 4). This explains B202 (no tidy A-variety relation). numpy-only; nothing to
CLAIMS.md.
"""
import os
import json
import numpy as np

HERE = os.path.dirname(__file__)
COMPS = os.path.join(HERE, "..", "frontier", "B203_silver_components_classified", "comps.json")
I3 = np.eye(3, dtype=complex)


def _mat(M):
    return np.array([[complex(a, b) for (a, b) in row] for row in M], dtype=complex)


def burnside(A, B, rounds=6):
    gens = [A, B, np.linalg.inv(A), np.linalg.inv(B)]
    allm = [I3]; fr = [I3]
    for _ in range(rounds):
        fr = [g @ m for m in fr for g in gens]; allm += fr
    return int(np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]), tol=1e-7))


def order_of(M, maxd=24):
    e = np.linalg.eigvals(M)
    return next((d for d in range(1, maxd + 1) if np.max(np.abs(e ** d - 1)) < 1e-6), None)


def test_all_four_silver_components_irreducible_and_cusped():
    d = json.load(open(COMPS))
    assert set(d.keys()) == {"comp0", "comp1", "comp2", "comp3"}, d.keys()
    for name, rep in d.items():
        A, B = _mat(rep["A"]), _mat(rep["B"])
        assert burnside(A, B) == 9, (name, "reducible")          # irreducible
        assert order_of(A) is None, (name, "A finite order")     # cusped-type (A infinite order)
        assert order_of(B) is None, (name, "B finite order")


def test_comp3_is_genuinely_new_irreducible():
    # the new comp3 {tr A+tr A^-1 = -1} is a genuine irreducible component (not a reducible artifact)
    d = json.load(open(COMPS))
    A, B = _mat(d["comp3"]["A"]), _mat(d["comp3"]["B"])
    assert burnside(A, B) == 9
    assert abs((np.trace(A) + np.trace(np.linalg.inv(A))) - (-1)) < 1e-6   # tr A + tr A^-1 = -1


if __name__ == "__main__":
    test_all_four_silver_components_irreducible_and_cusped()
    test_comp3_is_genuinely_new_irreducible()
    print("ALL CHECKS PASS")
