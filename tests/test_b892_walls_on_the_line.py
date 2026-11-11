"""B892 lock -- every wall on the line of the second measurement, from the joint eigenvalues (the audit's finding E5).

The arc's real-line scan never refined, and its findings read it as excluding a real nullity-14 point.  The exclusion now
rests on the joint diagonalisation of four commuting elements.

What could fail: a check of the committed run; a wall value with a real part; the pattern of seven classes changing; the old
scan's sentence standing with no correction beside it; and, in the slow lane, the whole computation run again."""
import importlib.util
import json
import os
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B892_second_measurement" / "verification"
RES = json.loads((V / "walls_on_the_line.json").read_text(encoding="utf-8"))
N = RES["numbers"]


def test_every_check_of_the_committed_run_holds():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 5 and all(checks.values())
    assert "CHECKS: 5, FAILING: 0" in (V / "walls_on_the_line_run.txt").read_text(encoding="utf-8")
    assert N["commutator"] < 1e-12 and N["residual"] < 1e-10 and N["cond_eigvec"] < 1e3


def test_the_walls_are_four_purely_imaginary_points_and_the_counts_add_up():
    assert (N["z_s1"], N["generic"], N["plane"]) == (46, 12, 30)
    walls = sorted(N["walls"])
    assert [(m, n) for _, m, n in walls] == [(2, 14), (6, 18), (6, 18), (2, 14)]              # ordered by t: -0.0515, -0.0464, +0.0464, +0.0515
    assert abs(walls[0][0] + walls[3][0]) < 1e-12 and abs(walls[1][0] + walls[2][0]) < 1e-12   # two conjugate pairs
    assert abs(walls[3][0] - 0.0515261607) < 1e-9 and abs(walls[2][0] - 0.0464130116) < 1e-9
    assert N["largest_real_part_over_modulus"] < 1e-12
    # every weight of z(s1) is accounted for: 12 that vanish on both, 18 more that vanish on x16, and the 16 at the four walls
    assert N["generic"] + (N["plane"] - N["generic"]) + sum(m for _, m, _ in walls) == N["z_s1"]
    assert N["classes"] == [2, 2, 6, 6, 6, 6, 6] and N["real_classes"] == [6, 6, 6] and sum(N["classes"]) == 34


def test_the_scans_sentence_carries_its_correction():
    f = (ROOT / "frontier" / "B892_second_measurement" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "120-point + golden-section" in f                                    # the sentence as written is kept
    for s in ("CORRECTED 2026-11-11 (the audit's finding E5", "the refinement never ran", "walls_on_the_line.py", "all purely imaginary", "a scan is the wrong instrument"):
        assert s in f, s
    src = (ROOT / "frontier" / "B892_second_measurement" / "wall_search.py").read_text(encoding="utf-8")
    assert "if not found:" in src and "golden-section refine" in src            # the fault is in the script as it was run, unchanged
    v = json.loads((ROOT / "frontier" / "B892_second_measurement" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert "CORRECTED 2026-11-11 (the audit's finding E5)" in v["claim_one_line"] and "120-point real-line scan" in v["claim_one_line"]
    b874 = (ROOT / "frontier" / "B874_measurement_ladder" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Dated note 2026-11-11 (the audit's finding E5" in b874 and "now has a reason rather than a scan" in b874
    # the old run itself: its grid found only the plane stratum
    wall = json.loads((ROOT / "frontier" / "B892_second_measurement" / "wall_results.json").read_text(encoding="utf-8"))
    assert wall["wall_points"] == [[1.5707963267948966, 30]]


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1: rebuilds E6's structure constants and diagonalises again (over a minute)")
def test_the_joint_weights_recomputed():
    spec = importlib.util.spec_from_file_location("walls_on_the_line_lock", V / "walls_on_the_line.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    DIM, X, Bal, W, info = m.joint_weights()
    assert DIM == 78 and info["commutator"] < 1e-12 and info["residual"] < 1e-10
    sc = {k: abs(v).max() for k, v in W.items()}
    Z = [i for i in range(DIM) if abs(W["s1"][i]) < 1e-7 * sc["s1"]]
    plane = [i for i in Z if abs(W["x16"][i]) < 1e-7 * sc["x16"]]
    ts = [(-W["x14"][i] / W["x16"][i]) for i in Z if i not in plane]
    assert len(Z) == 46 and len(plane) == 30 and len(ts) == 16 and max(abs(t.real) / abs(t) for t in ts) < 1e-9
    assert m.nullity_direct(Bal, 0.3, DIM)[0] == 12 and m.nullity_direct(Bal, 1j * max(t.imag for t in ts), DIM)[0] == 14
