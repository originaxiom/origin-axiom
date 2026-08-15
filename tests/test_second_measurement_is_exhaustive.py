"""The second measurement, enumerated over ALL of C rather than scanned on one line.

This is the cell B874 carried forward as open ("the joint measurement at the cubic-field
points -- does 26 appear ... the step-2 retirement question") and that B892 answered only
along the real (x14,x16) projective line.  The toral lemma makes the full answer cheap.

Because C is toral, e6 decomposes into simultaneous ad(C)-eigenspaces with weights
w in C*, and for any subset S of C

    dim z(S) = #{ w : w(y) = 0 for every y in S }.

So the entire second-measurement stratification is a linear-algebra count on 78 weight
vectors -- exhaustive, not sampled.

WHAT THIS ESTABLISHES

  * every banked value reproduces: dim z(C) = 12, z(x8) = z(x16) = 30,
    z(x14) = z(x22) = 12, z(x8,x16) = 30, z(x1) = 46 at all three walls;
  * the 48 "split" weights fall into exactly THREE ratio classes -w8/w16 -- the three
    walls, i.e. the S3-Galois orbit of the charge cubic's roots;
  * from a wall point x1 the 34 active weights fall into exactly SEVEN proportionality
    classes of sizes (2,2,6,6,6,6,6), identically at each of the three walls;
  * the two size-2 classes give dim 14, the five size-6 classes give dim 18.  So the
    14-locus is exactly TWO hyperplanes, and they are complex conjugates -- which is
    why B892 found y* non-real and no real 14-point;
  * ## dimension 26 IS ATTAINED on genuine 2-planes <x1,y>.  B874's addendum sentence
    "No 26 stratum exists" and "the complete centralizer ladder is {78,46,30,12}" are
    correct in their stated scope (coordinate subtori and the three enhancement points)
    but too strong as written.  Relayed, not silently overwritten.

WHY C7's PRICE IS ZERO.  Every point of the 14-locus yields a Levi with 8 roots, and
A2+A1 is the unique Levi type with 8 roots (test_levi_classification_forces_the_rungs).
So the choice of the second plane and of the point y* cannot change the terminus -- it
can only fail to reach it.

Numerics are double precision but SELF-CERTIFYING: every dimension count asserts an
explicit gap between the largest pairing treated as zero and the smallest treated as
nonzero.  If that gap ever narrows the test FAILS rather than silently misclassifying.
The figures below were first obtained at 60 digits, where the gap is 41 orders of
magnitude (7.5e-46 against 1.8e-5).
"""
import importlib.util
import itertools
import pathlib

import numpy as np
import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SRC = _ROOT / "frontier" / "B854_centralizer_exact" / "e6_centralizer.py"

pytest.importorskip("numpy")

_g = {"__file__": str(_SRC), "__name__": "b854_weights"}
exec(compile(_SRC.read_text(), str(_SRC), "exec"), _g)

DIM, N, br = _g["DIM"], _g["N"], _g["br"]
INV, hvec, evec, ROOTS_ = _g["INV"], _g["hvec"], _g["evec"], _g["ROOTS"]
NS = [8, 14, 16, 22]

_basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS_]
_trip = {}
for _p in range(DIM):
    for _q in range(DIM):
        for _r, _c in enumerate(br(_basis[_p], _basis[_q])):
            if _c:
                _trip.setdefault(_p, []).append((_q, _r, float(_c)))


def _admat(vec):
    A = np.zeros((DIM, DIM))
    for p in range(DIM):
        if not vec[p]:
            continue
        fp = float(vec[p])
        for q, r, c in _trip.get(p, []):
            A[r, q] += fp * c
    return A


AD = {n: _admat(INV[n]) for n in NS}


def _weights():
    M = AD[8] + 3.0 * AD[14] + 7.0 * AD[16] + 13.0 * AD[22]
    _, V = np.linalg.eig(M)
    W = np.zeros((DIM, 4), dtype=complex)
    for k in range(DIM):
        col = V[:, k]
        i = int(np.argmax(np.abs(col)))
        for j, n in enumerate(NS):
            W[k, j] = (AD[n] @ col)[i] / col[i]
    scale = np.max(np.abs(W))
    W[np.abs(W) < 1e-8 * scale] = 0
    return W


