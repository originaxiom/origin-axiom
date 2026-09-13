"""B1349 addendum 2 - the theta-even readout is ear-dependent exactly on the units of Z/15.

Independently re-derives the law from the SU(3)_2 modular data (no import of the arc's code),
then pins the exact closed forms and the output counts. Also LOCKS THE WITHDRAWN INSTRUMENT:
b1349d dropped the charge-conjugation weld C and compared complex values, and the test asserts
that doing so really does destroy the odd sector's ear-independence -- so the error cannot
silently return.
"""
import itertools
import json
import math
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1349_the_mirror_sector_posed"
PHI = (1 + 5 ** 0.5) / 2


def _data():
    """SU(3)_2 modular data, charge conjugation C, and the two theta-graded real bases."""
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
    ix = {w: i for i, w in enumerate(W)}
    C = np.zeros((6, 6))
    for i, w in enumerate(W):
        C[ix[(w[1], w[0])], i] = 1.0
    Bev = np.zeros((6, 4))
    Bev[ix[(0, 0)], 0] = 1; Bev[ix[(1, 1)], 1] = 1
    Bev[ix[(0, 1)], 2] = Bev[ix[(1, 0)], 2] = 1
    Bev[ix[(0, 2)], 3] = Bev[ix[(2, 0)], 3] = 1
    Bod = np.zeros((6, 2))
    Bod[ix[(0, 1)], 0], Bod[ix[(1, 0)], 0] = 1.0, -1.0
    Bod[ix[(0, 2)], 1], Bod[ix[(2, 0)], 1] = 1.0, -1.0
    R = T
    L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    return S, T, C, R, L, Bev, Bod


S, T, C, R, L, BEV, BOD = _data()


def _weld(m, use_C=True):
    P = np.linalg.matrix_power(R, m) @ np.linalg.matrix_power(L, m)
    return (C @ P) if use_C else P


def _form(m, B, use_C=True):
    """(G^-1 Sym(Re A), G) with A = B^T weld B -- the exact criterion's float image."""
    A = B.T @ _weld(m, use_C) @ B
    Qm = 0.5 * (A.real + A.real.T)
    G = B.T @ B
    return np.linalg.inv(G) @ Qm, G, Qm


def _is_scalar(M, tol=1e-10):
    lam = np.trace(M) / M.shape[0]
    return np.max(np.abs(M - lam * np.eye(M.shape[0]))) < tol, lam


def test_controls_on_the_modular_data():
    assert np.allclose(S, S.T, atol=1e-12)
    assert np.allclose(S @ S.conj().T, np.eye(6), atol=1e-12)
    assert np.allclose(S @ S, C, atol=1e-9), "C must be S^2, the charge conjugation"
    assert np.allclose(C @ C, np.eye(6), atol=1e-12)
    assert np.allclose(np.linalg.matrix_power(R, 15), np.eye(6), atol=1e-9)
    assert np.allclose(np.linalg.matrix_power(L, 15), np.eye(6), atol=1e-9)
    # C IS the theta-grading operator
    assert np.allclose(C @ BEV, BEV, atol=1e-12)
    assert np.allclose(C @ BOD, -BOD, atol=1e-12)


def test_scalar_criterion_is_not_vacuous():
    """CONTROL against E2: the criterion must REJECT a deliberately non-scalar form."""
    ok, _ = _is_scalar(np.diag([1.0, 1.0, 1.0, 2.0]))
    assert not ok, "the scalar test must reject diag(1,1,1,2)"
    ok2, lam2 = _is_scalar(np.eye(4) * 0.375)
    assert ok2 and abs(lam2 - 0.375) < 1e-14, "the scalar test must accept a true scalar"


def test_b856_reproduced_with_the_weld():
    """h(5) = -1 exactly and the golden |h|^2 pair -- B856's banked values."""
    u3 = np.zeros(6); u3[[1, 3]] = [1 / np.sqrt(2), -1 / np.sqrt(2)]   # (e(0,1)-e(1,0))/sqrt2
    hs = {m: complex(u3 @ _weld(m) @ u3) for m in range(1, 6)}
    assert abs(hs[5] + 1.0) < 1e-9, f"B856 banks h(5) = -1, got {hs[5]}"
    golden = {1 / (PHI * 5 ** 0.5), PHI / 5 ** 0.5, 1.0}
    for m, h in hs.items():
        assert min(abs(abs(h) ** 2 - g) for g in golden) < 1e-9, (m, abs(h) ** 2)
    assert abs(1 / (PHI * 5 ** 0.5) + PHI / 5 ** 0.5 - 1.0) < 1e-12, "the golden pair sums to 1"
    assert abs(hs[1].real - 1 / (2 * PHI)) < 1e-9, "Re h(1) = 1/(2 phi)"


