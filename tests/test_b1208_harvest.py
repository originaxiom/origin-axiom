"""B1208 — the five-memo harvest: the locks pin what the VERIFICATION established, not what the
memos claimed. Each of these is a fact this bench computed from main's own data.
"""
import importlib.util
import json
from itertools import combinations, product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1208_cross_seat_harvest"


def test_rank_one_is_impossible_under_SU2_but_NOT_under_t3_alone():
    """LEG 1: the correction. The memo derived the exclusion from t3-conservation; that gives
    antidiagonal support, which still admits rank 1. Full SU(2) is what excludes it. Both halves
    are asserted, because dropping either one is how the error happened."""
    def rank2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        if a == b == c == d == 0: return 0
        return 2 if a * d - b * c != 0 else 1
    # (a) t3 alone: the antidiagonal witness with one vanishing entry has rank 1
    assert rank2([[0, -3], [0, 0]]) == 1, "the rank-1 witness must survive the Cartan gate"
    # (b) full su(2): the invariant space is 1-dimensional and its determinant is a square
    a, b, c, d = sp.symbols("a b c d")
    B = sp.Matrix([[a, b], [c, d]])
    J3 = sp.Rational(1, 2) * sp.Matrix([[1, 0], [0, -1]])
    Jp, Jm = sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]])
    sol = sp.solve([e for X in (J3, Jp, Jm) for e in list(X.T * B + B * X)], [a, b, c, d], dict=True)[0]
    Binv = sp.simplify(B.subs(sol))
    free = sorted(Binv.free_symbols, key=str)
    assert len(free) == 1, "the SU(2) singlet in 2 (x) 2 is one-dimensional"
    assert sp.simplify(Binv.det() - free[0] ** 2) == 0, "det is a perfect square: rank in {0, 2}"


def test_the_census_does_not_force_the_3x3x4_shape():
    """LEG 2's caveat: B1185 called 3x3x4 'derived' from the census. Three factorizations fit."""
    census = (18, 9, 6, 3)
    sols = {(a1 + a2, b1 + b2, h) for a1, a2, b1, b2, h in product(range(1, 13), repeat=5)
            if (a1 * b1 * h, a2 * b1 * h, a1 * b2 * h, a2 * b2 * h) == census}
    assert sols == {(3, 4, 3), (3, 12, 1), (9, 4, 1)}, sols
    assert len(sols) > 1, "if this ever becomes unique the caveat can be retired"


def test_signed_CS_is_two_valued_at_every_volume_in_the_census():
    """LEG 3 / S5b, on main's own B1197 rows: B289's sign law makes signed CS a non-function of
    Vol, which is what refutes D2's variable reading -- by a control banked before the run."""
    c = json.loads((ROOT / "frontier" / "B1197_clock_coherence" / "verification" /
                    "b4_correct.json").read_text(encoding="utf-8"))
    rows = c["census"]
    assert len(rows) == 156 and c["control_sign_law"] == [156, 156]
    pairs = [(i, j) for i, j in combinations(range(len(rows)), 2)
             if abs(rows[i]["vol"] - rows[j]["vol"]) < 1e-9
             and abs(rows[i]["cs"] - rows[j]["cs"]) > 1e-9]
    assert len(pairs) == 156, f"expected every closing to be paired; got {len(pairs)}"
    opp = [(i, j) for i, j in pairs if abs(rows[i]["cs"] + rows[j]["cs"]) < 1e-7]
    assert len(opp) == len(pairs), "the sign law says the pair values are exactly opposite"


def test_absCS_is_not_a_function_of_volume_either():
    """LEG 3 / S5: the repair fails too, and this bench's witness is far steeper than the memo's."""
    g = json.loads((ROOT / "frontier" / "B1197_clock_coherence" / "verification" /
                    "b4_global.json").read_text(encoding="utf-8"))
    rows = sorted(g["rows"], key=lambda r: r["vol"])
    best = 0.0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            dv = rows[j]["vol"] - rows[i]["vol"]
            if dv > 0.0055: break
            if dv > 0:
                best = max(best, abs(rows[j]["abs_cs"] - rows[i]["abs_cs"]) / dv)
    assert best > 100, f"|CS| varies at least 100x faster than Vol somewhere; got {best:.1f}x"