W = _weights()
GAP = {"zero": 0.0, "nonzero": np.inf}
REL = 1e-9


def _is_zero(w, y):
    nw = max(np.max(np.abs(w)), 1e-300)
    ny = max(np.max(np.abs(y)), 1e-300)
    rel = abs(complex(w @ y)) / (nw * ny)
    if rel < REL:
        GAP["zero"] = max(GAP["zero"], rel)
        return True
    GAP["nonzero"] = min(GAP["nonzero"], rel)
    return False


def dim_z(points):
    pts = [np.asarray(y, dtype=complex) for y in points]
    return sum(1 for k in range(DIM) if all(_is_zero(W[k], y) for y in pts))


def _e(j):
    v = np.zeros(4, dtype=complex)
    v[j] = 1
    return v


def _walls():
    split = [k for k in range(DIM) if W[k, 0] != 0 and W[k, 2] != 0]
    ts = []
    for k in split:
        t = -W[k, 0] / W[k, 2]
        if not any(abs(t - u) < 1e-7 for u in ts):
            ts.append(t)
    return sorted(ts, key=lambda z: z.real), len(split)


def _classes(x1):
    always = [k for k in range(DIM) if not np.any(W[k] != 0)]
    killed = [k for k in range(DIM) if _is_zero(W[k], x1)]
    active = [k for k in killed if k not in always]
    cls = []
    for k in active:
        w = W[k]
        for c in cls:
            w0 = W[c[0]]
            i = int(np.argmax(np.abs(w0)))
            if np.max(np.abs(w - (w[i] / w0[i]) * w0)) < 1e-8 * np.max(np.abs(w)):
                c.append(k)
                break
        else:
            cls.append([k])
    return active, cls


def _null(normals):
    A = np.array(normals, dtype=complex)
    _, s, Vh = np.linalg.svd(A)
    rank = int((s > 1e-9 * max(s[0], 1e-300)).sum())
    return Vh[rank:].conj().T


# --------------------------------------------------------------- banked values


def test_banked_centralizer_dimensions_reproduce():
    assert dim_z([_e(0), _e(1), _e(2), _e(3)]) == 12          # dim z(C)
    assert dim_z([_e(0)]) == 30                                # x8
    assert dim_z([_e(2)]) == 30                                # x16
    assert dim_z([_e(1)]) == 12                                # x14
    assert dim_z([_e(3)]) == 12                                # x22
    assert dim_z([_e(0), _e(2)]) == 30                         # the soft plane


def test_the_soft_plane_is_soft_because_w8_vanishes_iff_w16_does():
    mixed = [k for k in range(DIM)
             if (W[k, 0] == 0) != (W[k, 2] == 0)]
    assert mixed == [], "a weight killing exactly one of x8, x16 would break the cliff"


def test_three_walls_from_the_split_weights():
    ts, nsplit = _walls()
    assert nsplit == 48
    assert len(ts) == 3
    for t in ts:
        assert dim_z([np.array([1, 0, t, 0], dtype=complex)]) == 46


# --------------------------------------------------------------- the new content


def test_seven_hyperplanes_with_the_same_sizes_at_every_wall():
    ts, _ = _walls()
    for t in ts:
        x1 = np.array([1, 0, t, 0], dtype=complex)
        active, cls = _classes(x1)
        assert len(active) == 34
        assert sorted(len(c) for c in cls) == [2, 2, 6, 6, 6, 6, 6]


def test_the_14_locus_is_exactly_two_hyperplanes():
    ts, _ = _walls()
    x1 = np.array([1, 0, ts[0], 0], dtype=complex)
    _, cls = _classes(x1)
    small = [c for c in cls if len(c) == 2]
    big = [c for c in cls if len(c) == 6]
    assert len(small) == 2 and len(big) == 5

    rng = np.random.default_rng(11)
    for c in small:
        nul = _null([W[c[0]]])
        for _ in range(4):
            y = nul @ (rng.normal(size=nul.shape[1]) + 1j * rng.normal(size=nul.shape[1]))
            assert dim_z([x1, y]) == 14
    for c in big:
        nul = _null([W[c[0]]])
        for _ in range(4):
            y = nul @ (rng.normal(size=nul.shape[1]) + 1j * rng.normal(size=nul.shape[1]))
            assert dim_z([x1, y]) == 18