def test_odd_sector_ear_independent_on_the_whole_period():
    """B856 reports 2e-16 at m=1; it holds for every m -- and it NEEDS the weld."""
    for m in range(1, 16):
        M, _, _ = _form(m, BOD)
        ok, _ = _is_scalar(M)
        assert ok, f"odd sector must be ear-independent at m={m}"
    assert len({round(_is_scalar(_form(m, BOD)[0])[1], 9) for m in range(1, 16)}) == 3
    # period 5, exactly (B856's collapse from ord 15)
    for m in range(1, 16):
        a = _is_scalar(_form(m, BOD)[0])[1]
        b = _is_scalar(_form((m + 5 - 1) % 15 + 1, BOD)[0])[1]
        assert abs(a - b) < 1e-9, f"odd Re h must have period 5 (m={m})"


def test_withdrawn_instrument_the_bug_was_complex_vs_real():
    """LOCK THE WITHDRAWAL, and lock WHICH deviation caused it.

    b1349d made two: it dropped the weld C, and it compared COMPLEX h instead of Re h.
    Only the second broke anything -- C merely negates lambda. Pinned so the diagnosis
    in addendum 2 section 0(a) cannot drift.
    """
    # dropping C does NOT break ear-independence; it flips the sign
    for m in range(1, 6):
        okw, lamw = _is_scalar(_form(m, BOD, use_C=True)[0])
        okn, lamn = _is_scalar(_form(m, BOD, use_C=False)[0])
        assert okw and okn, f"Re h stays scalar with and without C (m={m})"
        assert abs(lamw + lamn) < 1e-9, f"dropping C must NEGATE lambda (m={m})"
    # the sign B856 pins is what the missing weld actually cost
    u3 = np.zeros(6); u3[[1, 3]] = [1 / np.sqrt(2), -1 / np.sqrt(2)]
    assert abs(complex(u3 @ _weld(5, use_C=False) @ u3) - 1.0) < 1e-9, "unwelded gives +1"
    assert abs(complex(u3 @ _weld(5, use_C=True) @ u3) + 1.0) < 1e-9, "welded gives B856's -1"
    # THE ACTUAL BUG: complex h is ear-dependent on the odd sector, Re h is not
    Gm = BOD.T @ BOD
    ears = [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex),
            np.array([1, 1], dtype=complex) / np.sqrt(2), np.array([3, 4], dtype=complex) / 5]
    A = BOD.T @ _weld(1) @ BOD
    hs = [complex(np.conj(c) @ A @ c) / complex(np.conj(c) @ Gm @ c) for c in ears]
    assert max(abs(a - b) for a in hs for b in hs) > 0.5, "complex h IS ear-dependent"
    assert max(abs(a.real - b.real) for a in hs for b in hs) < 1e-10, "Re h is NOT"


def test_the_gcd_law_over_the_complete_period():
    """THE LAW: theta-even Re h is ear-independent  <=>  gcd(m,15) > 1. Complete, not inductive."""
    dep, indep = [], []
    for m in range(1, 16):
        M, _, _ = _form(m, BEV)
        (indep if _is_scalar(M)[0] else dep).append(m)
    assert dep == [1, 2, 4, 7, 8, 11, 13, 14], dep
    assert indep == [3, 5, 6, 9, 10, 12, 15], indep
    assert dep == [m for m in range(1, 16) if math.gcd(m, 15) == 1]
    assert len(dep) == 8, "phi(15) = 8"
    # the ear-dependent readings are TRACELESS: no mean, only spread
    for m in dep:
        M, _, _ = _form(m, BEV)
        assert abs(np.trace(M)) < 1e-9, f"m={m} must be traceless"
    # the four forced values
    lams = sorted({round(_is_scalar(_form(m, BEV)[0])[1], 9) for m in indep})
    assert lams == sorted({round(v, 9) for v in (-1 / (2 * PHI), 0.0, 0.5, 1.0)}), lams
    assert len(lams) == 4, "addendum 1 asked for four independent numbers"


def _spectrum(m):
    """generalised eigenvalues of (Q, G): G^-1 Q is NOT symmetric, so symmetrise first."""
    _, G, Qm = _form(m, BEV)
    Gh = np.diag(1.0 / np.sqrt(np.diag(G)))
    return np.sort(np.linalg.eigvalsh(Gh @ Qm @ Gh))


