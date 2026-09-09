"""B1239 — the 1/4 class is cusp-local (codex R040 reproduced, re-graded, two theorems, the residue located).

These locks pin FACTS with what decides them (E53 rule), not strings: the census counts are read from the vendored
JSON and the two theorems' bite controls are re-asserted live on the cheap witnesses.  The E52 #7 blind spot is
PINNED so nobody reaches for the orientation-blind detector again.
"""
import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B1239_quarter_class_is_cusp_local"
V = CELL / "verification"
TOL = 1e-6


def _cls(cs):
    x = float(cs) % 0.5
    return "zero" if min(x, 0.5 - x) < TOL else "quarter" if abs(x - 0.25) < TOL else "other"


def test_codex_census_reproduced_at_quad_double():
    s = json.load(open(V / "r040_census_rerun.json"))["summary"]
    assert s["census_size"] == 1260
    assert s["counts_quad"] == {"zero": 1260, "quarter": 0, "other": 0, "fail": 0}
    assert s["max_dist_quad_in_class"] < 1e-60          # codex's 1e-6 is nine orders loose; ours is 58 orders tighter
    assert s["vol_ratio_all_2"] and s["all_covers_orientable"]


def test_closed_control_codex_did_not_run():
    d = json.load(open(V / "r040_closed_control.json"))
    assert d["counts"] == {"zero": 17}
    rows = d["rows"]
    # Kawauchi's CONCLUSION, computed: Tor H1 a square and tau even on every closed case
    for r in rows:
        tor = [int(m) for m in re.findall(r"Z/(\d+)", r["H1_cover"])]
        assert all(tor.count(t) % 2 == 0 for t in set(tor)), r
        assert sum(1 for t in tor if t % 2 == 0) % 2 == 0, r


def test_closed_amphichiral_never_quarter_but_the_census_has_quarter_class():
    """Statement 1 (APS + eta odd; no Kawauchi, no freeness) on the ENTIRE closed census, with its bite."""
    d = json.load(open(V / "r040_quarter_is_a_cusp_phenomenon.json"))
    c = d["closed"]
    assert c["n"] == 11031 and c["undecided"] == 0 and c["cs_fail"] == 0
    assert c["table"]["amphichiral"] == {"zero": 37, "quarter": 0, "other": 0}
    assert c["table"]["chiral"]["quarter"] >= 17                      # the class exists in the closed census
    assert d["cusped"]["table"]["amphichiral"]["quarter"] >= 11       # ... and cusped amphichiral manifolds reach it
    assert d["verdict"]["prediction_holds"] and d["verdict"]["detector_bites"]


def test_swap_corollary_bucket_A_is_zero_and_bucket_B_is_where_it_could_have_failed():
    d = json.load(open(V / "r040_swap_corollary.json"))
    assert d["N_scanned"] == 61911 and d["undecided"] == 0
    b = d["buckets"]
    assert b["A"] == {"zero": 28, "quarter": 0, "other": 0}
    assert b["B"]["quarter"] >= 5 and b["B"]["zero"] >= 6            # amphichiral with a tau-invariant cusp: both classes occur
    assert float(str(d["max_dist_A"]).replace(" ", "")) < 1e-12   # pari-style "4.72 E-16" carries a space


def test_live_witnesses_and_the_pinned_blind_spot():
    snappy = pytest.importorskip("snappy")
    # bucket A witness (reversing isometry swaps the two cusps) -> zero; bucket B witness -> quarter
    assert _cls(snappy.Manifold("m203").chern_simons()) == "zero"
    assert _cls(snappy.Manifold("t12054").chern_simons()) == "quarter"
    m = snappy.Manifold("m203")
    isos = m.is_isometric_to(m, return_isometries=True)
    rev = [i for i in isos if round(i.cusp_maps()[0].det()) == -1]
    assert any(all(i.cusp_images()[j] != j for j in range(2)) for i in rev), "m203 must have a cusp-swapping reversing isometry"
    # the E52 #7 blind spot, PINNED: is_isometric_to(M, mirror) is orientation-blind (5_2 is chiral)
    k = snappy.Manifold("5_2"); km = k.copy(); km.reverse_orientation()
    assert k.is_isometric_to(km) is True                    # the trap (B1181's instrument)
    assert k.symmetry_group().is_amphicheiral() is False    # the detector (B1235's)
    assert snappy.Manifold("4_1").symmetry_group().is_amphicheiral() is True
    # m004's own case: the residue -- its single cusp is tau-invariant (Gieseking quotient has a Klein bottle cusp)
    assert snappy.Manifold("m000").cusp_info()[0]["topology"] == "Klein bottle cusp"
    assert not snappy.Manifold("m000").is_orientable()


def test_the_fences_are_written_and_l194_stays_open():
    f = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "cited, not read" in f or "cited-not-read" in f
    assert "Meyerhoff" in f and "Kawauchi" in f
    assert "L194 is therefore refined, not closed" in f
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    m = re.search(r"^## L194 .*?(?=^## L195)", leads, re.S | re.M)
    assert m and "cusp-local" in m.group(0) and "B1239" in m.group(0)
    assert "CLOSED" not in m.group(0).split("\n")[0]
    v = json.loads((CELL / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["creates_law"] is False and v["identifications"] == []
    assert (ROOT / "frontier" / "B1234_a6_built_the_walls" / "ADDENDUM_2026-09-02_B1239.md").exists()
