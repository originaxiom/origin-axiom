"""B1386 lock -- THE OPEN EISENSTEIN CUSP: L4 (the fixed-point congruence: where an order-3 isometry fixing the class rotates a cusp,
chi(d+) = #(its fixed points in d+) mod 3; where it translates, chi(d+) = 0 mod 3) on the model torus, with the Morse count reproducing
L1; the rotation filter on ocube06_08812's covers of degree 2 and 3; the member cube~3.24 (SnapPy facts from its stored signature).
Slow: the member's classes and modes through B1369's and B1370's instruments (v+ the invariant and cuspidal line, negated by nothing;
the leading shells; L4 and the index on its own invariant fields), and one closed class of the search (cube~3.28, closed by L3)."""
import importlib.util
import math
import warnings
from pathlib import Path

import numpy as np
import pytest

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1386_the_open_eisenstein_cusp" / "verification"


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, VER / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _load("b1386_the_open_cusp", "the_open_cusp.py")


def test_the_fixed_point_congruence_on_the_model_torus():
    # the Morse count reproduces L1 on the symmetric first shell (B1385 S7; its basis has b1, b2 at sixty degrees, so the rotation's
    # fixed points are 0, (1/3, 1/3), (2/3, 2/3) -- the three extrema)
    fix3 = [(0.0, 0.0), (1 / 3, 1 / 3), (2 / 3, 2 / 3)]
    for deg in (0, 45, 100, 135, 180, -60):
        phi = math.radians(deg)
        terms = [(complex(math.cos(phi), math.sin(phi)), k) for k in T.EP.SHELL3]
        chi, complete, gap, pts = T.morse_chi(terms, fix3)
        assert complete and chi == T.EP.morse_prediction(phi) and len(pts) == 6
        at_fixed = [k for x, _, k in pts if any(np.allclose((x - np.array(p) + 0.5) % 1.0 - 0.5, 0, atol=1e-6) for p in fix3)]
        assert len(at_fixed) == 3 and all(k in ("max", "min") for k in at_fixed)      # the fixed points are extrema, never saddles
    # L4 on random fields averaged over the rotation or over a translation of order 3; the grid agrees where resolved
    out = T.l4_synthetic(trials=10, n=120, seed=2, box=1)
    for key in ("rotation-averaged", "translation-averaged"):
        assert out[key].get("congruence holds", 0) >= 9 and "congruence FAILS" not in out[key]
        assert "grid DISAGREES" not in out[key]


def test_the_rotation_filter():
    S = _load("b1386_eisenstein_search", "eisenstein_search.py")
    assert S.run_filter(2) == (7, [1])
    assert S.run_filter(3) == (176, [24, 27, 28, 33, 55, 60, 80, 81, 82, 93, 102, 103, 105, 128, 139, 156, 167])


def test_the_member():
    out = T.s2_snappy()
    assert out["tetrahedra"] == 90 and out["solution"] == "all tetrahedra positively oriented"
    assert out["volume ratio error"] < 1e-50 and out["H1"] == "Z/3 + Z/3 + Z/9 + Z + Z + Z + Z + Z" and out["cusps"] == 4
    assert out["isometries"] == 6 and out["group"] == "D3" and out["amphichiral"] is False
    assert out["rotation cusps"] == [0, 3] and out["isometric to the covering path"]


@pytest.mark.slow
def test_the_open_cusp_and_its_index():
    FM, cls, cusps = T.analyse()
    s = cls["summary"]
    assert all(o == "preserving" for _, o in s["isometries (cusp permutation, orientation)"])
    assert s["dim V = dim H^1(M)^R"] == 3 and s["V inside ann(P_c)"] == {0: True, 1: False, 2: False, 3: True}
    assert s["dim H^1(M)^Isom"] == 1 and s["dim of the cuspidal line"] == 1 and s["v+ (B1369's H-basis)"] == [1, -1, -1, 0, -2]
    assert s["swap eigenvalues on V"] == [[-1, -1, 1]] * 3 and s["isometries negating v+"] == [] and s["v+ fixed by every isometry"]
    lead = {c: tuple(int(x) if i else x for i, x in enumerate(row["leading allowed shell (|k|^2 / first, vectors, directions, real dim)"]))
            for c, row in cusps.items()}
    assert lead == {0: (1.0, 6, 3, 2), 1: (3.0, 2, 1, 1), 2: (3.0, 6, 3, 3), 3: (1.0, 6, 3, 2)}
    assert [cusps[c]["R acts by"] for c in range(4)] == ["rotation", "translation", "translation", "rotation"]
    assert all(len(cusps[c]["R's fixed points"]) == 3 for c in (0, 3))
    checks, _ = T.s4_l4(cusps, trials=4, n=120)
    for c, per in checks.items():
        for label, tally in per.items():
            assert "congruence FAILS" not in tally and "grid DISAGREES" not in tally, (c, label, tally)
    vals, congruent, _ = T.s4_index(cusps, trials=20, n=120)
    assert congruent and 0 not in vals and set(vals) <= {-5, -2, -1, 1, 2, 5}


@pytest.mark.slow
def test_a_closed_class_of_the_search():
    S = _load("b1386_eisenstein_search", "eisenstein_search.py")
    r = S.analyse(S.base().covers(3)[28], "cube~3.28")
    assert r["cusps"] == 4 and r["b1"] == 6 and r["isometries"] == 6 and r["triangulation"] == "own"
    assert r["rot"] == [(0, 2, False, True, False), (3, 2, False, True, False)]      # locally open, negated globally (L3)