def test_ear_dependent_spectra_are_the_proved_closed_forms():
    """Every ear-dependent eigenvalue is (1/(2 sqrt2)) x a unit of Z[phi].

    Proved exactly in b1349e_charpoly.py (radsimp(got - claim) == 0); pinned here.
    """
    s2 = 2 * 2 ** 0.5
    for ms, units in [((1, 4, 11, 14), (PHI ** 2, 1 / PHI)),
                      ((2, 7, 8, 13), (5 ** 0.5, 1.0))]:
        want = sorted([-units[0] / s2, -units[1] / s2, units[1] / s2, units[0] / s2])
        for m in ms:
            assert np.allclose(_spectrum(m), want, atol=1e-9), (m, _spectrum(m), want)
    # sqrt10/4 == sqrt5/(2 sqrt2), the form addendum 2 states
    assert abs(10 ** 0.5 / 4 - 5 ** 0.5 / s2) < 1e-15
    # the ear-INDEPENDENT spectra are genuinely scalar
    for m, lam in [(3, 0.5), (12, 0.5), (5, 0.0), (10, 0.0),
                   (6, -1 / (2 * PHI)), (9, -1 / (2 * PHI)), (15, 1.0)]:
        assert np.allclose(_spectrum(m), [lam] * 4, atol=1e-9), (m, _spectrum(m))
    # sqrt2 is NOT in Q(zeta_60): conductor(Q(sqrt2)) = 8 does not divide 60
    assert 60 % 8 != 0, "the field statement rests on 8 not dividing 60"


def _rank(ms, extra=None):
    """rank over R of the span of {Q_m} in Sym_4(R), with the gap asserted unambiguous."""
    rows = [[_form(m, BEV)[2][i, j] for i in range(4) for j in range(i, 4)] for m in ms]
    if extra is not None:
        rows = rows + [[extra[i, j] for i in range(4) for j in range(i, 4)]]
    sv = np.linalg.svd(np.array(rows, dtype=float), compute_uv=False)
    r = int((sv > sv[0] * 1e-9).sum())
    assert sv[r - 1] / sv[0] > 1e-3, f"rank {r} not unambiguous: {sv}"
    if r < len(sv):
        assert sv[r] / sv[0] < 1e-9, f"rank {r} not unambiguous: {sv}"
    return r


def test_output_counts_over_the_REALS():
    """The count is dim_R span{Q_m}, NOT the Q-rank of Q(zeta_60) coefficient vectors.

    A first pass reported 6 by taking the rank over Q of power-basis coefficient vectors --
    that inflates by the field degree (1 and sqrt5 are Q-independent but both real scalars).
    The honest count is 3, and it reverses branch B's verdict. See addendum 2 section 0(c).
    """
    ALL = list(range(1, 16))
    UNITS = [m for m in ALL if math.gcd(m, 15) == 1]
    NON = [m for m in ALL if math.gcd(m, 15) != 1]
    G = BEV.T @ BEV
    assert _rank(ALL) == 3, "dim_R span over the whole period"
    assert _rank(UNITS) == 2, "the ear-dependent forms span 2 dimensions"
    assert _rank(NON) == 1, "the ear-independent forms are all proportional to G"
    assert _rank(ALL, extra=G) == 3, "G lies in the span of all 15"
    assert _rank(UNITS, extra=G) == 3, "G does NOT lie in the ear-dependent span"
    # either way: 2 ear-discriminating directions, which is < 3 bits -> branch B FAILS R11
    assert _rank(ALL) - 1 == 2 and _rank(UNITS) == 2
    # 8 distinct Re h at the anchor ear -- 8 readings, but only 3 independent forms
    vals = {round(_form(m, BEV)[2][0, 0], 9) for m in range(1, 16)}
    assert len(vals) == 8, sorted(vals)
    # branch A: four forced values, no direction selected
    lams = sorted({round(_is_scalar(_form(m, BEV)[0])[1], 9) for m in NON})
    assert len(lams) == 4 and sum(1 for v in lams if abs(v - round(v, 3)) > 0) >= 0
    assert min(lams) == round(-1 / (2 * PHI), 9), "the lone value outside Q"


def test_results_json_matches():
    res = json.loads((ARC / "verification" / "b1349e_results.json").read_text())
    for m in range(1, 16):
        row = res["even"][str(m)]
        assert row["gcd"] == math.gcd(m, 15)
        assert row["ear_independent"] == (math.gcd(m, 15) > 1)
        assert res["odd"][str(m)]["ear_independent"] is True


# --- addendum 3: the 4/4 orbit split, and branch B's tie at zero ---

def _proj_eq(u, v, tol=1e-7):
    """Projective equality, INDEX-FREE and ROUNDING-FREE: [u] == [v] iff |<u,v>| = |u||v|.

    WHY NOT A ROUNDED KEY. The first version of this test canonicalised by dividing by the
    argmax entry and rounding to 9 decimals, and the orbit came out at 66 -- which does not
    divide 720, so the orbit-stabiliser assert caught it. That is the FOURTH float drift in
    this family (B1348 step 4: 68; B1349: 370, 423; here: 66) and it has two causes, both
    boundary effects: np.round splits values that straddle a rounding boundary, and argmax
    flips the pivot between entries of nearly equal magnitude. A Cauchy-Schwarz test has
    neither a pivot nor a boundary. The EXACT settlement is verification/b1349f_orbit_split.py,
    which divides in Q(zeta_60) and needs no tolerance at all.
    """
    u = np.asarray(u, dtype=complex); v = np.asarray(v, dtype=complex)
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    return abs(abs(np.vdot(u, v)) - nu * nv) < tol * nu * nv


