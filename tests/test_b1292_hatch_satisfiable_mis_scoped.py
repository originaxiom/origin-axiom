"""B1292 — B1291's hatch is satisfiable (m202) and mis-scoped (flatness, not parity)."""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1292_the_hatch_is_satisfiable_and_mis_scoped"
V_TET = 1.0149416064096536


def _snappy():
    import warnings; warnings.filterwarnings("ignore")
    return __import__("snappy")


def test_the_arc_reproduces_by_RUNNING_its_script():
    r = subprocess.run([sys.executable, str(ARC / "verification" / "m202.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-2000:]
    assert r.stdout.rstrip().endswith("SELFTEST: PASS")


def test_m202_meets_every_clause_of_the_hatch():
    s = _snappy()
    M = s.Manifold("m202")
    assert M.num_cusps() == 2
    v = float(M.volume())
    assert abs(v / V_TET - 4) < 1e-7                      # tiled by 4 regular ideal tetrahedra
    assert abs(v / float(s.Manifold("m004").volume()) - 2) < 1e-9
    hexa = complex(0.5, 3 ** 0.5 / 2)
    for i in range(2):
        assert abs(complex(M.cusp_info(i)["shape"]) - hexa) < 1e-9    # hexagonal => Z/6 available
    G = M.symmetry_group()
    assert G.order() == 12                                 # D6
    def dAI(A):
        a, b, c, d = int(A[0,0]), int(A[0,1]), int(A[1,0]), int(A[1,1])
        return abs((a-1)*(d-1) - b*c)
    both3 = [iso for iso in G.isometries() if all(dAI(A) == 3 for A in iso.cusp_maps())]
    assert len(both3) == 4                                 # |Fix| = 3 on BOTH cusps


def test_m004s_cusp_is_RECTANGULAR_which_is_why_order_3_is_impossible_there():
    M = _snappy().Manifold("m004")
    assert abs(complex(M.cusp_info(0)["shape"]).real) < 1e-9


def test_the_2T_count_and_its_METHOD_CONTROL():
    """m202 keeps 2T (96) — and the counter is validated against m004's BANKED 48 in the same run."""
    sys.path.insert(0, str(ARC / "verification"))
    try:
        import m202 as mod
    finally:
        sys.path.pop(0)
    s = _snappy()
    assert mod.surjections_onto_2T(s.Manifold("m004"))[1] == 48, "method control failed"
    assert mod.surjections_onto_2T(s.Manifold("m202"))[1] == 96


def test_the_MIS_SCOPING_is_the_deliverable_and_is_exhibited_at_three_cusp_counts():
    """chi(M) = 0 at ANY cusp count — so going multi-cusped cannot help net chirality."""
    s = _snappy()
    for nm, nc in (("m004", 1), ("m202", 2), ("o10_150704", 4)):
        M = s.Manifold(nm); G = M.fundamental_group()
        assert M.num_cusps() == nc
        assert 1 - len(G.generators()) + len(G.relators()) == 0, nm


def test_B1291_is_re_scoped_AT_SOURCE_not_only_in_the_log():
    """E53: the correction must reach the artifact. Both the kill-graph hatch and the FINDINGS."""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    e = next(x for x in kg if x["id"] == "B1291")
    assert "RE-SCOPED AT B1292" in e["hatch"] and "WRONG OBSTRUCTION" in e["hatch"]
    f = (ROOT / "frontier" / "B1291_the_parity_of_the_cusp" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "RE-SCOPED AT B1292" in f and "Do not read it as one" in f
    # and B1291's own verdict must NOT have been flipped — the theorem stands
    v = json.loads((ROOT / "frontier" / "B1291_the_parity_of_the_cusp" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "NEGATIVE" and v["creates_law"] is True


def test_no_generation_claim_is_made():
    """The disclaimer must survive markdown emphasis, so strip it before matching."""
    import re
    raw = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    plain = re.sub(r"[*_`]", "", raw).lower()
    assert "not a generation count" in plain, "the arc must disclaim the generation reading"
    assert "i-26 is untouched" in plain and "unearned" in plain
    # and it must NOT claim m202 is the object
    assert "nothing here claims m202 is the object" in plain or "not a result" in plain
