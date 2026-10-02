"""B1449 lock -- the fourteen silent receipts, read.

Live: the decisive test of B469 with its one-line fix reproduces the arc's statement (and the tracked script still
raises, which is why the receipt on disk is a crash).  Recorded: the fourteen classifications, and that every
correction they call for is in place.
"""
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1449_the_silent_receipts_read"
V = ARC / "verification"


def test_the_fourteen_are_classified_and_the_sweep_agrees_on_the_list():
    d = json.load(open(V / "receipts_read.json"))
    assert d["read"] == 14 and len(d["receipts"]) == 14
    assert d["counts"] == {"ACKNOWLEDGED": 4, "ACKNOWLEDGED IN SUBSTANCE": 1, "FALSE POSITIVE": 3, "INCIDENTAL": 4, "LOAD-BEARING": 1, "STALE RECEIPT, CLAIM REPRODUCED": 1}
    sweep = json.load(open(ROOT / d["source"]))
    listed = set(sweep["silent"]) - {"frontier/B1411_the_sm_seats_v10_arcs_harvested/verification/main_b1355_geometry_run.txt"}
    assert listed == {r["receipt"] for r in d["receipts"]}, "the fourteen are the sweep's fifteen less the one repaired at B1425"
    assert all((ROOT / r["receipt"]).is_file() for r in d["receipts"])


def test_the_false_positives_are_what_the_record_says():
    for cell in ("W3-084", "W4-084r"):
        t = (ROOT / "frontier/B771_phase1_wave1/cells" / cell / "output.txt").read_text()
        assert "FAILED GATES: []" in t and "Traceback" not in t
    assert (ROOT / "frontier/B771_phase1_wave1/cells/W3-149r/output.txt").read_text().rstrip().endswith("ALL CHECKS PASS")


def test_every_correction_is_in_place():
    for p in ("frontier/B498_mixed_monoid_dynamics/FINDINGS.md", "frontier/B469_breath_campaign/FINDINGS.md", "frontier/B477_sterile_classes/FINDINGS.md",
              "frontier/B485_metallic_apoly_family/FINDINGS.md", "frontier/B764_c19_comparator/FINDINGS.md", "frontier/B670_anatomy_full/packet/loop2/b2_massey/FINDINGS_CC2.md"):
        assert "**Receipt note (2026-10-02, B1449).**" in (ROOT / p).read_text(), p
    add = (ROOT / "frontier/B530_natural_history/ADDENDUM_2026-10-02_the_gap_slope_ratio_is_not_1_204.md").read_text()
    assert "W4-270r" in add and "fit-protocol dependent" in add and "withdrawn" in add
    w2 = (ROOT / "frontier/B771_phase1_wave1/cells/W2-270/output.txt").read_text()
    assert "FAIL  got 1.257492 vs banked 1.204" in w2, "the receipt that contradicts the banked ratio"
    w4 = json.load(open(ROOT / "frontier/B771_phase1_wave1/wave4_results.json")); cells = w4 if isinstance(w4, list) else list(w4.get("cells", w4).values() if isinstance(w4.get("cells", w4), dict) else w4.get("cells", w4))
    c = next(x for x in cells if isinstance(x, dict) and x.get("id") == "W4-270r")
    assert c["verdict"] == "RESOLVED-B" and "fit-protocol dependent" in c["headline"]


def test_the_decisive_test_of_b469_reproduces_with_the_fix_live():
    pytest.importorskip("snappy")
    out = subprocess.run([sys.executable, str(V / "octic_test_fixed.py")], capture_output=True, text=True, timeout=600)
    lines = {l.split(" = ")[0]: l for l in out.stdout.splitlines() if " = " in l}
    assert "kappa(a,c) = -2.00000000+0.00000000j" in lines["kappa(a,c)"]
    for w in ("tr(ac)", "tr(aC)"):
        assert float(lines[w].split("|octic| = ")[1].split()[0]) < 1e-10, lines[w]
    assert float(lines["tr(a)"].split("|octic| = ")[1].split()[0]) > 1
    # the bite: the script as tracked still raises -- that is why the only receipt on disk is a crash
    bad = subprocess.run([sys.executable, "octic_test.py"], capture_output=True, text=True, timeout=600, cwd=str(ROOT / "frontier/B469_breath_campaign"))
    assert bad.returncode != 0 and "TypeError" in bad.stderr
