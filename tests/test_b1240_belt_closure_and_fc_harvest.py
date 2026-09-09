"""B1240 -- THE BELT CLOSURE + the fc R42-R50 harvest.  Locks assert facts with what decides them.

Two kinds of lock here: (1) records of the harvest's recomputations (R42 class numbers by two routes,
R43 volume digits, R44 the E7 Perron vector, R50 the V4 table, B955 surjections, B511 D3.3 on the trace
map) -- pinned to the JSON the verification scripts regenerate; (2) THE BELT RATCHET -- the instrument
`scripts/checks/reproduce_belt.py` is RUN (subprocess), and the number of string-only REPRODUCES locks may
not grow past 27 nor may any runner reference a file main does not track.  The live counterpart, which
executes the runners, is tests/test_reproduce_runners_live.py."""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1240_belt_closure_and_fc_harvest"
V = ARC / "verification"
BELT = ROOT / "scripts" / "checks" / "reproduce_belt.py"


def _j(name):
    return json.loads((V / name).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- the arc's own record
def test_arc_verdict_fields():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1240" and v["verdict"] == "OPEN"          # record/harvest class, as B1167/B1171/B1213
    assert v["identifications"] == [] and v["creates_law"] is False
    assert {"date", "arc", "was", "decision", "class", "basis"} <= set(v["creates_law_reviewed"])
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "## THE PRIZE FIRST" in f and "E57" in f and "27" in f


# ---------------------------------------------------------------- R42: class numbers of the metallic orders
def test_r42_own_reduction_matches_pari_and_m12_splits_sl_vs_gl():
    r = _j("fast_checks.json")["R42"]
    own, pari = r["own"], r["pari_proper"]
    for m in range(1, 12):                      # every m <= 11: our SL2(Z) count == PARI's proper class number
        assert own[str(m)]["SL"] == pari[str(m)], m
    assert own["12"] == {"D": 148, "SL": 3, "GL": 2} and pari["12"] == 3
    # the discriminating fact: 6+sqrt(37) has norm -1, so h+ = h = 3 for the conductor-2 order; GL2(Z) folds
    # the two non-ambiguous classes -> 2.  A route that counted imprimitive forms reported 4/3 (self-caught).
    assert own["6"]["SL"] == own["9"]["SL"] == own["10"]["SL"] == 2 and own["11"]["SL"] == 1


def test_r42_pari_rho_cycles_independent_route():
    r = _j("r42_pari_cycles.json")
    for m, row in r.items():
        assert row["SL_cycles"] == row["pari_qfbclassno"], m
        assert row["left_set"] is False, m
    assert r["12"]["n_reduced"] == 14 and r["12"]["SL_cycles"] == 3 and r["12"]["GL"] == 2


# ---------------------------------------------------------------- R43 / R44 / B955 / R50
def test_r43_vol41_digits_and_b980_slip():
    v = _j("fast_checks.json")["R43_vol41_35dps"]
    assert v.startswith("2.02988321281930725004240510854904")
    assert "0424051081" not in v                # B980 FINDINGS.md:81 printed ...0424051081... -- a digit slip


def test_r44_b549_seven_numbers_are_e7_adjacency_perron_vector():
    r = _j("fast_checks.json")["R44"]
    assert r["match"] is True and len(r["b549"]) == 7
    assert r["perron_vector_sorted"][0] == 1.0 and abs(r["perron_vector_sorted"][-1] - 3.701666) < 2e-6


def test_b955_surjections_all_true():
    assert _j("fast_checks.json")["B955"] == {"A4": True, "D5": True, "S5": True}


def test_r50_b775_v4_table_eight_rows():
    r = _j("fast_checks.json")["R50"]
    assert len(r) == 8
    amph = {k for k, v in r.items() if v["amphicheiral"]}
    assert amph == {"m004", "m003", "m025", "b++RRLL"}
    assert r["m004"]["sym_order"] == 8 and r["m025"]["sym_order"] == 6 and r["m009"]["sym_order"] == 4


# ---------------------------------------------------------------- B511 D3.3 on the trace map (200-bit)
def test_b511_d3_prec200_no_escapes_and_double_precision_artifact():
    r = _j("b511_d3_tracemap.json")["runs"]
    prec = {k: v for k, v in r.items() if k.startswith("prec200")}
    dbl = {k: v for k, v in r.items() if k.startswith("double")}
    assert len(prec) == 8 and len(dbl) == 8
    for k, v in prec.items():
        assert v["escaped"] == 0, k
        if "control" in k:
            assert v["classical"] < 0.05 and v["wild"] > 0.7, k         # two-sided: the detector must bite
        else:
            assert v["classical"] >= 0.85 and v["wild"] < 0.1, k
    for k, v in dbl.items():
        if "control" not in k:
            assert v["escaped"] >= 100, k                                 # the banked "2.0,2.0,2.0" was this collapse
            assert v["classical"] < 0.7, k


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 re-runs the 200-bit trace map (~6 min)")
def test_b511_d3_rerun_reproduces():
    res = subprocess.run([sys.executable, str(V / "b511_d3_tracemap.py")], capture_output=True, text=True, timeout=1800)
    assert res.returncode == 0 and "REPRODUCES" in res.stdout, res.stdout[-800:] + res.stderr[-800:]


# ---------------------------------------------------------------- THE BELT RATCHET (runs the instrument)
def _belt(*args):
    res = subprocess.run([sys.executable, str(BELT), *args], capture_output=True, text=True, timeout=120,
                         env={**os.environ, "OA_ROOT": str(ROOT)})
    assert res.returncode == 0, res.stdout[-800:] + res.stderr[-800:]
    return res


def test_belt_instrument_selftest():
    assert "9/9 controls pass" in _belt("--selftest").stdout


def test_belt_ratchet_string_locks_do_not_grow(tmp_path):
    out = tmp_path / "belt.json"
    _belt("--json", str(out))
    j = json.loads(out.read_text())
    assert len(j["string_locks"]) <= 27, sorted(j["string_locks"])
    flagged = [r for r in j["runners"] if r["missing"]]
    assert flagged == [], flagged                                      # every runner's references are tracked
    inert = {r["runner"].split("/")[1] for r in j["inert"]}
    assert "B1175_charter_close_harvest" in inert                     # the honest RECORD-only runner


def test_belt_before_record_names_the_five():
    t = (V / "reproduce_belt_before_output.txt").read_text(encoding="utf-8")
    for arc in ("B1147_clane_harvest", "B1148_carrier_harvest", "B1149_meridian_longitude_harvest",
                "B1150_yukawa_clock_and_family", "B1153_peripheral_and_superposition"):
        assert arc in t, arc


def test_closure_run_full_record_is_25_of_25():
    """The record of the five runners with the closure vendored: parse banners and verdicts, never substring-count
    (the B1148 runner prints `rc=0 REPRODUCES` with ONE space; the others two)."""
    import re
    t = (V / "closure_run_full.txt").read_text(encoding="utf-8")
    banners = [b for b in re.findall(r"^===== (\S+) =====$", t, re.M) if b not in ("DONE", "REPRODUCE_DONE")]
    verdicts = re.findall(r"^\s*(?:VERDICT: )?rc=(\d+)\s+REPRODUCES", t, re.M)
    runner_rcs = re.findall(r"^########## rc=(\d+) secs=\d+$", t, re.M)
    assert len(banners) == 25 and len(set(banners)) == 25, banners
    assert len(verdicts) == 25 and set(verdicts) == {"0"}, (len(verdicts), set(verdicts))
    assert runner_rcs == ["0"] * 5, runner_rcs
    assert re.search(r"\bDIFF\s*$", t, re.M) is None and "(no committed output)" not in t
    assert re.search(r"/(?:Users|home)/", t) is None            # no machine paths in the record
    for arc, n in (("B1147", 11), ("B1148", 7), ("B1149", 3), ("B1150", 2), ("B1153", 2)):
        seg = t.split(f"########## {arc}_")[1].split("########## rc=")[0]
        assert seg.count("REPRODUCES") == n, (arc, seg.count("REPRODUCES"))


# ---------------------------------------------------------------- the vendored closure is what it says it is
@pytest.mark.parametrize("arc", ["B1147_clane_harvest", "B1148_carrier_harvest", "B1149_meridian_longitude_harvest",
                                 "B1150_yukawa_clock_and_family", "B1153_peripheral_and_superposition"])
def test_vendored_from_sha256_matches_files(arc):
    vdir = ROOT / "frontier" / arc / "verification"
    rows = [l.split() for l in (vdir / "VENDORED_FROM.txt").read_text(encoding="utf-8").splitlines()
            if l and not l.startswith(("VENDORED_FROM", "Source", "Why", "certificates by", "transitive", "record it",
                                       "Integrity", "GENERATED", "on the main", "path"))]
    rows = [r for r in rows if len(r) >= 2 and len(r[1]) == 64]
    assert len(rows) >= 6, arc
    for rel, h, *_ in rows:
        p = vdir / rel
        assert p.is_file(), f"{arc}: {rel} missing"
        assert hashlib.sha256(p.read_bytes()).hexdigest() == h, f"{arc}: {rel} differs from VENDORED_FROM"
    assert (ROOT / "frontier" / arc / "ADDENDUM_2026-09-02_B1240.md").is_file()
