"""B1518 -- THE BAR: the lock.

Locks the seal (every sealed file unchanged since `697217be`), the instrument's and the run's planted controls, the sealed run's
record and its predictions, the independent route's witness pair (m369 against o9_00001, recomputed live), the design facts,
the standing text `docs/THE_BAR.md`, and the numbers FINDINGS quotes against the records they come from. The full re-run of
the sealed analysis is slow.
"""
import hashlib
import importlib.util
import json
import math
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1518_the_bar"
VER = ARC / "verification"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _norm(p):
    return " ".join(re.sub(r"[*`>]", "", p.read_text(encoding="utf-8")).split())


def _json(name):
    return json.loads((VER / name).read_text(encoding="utf-8"))


NM = _load("null_model_b1518", VER / "null_model.py")
BR = _load("bar_run_b1518", VER / "bar_run.py")
PR = _load("post_run_checks_b1518", VER / "post_run_checks.py")


# ------------------------------------------------------------------------------------------------- the seal
def test_sealed_files_unchanged_since_the_seal():
    lines = [l for l in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines() if l and l[0] != "#"]
    assert len(lines) == 11
    for line in lines:
        digest, rel = line.split("  ", 1)
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == digest, rel


def test_seal_markers_and_ledger():
    pre = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in pre and "PRIOR ART:" in pre
    sha = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    assert sha in ledger and "B1518 THE BAR" in ledger


# ------------------------------------------------------------------------------------------------- controls
def test_instrument_planted_controls():
    checks = NM.selftest()
    assert len(checks) == 10 and all(checks.values()), checks


def test_dry_run_planted_controls():
    d = BR.dry_run()
    assert len(d["checks"]) == 8 and d["passed"], d["checks"]


def test_sidak_and_interval_by_hand():
    assert abs(NM.sidak(0.0108494575, 2) - 0.0215812) < 1e-6
    lo, hi = NM.clopper_pearson(87, 536)
    assert 0.132 < lo < 0.1322 and 0.1962 < hi < 0.1964


# ------------------------------------------------------------------------------------------------- the sealed run
def test_run_record_controls_and_predictions():
    r = _json("bar_run.json")
    assert all(v for v in r["controls"].values() if isinstance(v, bool)) and "stopped" not in r
    assert r["controls"]["C1 hit count (main B1439: 95)"] == 95
    p = r["predictions"]
    keys = list(p)
    assert [p[k] for k in keys[:4]] == [True, True, True, False]
    assert p["corrected p-values (T2, T3)"][0] < 0.01 <= p["corrected p-values (T2, T3)"][1]


def test_run_record_numbers():
    r = _json("bar_run.json")
    R, T, D = r["readings"], r["tests"], r["decided"]
    assert (R["R1 base rate, word states"]["hits"], R["R1 base rate, word states"]["units"]) == (95, 758)
    assert (R["R1 base rate, manifolds"]["hits"], R["R1 base rate, manifolds"]["units"]) == (87, 536)
    assert R["R1 split own-level manifolds (B1517 C5 found none)"] == []
    assert R["R3 level-manifolds by k (hits, units)"] == {"1": [87, 536], "2": [50, 79], "3": [25, 32], "4": [5, 5],
                                                          "5": [3, 4], "6": [1, 1], "7": [2, 2]}
    assert [T[f"T1 determinism under S{i}"]["mixed_strata"] for i in (1, 2, 3)] == [21, 22, 15]
    assert T["T2 leave-one-out AUC under S1"] == 0.8583
    assert T["T3 reversal-closed, unconditional (hits, units)"] == {"closed": [79, 314], "paired": [8, 222]}
    assert T["T3 reversal-closed given S2: conditional permutation"]["observed"] == 79
    assert D["D1 holds"] and D["D2 the root's own level is silent (main B1434 (a): torsion 1, no character)"]
    tower = D["D3 the root's tower against the other level-manifolds at the same k"]
    assert tower["2"]["root_hit"] is False and tower["2"]["others_hit"] == 50
    assert [tower[str(k)]["root_backgrounds"] for k in range(3, 8)] == [48, 256, 400, 2160, 3136]


@pytest.mark.slow
def test_sealed_run_reproduces():
    fresh = json.loads(json.dumps(BR.run(), default=str))
    assert fresh == _json("bar_run.json")


# ------------------------------------------------------------------------------------------------- the independent route
def test_independent_route_banked_identities_and_witness_live():
    counts = {s: PR.own_level_census(s)["generation_backgrounds"] for s in ("+LR", "-LLRLR", "-LLLRLR", "-LLLLLLLLR")}
    assert counts == {"+LR": 0, "-LLRLR": 8, "-LLLRLR": 16, "-LLLLLLLLR": 0}
    rows = {r["state"]: r for r in _json("covariates.json")["rows"]}
    a, b = rows["-LLRLR"], rows["-LLLLLLLLR"]
    for key in ("d1", "d2", "sign", "trace", "reversal_closed", "symmetry_order", "amphichiral"):
        assert a[key] == b[key], key
    assert (a["d1"], a["d2"]) == (1, 12) and a["trace"] == -10


def test_independent_route_record():
    q = _json("post_run_checks.json")
    assert q["Q2 banked identities pass"] and q["Q2 the own route agrees with main on every one"]
    rows = q["Q2 every manifold of the mixed strata: [stratum, state, main, own route, agree]"]
    assert len(rows) == 52 and q["Q1 mixed (d1, d2, sign) strata"] == 22 and all(r[4] for r in rows)
    assert q["Q3 the witness pair, identified"]["-LLRLR"]["identify"] == ["m369(0,0)"]
    assert q["Q3 the witness pair, identified"]["-LLLLLLLLR"]["identify"] == ["o9_00001(0,0)"]
    assert q["Q4 inside the strata holding both reversal classes (hits, manifolds)"] == {"closed": [6, 36],
                                                                                        "paired": [0, 34]}


# ------------------------------------------------------------------------------------------------- design facts
def test_design_facts():
    f = _json("design_checks.json")
    assert f["F1 odd length: states, of which torsion even"] == [268, 268]
    assert f["F1 even length: torsion even exactly when A = I mod 2"] and f["F2 (|G|, sign) fixes tr A on every state"]
    assert f["F5 census level-manifolds by k"] == {"1": 536, "2": 79, "3": 32, "4": 5, "5": 4, "6": 1, "7": 2}


# ------------------------------------------------------------------------------------------------- surfaces
def test_the_bar_standing_text():
    t = _norm(ROOT / "docs" / "THE_BAR.md")
    for s in ("DERIVED", "REPRODUCED", "FITTED", "UNJUDGED", "p < 0.01", "B614", "87 of 536 manifolds", "B1518"):
        assert s in t, s


def test_findings_quote_the_records():
    t = _norm(ARC / "FINDINGS.md")
    r, q = _json("bar_run.json"), _json("post_run_checks.json")
    corrected = r["predictions"]["corrected p-values (T2, T3)"]
    assert f"{round(corrected[1], 3)}" in t                       # 0.022
    assert f"{r['tests']['T2 leave-one-out AUC under S1']:.3f}" in t  # 0.858
    for s in ("87 of 536", "6 of 36", "0 of 34", "o9_00001", "m369", "Twenty-two", "0.986", "PROVED"):
        assert s in t, s
    assert math.isclose(q["Q5 the bar applied to the record's positives"][
        "m369 and s639 (B1434; found by scanning 24 manifolds)"]["p = 1 - (1 - r_P)^24"], 0.9857)