def test_no_abelian_character_of_the_27_stabilizes_a_neutral():
    """LEG 4, rebuilt on main's own weight generator and in the stronger 'any 2-subset' form.
    Restricted to n = 2, 3 so the lock stays fast; the full n = 2..6 sweep is in the reproducer."""
    spec = importlib.util.spec_from_file_location(
        "tt", ROOT / "frontier" / "B299_trinification_triality" / "trinification_triality.py")
    tt = importlib.util.module_from_spec(spec); spec.loader.exec_module(tt)
    W = tt._weights_27()
    assert len(W) == 27
    for n in (2, 3):
        for a in product(range(n), repeat=6):
            vals = [sum(ai * wi for ai, wi in zip(a, w)) % n for w in W]
            for cshift in range(n):
                k = sum(1 for v in vals if (v + cshift) % n != 0)
                assert not (0 < k <= 2), f"stabilizer found at n={n}, a={a}, c={cshift}"


def test_the_stabilizer_instrument_can_actually_fire():
    """MB12 for the leg above: a census that cannot succeed proves nothing."""
    fake = [(0,) * 6] * 25 + [(1,) + (0,) * 5, (2,) + (0,) * 5]
    found = 0
    for a in product(range(3), repeat=6):
        vals = [sum(ai * wi for ai, wi in zip(a, w)) % 3 for w in fake]
        for cshift in range(3):
            k = sum(1 for v in vals if (v + cshift) % 3 != 0)
            if 0 < k <= 2: found += 1
    assert found > 0, "the instrument cannot detect a stabilizer -- the negative would be vacuous"


def test_the_mirror_chain_and_its_primality_control():
    """LEG 5: cc3's chain, and the control that makes their Escape-(i) closure non-vacuous."""
    t = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    assert sp.simplify(t**2 - t + 1) == 0
    w = sp.simplify(t**2)
    assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0      # primitive cube root
    assert sp.simplify(w**2 + w + 1) == 0                              # Phi_3
    assert sp.simplify(w**2 - sp.conjugate(w)) == 0                    # the swap IS conjugation
    assert sp.simplify(sp.conjugate(t) - (1 - t)) == 0                 # and reverses orientation
    assert sp.simplify((1 - t)**2 - (1 - t) + 1) == 0                  # same relator
    # Escape (i) is vacuous exactly at prime order -- not merely at 2
    for n, vacuous in ((2, True), (3, True), (4, False), (6, False), (8, False), (9, False)):
        proper = [d for d in range(2, n) if n % d == 0]
        assert (not proper) == vacuous, n


def test_the_arc_records_the_fork_with_all_three_outcomes():
    """LEG 2's fork is the arc's forward-looking product; branch (b) flips a PERMANENT row, so it
    must not be quietly reduced to 'no change expected'."""
    r = json.loads((ARC / "b1208_results.json").read_text(encoding="utf-8"))
    fork = next(l for l in r["legs"] if l["leg"] == 2)["fork"]
    assert set(fork) == {"a", "b", "c"}
    assert "FORCED" in fork["b"] and "ABSENT" in fork["c"]
    assert "character" in next(l for l in r["legs"] if l["leg"] == 2)["decisive_datum"]


def test_kappa_is_preserved_by_the_internal_group_and_separates_the_mirror():
    """LEG 6 and the convergence: the SAME identity that made B1203's climb generate no new
    invariant is what makes the mirror irremovable. Both directions are asserted here, because the
    pairing is the finding -- either alone is half of it."""
    x, y, z = sp.symbols("x y z")
    kappa = x**2 + y**2 + z**2 - x*y*z - 2
    internal = {"letter swap": (y, x, z), "lift a": (-x, y, -z), "lift b": (x, -y, -z),
                "tau_a": (x, z, x*z - y), "tau_b": (z, y, y*z - x),
                "B1203 climb": (z, x, x*z - y)}
    for name, (X, Y, Z) in internal.items():
        assert sp.expand(kappa.subs({x: X, y: Y, z: Z}, simultaneous=True) - kappa) == 0, name
    # MB12: the identity must be able to fail, or invariance is vacuous
    assert sp.expand(kappa.subs({x: x**2 - 2}, simultaneous=True) - kappa) != 0
    # and kappa separates the object's point from its mirror
    w = sp.symbols("w")
    red = lambda e: sp.simplify(sp.rem(sp.expand(e), w**2 - w + 1, w))
    k0 = red(kappa.subs({x: 2, y: 2, z: 2 - w}, simultaneous=True))
    kg = red(kappa.subs({x: 2, y: 2, z: 1 + w}, simultaneous=True))
    assert sp.simplify(k0 - (1 + w)) == 0 and sp.simplify(kg - (2 - w)) == 0
    assert sp.simplify(k0 - kg) != 0, "if kappa stopped separating them the proof would collapse"
    assert sp.simplify(red(k0 + kg) - 3) == 0 and sp.simplify(red(k0 * kg) - 3) == 0
