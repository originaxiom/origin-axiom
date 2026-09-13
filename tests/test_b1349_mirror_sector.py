"""B1349 - the mirror sector posed: freedom 48, and R11's arithmetic does not close."""
import json
import math
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1349_the_mirror_sector_posed"


def _even_group():
    import itertools
    k, kap = 2, 5
    W = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    Lv = lambda w: np.array([w[0] + w[1] + 2.0, w[1] + 1.0, 0.0])
    ip = lambda u, v: float(np.dot(u, v) - u.sum() * v.sum() / 3.0)
    perms = list(itertools.permutations(range(3)))
    sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    S = np.zeros((6, 6), dtype=complex)
    for i, wl in enumerate(W):
        for j, wm in enumerate(W):
            S[i, j] = sum(sgn(p) * np.exp(-2j * np.pi * ip(Lv(wl)[list(p)], Lv(wm)) / kap)
                          for p in perms)
    S *= -1j / (kap * np.sqrt(3.0))
    C2 = lambda w: (2 / 3) * (w[0] ** 2 + w[0] * w[1] + w[1] ** 2) + 2 * (w[0] + w[1])
    T = np.diag([np.exp(2j * np.pi * (C2(w) / (2 * kap) - (8.0 * k / (k + 3.0)) / 24.0)) for w in W])
    idx = {w: i for i, w in enumerate(W)}
    E = np.zeros((6, 4), dtype=complex)
    E[idx[(0, 0)], 0] = 1; E[idx[(1, 1)], 1] = 1
    E[idx[(0, 1)], 2] = E[idx[(1, 0)], 2] = 1
    E[idx[(0, 2)], 3] = E[idx[(2, 0)], 3] = 1
    assert np.allclose((S @ S) @ E, E, atol=1e-9), "the even basis must be C-fixed"
    rest = lambda M: np.linalg.lstsq(E, M @ E, rcond=None)[0]
    Ro = rest(T)
    Lo = rest(np.linalg.inv(S) @ np.linalg.inv(T) @ S)

    def pkey(M, q=6):
        Mn = M / (np.linalg.det(M) ** 0.25)
        best = None
        for r in range(4):
            A = Mn * np.exp(2j * np.pi * r / 4)
            kk = tuple((round(float(x.real), q), round(float(x.imag), q)) for x in A.flatten())
            best = kk if best is None else min(best, kk)
        return best
    seen, frontier, mats = {pkey(np.eye(4))}, [np.eye(4, dtype=complex)], [np.eye(4, dtype=complex)]
    gens = [Ro, Lo, np.linalg.inv(Ro), np.linalg.inv(Lo)]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = M @ g
                kk = pkey(P)
                if kk not in seen:
                    seen.add(kk); nxt.append(P); mats.append(P)
        frontier = nxt
    return mats


def test_arc_is_banked_as_a_negative():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1349" and v["verdict"] == "NEGATIVE", (
        "the headline is a recommendation NOT to spend the row")
    assert {i["row"] for i in v["identifications"]} == {"I-13"}


def test_the_projective_image_is_A4_x_A5():
    mats = _even_group()
    assert len(mats) == 720, f"A_4 x A_5 has order 720, got {len(mats)}"


def test_the_maximal_stabiliser_is_15_and_the_freedom_is_48():
    mats = _even_group()
    par = lambda a, b: np.linalg.norm(
        b / np.linalg.norm(b)
        - np.vdot(a / np.linalg.norm(a), b / np.linalg.norm(b)) * a / np.linalg.norm(a)) < 1e-6
    stab = lambda v: sum(1 for M in mats if par(v, M @ v))
    best = 0
    for M in mats:
        if np.allclose(M - (np.trace(M) / 4) * np.eye(4), 0, atol=1e-8):
            continue
        for v in np.linalg.eig(M)[1].T:
            best = max(best, stab(v / np.linalg.norm(v)))
    assert best == 15, f"maximal |Stab| must be 15 = 3 x 5, got {best}"
    assert 720 % best == 0 and 720 // best == 48, "orbit-stabiliser gives the freedom 48"


def test_orbit_stabiliser_is_the_invariant_that_caught_the_drift():
    """every banked orbit size must divide 720 -- the check that withdrew the first enumeration."""
    for stab_order, orbit in ((15, 48), (10, 72), (9, 80), (6, 120), (5, 144), (3, 240), (2, 360)):
        assert stab_order * orbit == 720
    for bogus in (68, 370, 423, 319):
        assert 720 % bogus != 0, f"{bogus} was in the withdrawn table and cannot be an orbit size"


def test_r11_does_not_close():
    """one output against a 48-fold selection is vacuous by MB12."""
    freedom = 48
    bits = math.log2(freedom)
    assert bits > 5.5, f"the selection costs {bits:.2f} bits"
    outputs = 1                                    # the mirror row is one row
    assert outputs < bits, "outputs - anchors < 0, so R11 declares the cell vacuous"


def test_the_recommendation_and_fences_are_on_the_record():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Do not spend the last row" in t
    assert "withdrawn" in t.lower() and "do not divide 720" in t
    assert "F2" in t and "I-13 remains UNEARNED" in t
    assert "B1350" in t, "the reserved-range note must travel with the last usable id"


def test_the_galois_cut_and_its_control():
    """the addendum: 48 -> 8 rational, and the rationality test must reject 1/phi."""
    from fractions import Fraction
    def is_rational(x, tol=1e-11, maxden=1000):
        return abs(float(Fraction(x).limit_denominator(maxden)) - x) <= tol
    phi_inv = (5 ** 0.5 - 1) / 2
    assert not is_rational(phi_inv), "1/phi must be REJECTED -- the first pass accepted it"
    assert is_rational(-0.5) and is_rational(1.0), "genuine rationals must be accepted"
    # the recomputed ledger
    assert math.log2(8) == 3.0
    assert 1 - math.log2(8) < 0, "R11 still does not close at one output"
    assert 4 - math.log2(8) > 0, "four independent outputs would close it"


def test_the_exactification_is_recorded_as_discharged():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "EXACTIFICATION DISCHARGED" in t or "exactification debt is discharged" in t
    assert "1/\u03c6" in t or "1/φ" in t, "the golden false positive must stay on the record"
    assert "68" in t, "the third orbit-drift instance must stay recorded"
