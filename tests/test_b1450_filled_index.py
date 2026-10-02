"""B1450 lock -- the filled index on the grid.

Live: the formula on three published slopes of the figure-eight complement, with one published coefficient changed,
which fails; the strict angle structure of the twelve census triangulations.  Recorded: the sealed run on the 87
slopes, the reader's answers, and the hashes of the sealed files.
"""
import hashlib
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1450_the_filled_index_on_the_grid"
V = ARC / "verification"
sys.path.insert(0, str(V))

ARITH = {(5, 1), (-5, 1), (6, 1), (-6, 1), (8, 1), (-8, 1)}


def series(*c):
    return {2 * i: v for i, v in enumerate(c) if v}


def test_three_published_slopes_live_and_a_changed_coefficient_fails():
    from filled_index import filled
    pub = {(9, 1): series(1, 0, -1, 0, 0, 2, 2, 4, 1, -1, -6), (1, 3): series(1, -2, -3, 1, 6, 13, 16, 17, 4, -20, -55),
           (7, 1): series(1, 0, -1, 0, 1, 3, 3, 6, 4, 2, -4)}
    for sl, want in pub.items():
        got, info = filled(sl[0], sl[1], 20)
        assert got == want, sl
    wrong = dict(pub[(1, 3)]); wrong[20] = -54                      # the (1,4) entry: differs only at q^10
    assert filled(1, 3, 20)[0] != wrong


def test_the_klein_bottle_slope_is_undefined_live():
    from filled_index import filled
    got, info = filled(4, 1, 12)
    assert got is None and info.get("divergent")


def grid():
    rows = json.load(open(V / "grid_index.json"))["rows"]
    return {tuple(r["slope"]): (None if r["series"] is None else {int(k): v for k, v in r["series"].items()}) for r in rows}


def test_the_sealed_run_recorded():
    S = grid()
    assert len(S) == 87 and {s for s, d in S.items() if d is None} == {(4, 1), (-4, 1)}
    exc = {(0, 1), (1, 1), (-1, 1), (2, 1), (-2, 1), (3, 1), (-3, 1), (4, 1), (-4, 1)}
    assert all(S[s] == {0: 1} for s in exc if S[s] is not None)
    hyp = [s for s in S if s not in exc]
    assert len(hyp) == 78 and all(S[s][0] == 1 and min(S[s]) == 0 and len(S[s]) > 1 for s in hyp)
    assert all(S[(p, q)] == S[(-p, q)] for (p, q) in S if p > 0)
    cen = [json.loads(l) for l in open(ROOT / "frontier" / "B1419_the_arithmetic_fillings_corrected" / "verification" / "arithmetic_census_closed.jsonl")]
    assert {tuple(r["slope"]) for r in cen if r.get("arithmetic") is True} == ARITH


def test_the_index_does_not_see_arithmeticity():
    S = grid()
    lead = lambda d: (min(k for k in d if k > 0), d[min(k for k in d if k > 0)])
    assert lead(S[(8, 1)]) == lead(S[(7, 1)]) == (4, -1), "an arithmetic and a non-arithmetic slope begin alike"
    assert S[(8, 1)] != S[(7, 1)]
    pos = [s for s in S if s[0] > 0 and S[s] is not None and len(S[s]) > 1]
    assert len(pos) == 39 and len({tuple(sorted(S[s].items())) for s in pos}) == 26
    for a in ARITH:
        assert [s for s in pos if S[s] == S[a] and s != (abs(a[0]), a[1])] == []
    text = open(V / "grid_read.txt").read()
    assert "features that separate: 0 of 6" in text and "78 of 78" in text and "43 of 43" in text


def test_the_census_triangulations_carry_a_strict_angle_structure_live():
    snappy = pytest.importorskip("snappy")
    for n in ["m003", "m004", "m006", "m007", "m009", "m015", "m016", "m017", "m019", "m022", "m023", "m026"]:
        M = snappy.Manifold(n)
        assert M.solution_type() == "all tetrahedra positively oriented"
        assert min(complex(z).imag for z in M.tetrahedra_shapes("rect")) > 0.3, n
    assert snappy.Manifold("m004(4,1)").solution_type() != "all tetrahedra positively oriented", "the check can fail"


def test_the_sealed_files_are_the_sealed_files():
    for line in open(ARC / "ARTIFACT_HASHES.txt"):
        if line.startswith("#") or not line.strip(): continue
        h, name = line.split(None, 1); name = name.strip()
        assert hashlib.sha256(open(ARC / name, "rb").read()).hexdigest() == h, name
