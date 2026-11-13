"""B1908's lock. It solves the monodromy exactly at k = 1 to 5 and checks it against the word's trace, shows that B1847's
bounded search stops at k = 3 (the cause) and agrees at k = 1, and holds the page's table and fits to the kept output of
k3_extrapolation.py, which it recomputes from runs/. It writes nothing."""
import sys, os, re, json, math, pathlib, importlib.util, pytest
HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "frontier" / "B1847_the_level_surfaces_own_modulus" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1846_the_metrics_read_out" / "verification"))
PAGE = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
snappy = pytest.importorskip("snappy")
import sympy as sp
import monodromy_exact as MX

def _member(k):
    from oa_harm import _chi_vector
    G = snappy.Manifold("b++LLLLLLR" + "LR" * k).fundamental_group(); gens, rels = G.generators(), G.relators()
    return gens, rels, _chi_vector(gens, rels)

def test_the_monodromy_is_solved_exactly_and_has_the_words_trace():
    L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
    want = {1: [[-1, -3], [8, 23]], 2: [[15, -28], [-23, 43]], 3: [[109, -71], [-66, 43]], 4: [[-21, 55], [-160, 419]], 5: [[-55, 144], [-419, 1097]]}
    for k in range(1, 6):
        _, _, sols, _ = MX.monodromy_from_relators(*_member(k))
        assert len(sols) == 1 and sols[0].tolist() == want[k], k
        assert int(sols[0][0, 0] + sols[0][1, 1]) == ((L ** 6) * R * ((L * R) ** k)).trace()
        assert ("[[%d, %d], [%d, %d]]" % tuple(x for r in want[k] for x in r)).replace(" ", "") in PAGE.replace(" ", "").replace("\u2212", "-")

def test_the_bounded_search_is_the_cause():
    import fibre_faces as FF
    _, _, old, _ = FF.monodromy_from_relators(*_member(1))
    assert [m.tolist() for m in old] == [[[-1, -3], [8, 23]]]
    _, _, old3, _ = FF.monodromy_from_relators(*_member(3))
    assert old3 == []                                    # entries beyond 40: the search finds nothing, and the mesher then stops

def test_the_table_and_the_fits_are_the_runs():
    spec = importlib.util.spec_from_file_location("k3x", HERE / "k3_extrapolation.py")
    kept = json.loads((HERE / "k3_extrapolation.json").read_text(encoding="utf-8"))
    import io, contextlib
    before = (HERE / "k3_extrapolation.json").read_bytes()
    with contextlib.redirect_stdout(io.StringIO()):
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)     # its write is under a main guard
    assert (HERE / "k3_extrapolation.json").read_bytes() == before                  # the lock wrote nothing
    assert abs(m.a2 - kept["two-point"]) < 1e-12 and abs(float(m.I0) - kept["three-point"]) < 1e-12
    flat = " ".join(PAGE.split())
    for key, col in (("levels", 1), ("levels at grid 160", 3)):
        for d, (re_, im, dE) in kept[key].items():
            label = ("%+.4f" % float(d)).replace("-", "\u2212")
            row = [l for l in PAGE.splitlines() if l.startswith("| %s |" % label)]
            assert row, d
            cells = [c.strip() for c in row[0].strip("|").split("|")]
            assert cells[col] == "%.3f" % im, (key, d, cells[col], im)
    assert "6.6940 and 6.6895" in flat and "gives 6.0291" in flat
    assert ("%.4f" % kept["two-point"], "%.4f" % kept["three-point"], "%.4f" % kept["parabola through the good levels"]) == ("6.6940", "6.6895", "6.0291")