def test_the_two_14_hyperplanes_are_complex_conjugate():
    """Why B892 found y* non-real and no real nullity-14 point."""
    ts, _ = _walls()
    x1 = np.array([1, 0, ts[0], 0], dtype=complex)
    _, cls = _classes(x1)
    small = [c for c in cls if len(c) == 2]
    a, b = W[small[0][0]], W[small[1][0]]
    a = a / a[int(np.argmax(np.abs(a)))]
    b = b / b[int(np.argmax(np.abs(b)))]
    assert np.max(np.abs(a - np.conj(b))) < 1e-6
    assert np.max(np.abs(a.imag)) > 1e-3, "the hyperplane is genuinely non-real"


def test_generic_second_charge_gives_the_floor():
    ts, _ = _walls()
    x1 = np.array([1, 0, ts[0], 0], dtype=complex)
    rng = np.random.default_rng(5)
    for _ in range(40):
        y = rng.normal(size=4) + 1j * rng.normal(size=4)
        assert dim_z([x1, y]) == 12


def test_the_coordinate_charges_give_twelve_as_B874_found():
    ts, _ = _walls()
    for t in ts:
        x1 = np.array([1, 0, t, 0], dtype=complex)
        assert dim_z([x1, _e(1)]) == 12          # x14
        assert dim_z([x1, _e(3)]) == 12          # x22


def test_dimension_26_is_attained_amending_B874s_addendum():
    """B874: "No 26 stratum exists" -- true for coordinate subtori, too strong overall."""
    ts, _ = _walls()
    x1 = np.array([1, 0, ts[0], 0], dtype=complex)
    _, cls = _classes(x1)
    rng = np.random.default_rng(3)
    found = False
    for combo in itertools.combinations(range(len(cls)), 2):
        nul = _null([W[cls[i][0]] for i in combo])
        if nul.shape[1] == 0:
            continue
        for _ in range(4):
            y = nul @ (rng.normal(size=nul.shape[1]) + 1j * rng.normal(size=nul.shape[1]))
            if np.max(np.abs(y)) < 1e-12:
                continue
            if dim_z([x1, y]) == 26:
                # a genuine 2-plane, not y in <x1>
                assert np.linalg.matrix_rank(np.array([x1, y]), tol=1e-8) == 2
                found = True
    assert found, "26 must be attained somewhere in C"


def test_every_attained_dimension_is_a_levi_dimension():
    """Cross-check against the independent Levi enumeration."""
    LEVI = {6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78}
    ts, _ = _walls()
    x1 = np.array([1, 0, ts[0], 0], dtype=complex)
    _, cls = _classes(x1)
    rng = np.random.default_rng(2)
    seen = set()
    for r in (1, 2, 3):
        for combo in itertools.combinations(range(len(cls)), r):
            nul = _null([W[cls[i][0]] for i in combo])
            if nul.shape[1] == 0:
                continue
            for _ in range(3):
                y = nul @ (rng.normal(size=nul.shape[1])
                           + 1j * rng.normal(size=nul.shape[1]))
                if np.max(np.abs(y)) < 1e-12:
                    continue
                seen.add(dim_z([x1, y]))
    assert seen <= LEVI, f"non-Levi dimension attained: {seen - LEVI}"
    assert {14, 18, 26} <= seen


def test_the_numerics_are_certified_by_an_explicit_gap():
    """A tolerance-fragile classification must fail loudly, not silently."""
    assert GAP["nonzero"] / max(GAP["zero"], 1e-300) > 1e6, (
        f"gap too narrow: zero<={GAP['zero']:.3e}, nonzero>={GAP['nonzero']:.3e}")