def _find(pts, w):
    for i, p in enumerate(pts):
        if _proj_eq(p, w):
            return i
    return -1


def _even_restriction():
    """R, L restricted to the 4-dim theta-even sector; BEV is a 0/1 selection, so read the blocks."""
    rows = [1 - 1, 4, 1, 2]           # placeholder, replaced below by index lookup
    # recover the weight order used by _data()
    k = 2
    W = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    ix = {w: i for i, w in enumerate(W)}
    rows = [ix[(0, 0)], ix[(1, 1)], ix[(0, 1)], ix[(0, 2)]]
    R4 = np.array([[(R @ BEV)[r, b] for b in range(4)] for r in rows])
    L4 = np.array([[(L @ BEV)[r, b] for b in range(4)] for r in rows])
    # the restriction must be faithful: M6 . BEV == BEV . M4
    assert np.allclose(R @ BEV, BEV @ R4, atol=1e-9), "R must restrict exactly"
    assert np.allclose(L @ BEV, BEV @ L4, atol=1e-9), "L must restrict exactly"
    return R4, L4


def _orbit(v0, gens, cap=400):
    pts = [np.asarray(v0, dtype=complex)]
    frontier = [pts[0]]
    while frontier:
        nxt = []
        for v in frontier:
            for M in gens:
                w = M @ v
                if _find(pts, w) < 0:
                    pts.append(w); nxt.append(w)
                    assert len(pts) <= cap, "orbit exceeded cap"
        frontier = nxt
    return pts


RATIONAL_DIRECTIONS = {
    "e1": [1, 0, 0, 0], "e2": [0, 1, 0, 0], "e3": [0, 0, 1, 0], "e4": [0, 0, 0, 1],
    "(1,0,0,-1/2)": [1, 0, 0, -0.5], "(1,0,0,1)": [1, 0, 0, 1],
    "(0,1,1,0)": [0, 1, 1, 0], "(0,1,-1/2,0)": [0, 1, -0.5, 0],
}


def test_the_eight_rationals_split_four_and_four():
    """THE SPLIT: two orbits of 48, four rationals each. Addendum 1 left this OPEN.

    Every orbit size must divide 720 -- the orbit-stabiliser invariant that caught three
    earlier float drifts (reported 68, 370, 423). Asserted, not hoped for.
    """
    gens = _even_restriction()
    orbits = []
    for name, v in RATIONAL_DIRECTIONS.items():
        for members, names in orbits:
            if _find(members, v) >= 0:
                names.append(name); break
        else:
            O = _orbit(v, gens)
            assert 720 % len(O) == 0, f"|orbit| = {len(O)} must divide 720 ({name})"
            assert len(O) == 48, f"{name}: expected the 48-orbit, got {len(O)}"
            orbits.append((O, [name]))
    assert len(orbits) == 2, f"expected exactly two orbits, got {len(orbits)}"
    assert sorted(len(n) for _, n in orbits) == [4, 4], [n for _, n in orbits]
    assert sum(len(n) for _, n in orbits) == 8
    # the membership itself, as banked
    byname = {frozenset(n) for _, n in orbits}
    assert byname == {frozenset({"e1", "e2", "(1,0,0,1)", "(0,1,1,0)"}),
                      frozenset({"e3", "e4", "(1,0,0,-1/2)", "(0,1,-1/2,0)"})}, byname


def test_branch_B_ties_at_zero_and_no_third_direction_exists():
    """One orbit => log2(4) = 2 bits, so branch B reads 2 - 2 = 0. R11 needs > 0, so it FAILS.

    And the tie cannot be broken from inside the sector: there is provably no third
    ear-discriminating direction.
    """
    anchor_bits_one_orbit = math.log2(4)
    assert anchor_bits_one_orbit == 2.0
    UNITS = [m for m in range(1, 16) if math.gcd(m, 15) == 1]
    outputs = _rank(UNITS)
    assert outputs == 2, "the ear-dependent forms span exactly 2 dimensions"
    assert outputs - anchor_bits_one_orbit == 0.0, "branch B ties at zero"
    assert not (outputs - anchor_bits_one_orbit > 0), "a tie is NOT a close under R11"
    # no third direction: adding G does not raise the unit-span past 3, and the units alone stop at 2
    assert _rank(UNITS, extra=BEV.T @ BEV) == 3, "G is outside the unit span, so 2 is the ceiling"
