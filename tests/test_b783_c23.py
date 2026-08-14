"""C23 -- the T1-mover no-go. Locks on FALSIFIABLE computed facts (not entailed restatements).

NOTE (self-correction 2026-07-24): the first version of this lock asserted "distinct
signatures => only the identity permutation preserves them", which is ENTAILED by
distinctness and cannot fail — an L1/MB12 vacuity, the exact rule cc had just made binding
on the Wave-6 cells. Replaced with the computed geometric facts the wall actually rests on.
"""
import itertools
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B775_phase2_wave1"


def test_geometric_pair_is_non_real_so_c_has_a_free_orbit():
    # THE load-bearing fact (can fail: a real curve, or a c fixing rho, breaks it)
    y, x = sp.symbols("y x")
    curve = y**2 - (x**2 - 1) * y + (x**2 - 1)      # the B711 character-variety curve
    rho, rhobar = sp.solve(curve.subs(x, 2), y)
    assert sp.simplify(sp.im(sp.nsimplify(rho))) != 0        # rho_geo is NON-real
    assert sp.simplify(sp.conjugate(rho) - rho) != 0          # c MOVES it
    assert sp.simplify(sp.conjugate(rho) - rhobar) == 0       # c SWAPS the pair (free orbit)
    # and the pair is Galois-conjugate over Q (symmetric functions rational)
    assert sp.simplify(rho + rhobar).is_rational and sp.simplify(rho * rhobar).is_rational


def test_V4_abelian_so_any_mover_must_be_outer():
    # C21's premise, re-locked (can fail for a non-abelian group)
    V4 = list(itertools.product([0, 1], repeat=2))
    mul = lambda a, b: tuple((p + q) % 2 for p, q in zip(a, b))
    for g in V4:
        for v in V4:
            assert mul(mul(g, v), g) == v          # conjugation trivial => inner action trivial


def test_c23_banked_from_wave1():
    d = json.loads((ARC / "wave1_results.json").read_text())
    cell = next(c for c in d["cells"] if c["id"] == "P2-T1MOVER")
    assert cell["verdict"] == "RESOLVED-B" and cell["upheld"] is True
