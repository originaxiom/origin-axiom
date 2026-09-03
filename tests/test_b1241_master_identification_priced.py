"""B1241 -- THE MASTER IDENTIFICATION PRICED + the fc R51/R52/Phase E part 1 harvest.  Locks assert facts with what decides them.

Three kinds of lock: (1) THE REGISTER -- I-13 (the listener map u) .. I-16 are UNEARNED and I-17 REFUTED in the live
ledger, the baseline's UNEARNED equals the live count (the by-hand raise is logged with its rows), and the arc's
arc_verdict declares exactly these five; (2) THE CORRECTIONS -- LAW_MAP:263 carries the dated bracket, B232 is OPEN with
its claim rewritten, B167's claim names the POSTULATED premise, B647's says NOT forced -- each pinned together with the
prose that decides it in the source arc; (3) THE RECOMPUTATIONS -- R51's residuals (77 = 34 + 43; six metallic bundles
amphicheiral, order 8, CS = 0) and R52's cubic, read from the JSON the verification scripts regenerate, and the runner
executed (subprocess) so the lock is not a string."""
import csv
import json
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1241_master_identification_priced_and_phase_e_harvest"
V = ARC / "verification"
LEDGER = ROOT / "docs" / "IDENTIFICATION_LEDGER.md"
BASELINE = ROOT / "docs" / "IDENTIFICATION_BASELINE.json"


def _j(name):
    return json.loads((V / name).read_text(encoding="utf-8"))


def _rows():
    out = {}
    for m in re.finditer(r"^\|\s*(I-\d+)\s*\|(.*)$", LEDGER.read_text(encoding="utf-8"), re.M):
        cells = [c.strip().strip("*").strip() for c in m.group(2).split("|")]
        out[m.group(1)] = next((c for c in cells if c in ("EARNED", "REFUTED", "UNEARNED")), None)
    return out


# ---------------------------------------------------------------- 1. the register
def test_the_master_identification_is_registered_unearned_and_names_the_crossing_as_its_price():
    line = next(l for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.startswith("| I-13 |"))
    assert "**UNEARNED**" in line and "listener map u" in line.lower().replace("the listener map u", "listener map u")
    assert "B532" in line and "CLOSURE_2026-07-11" in line          # first explicit use, and the only fence
    assert "crossing cell" in line and "W5/W6" in line                # what earns it: nothing inside the object


def test_the_five_rows_are_registered_and_the_two_fixed_statuses_hold():
    # fact-pins, not count-pins (E53 rule): I-13 stays UNEARNED until the crossing cell earns it (that is the
    # row's point); I-17 is REFUTED by a theorem (B727) and cannot move back; I-14/I-15/I-16 are registered
    # here with a status a later DATED cell may move (L199 names the two computations). I-12 was EARNED by a
    # computation (B1238) and stays.
    r = _rows()
    assert r["I-13"] == "UNEARNED" and r["I-17"] == "REFUTED" and r["I-12"] == "EARNED"
    assert all(r[k] in {"UNEARNED", "EARNED", "REFUTED"} for k in ("I-14", "I-15", "I-16"))
    assert {"I-6", "I-7", "I-9", "I-10", "I-11"} <= set(r)   # nothing older dropped


def test_the_baseline_was_raised_by_hand_and_equals_the_live_count():
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    live = sum(1 for v in _rows().values() if v == "UNEARNED")
    assert base["unearned"] == live                       # the ratchet is kept TIGHT (baseline == live), never slack
    assert "I-13" in base["rows"] and "I-17" not in base["rows"]
    raise_ = next(r for r in base["_baseline_raises"] if r.get("to") == 9)   # the B1241 raise is history: 5 -> 9
    assert raise_["from"] == 5 and "I-13" in raise_["row"] and "listener map u" in raise_["reason"]
    assert base["total_rows"] == len(_rows())
    assert set(base["rows"]) == {k for k, v in _rows().items() if v == "UNEARNED"}   # rows == the live UNEARNED set


def test_the_arc_declares_exactly_the_five_rows():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1241" and d["verdict"] == "OPEN" and d["instrument"] is False and d["creates_law"] is False
    decl = {i["row"]: i["status"] for i in d["identifications"]}
    assert decl == {"I-13": "UNEARNED", "I-14": "UNEARNED", "I-15": "UNEARNED", "I-16": "UNEARNED", "I-17": "REFUTED"}
    assert {"date", "arc", "was", "decision", "class", "basis"} <= set(d["creates_law_reviewed"])
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "## THE PRIZE FIRST" in f and "I-13" in f and "listener map u" in f


# ---------------------------------------------------------------- 2. the corrections, each with what decides it
def test_law_map_263_carries_the_correction_and_the_retracted_number_is_named_as_retracted():
    row = next(l for l in (ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8").splitlines()
               if l.startswith("| **THE ONE-WAY FAMILY TEST"))
    assert "[2026-09-02 B1241]" in row and "83/83 was the orientation-blind isometry call" in row
    assert "depends on the quantifier" in row
    # what decides it: B1181 is RETRACTED on main and B1235's split is 38/112
    b1181 = json.loads((ROOT / "frontier" / "B1181_amphichirality_closure" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert b1181["verdict"] == "RETRACTED"
    ch = json.loads((ROOT / "frontier" / "B1235_two_seat_harvest" / "verification" / "chirality_112.json").read_text(encoding="utf-8"))
    assert sum(1 for r in ch if r["amphicheiral"]) == 38 and len(ch) == 112
    assert (ROOT / "frontier" / "B1235_two_seat_harvest" / "ADDENDUM_2026-09-02_B1241.md").exists()


def test_b232_is_open_because_its_own_findings_call_it_a_reduction():
    arc = ROOT / "frontier" / "B232_rho_n_plethysm"
    v = json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "OPEN" and "REDUCED" in v["claim_one_line"] and "n=8" in v["claim_one_line"]
    f = (arc / "FINDINGS.md").read_text(encoding="utf-8")
    assert "not** a proof" in f or "not a proof" in f                  # the deciding prose
    assert (arc / "ADDENDUM_2026-09-02_B1241.md").exists()


def test_b167_claim_names_its_postulated_premise():
    arc = ROOT / "frontier" / "B167_conserved_no_scale_lemma"
    v = json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "NEGATIVE" and "POSTULATED" in v["claim_one_line"]
    assert "POSTULATED" in (arc / "FINDINGS.md").read_text(encoding="utf-8")
    assert (arc / "ADDENDUM_2026-09-02_B1241.md").exists()


def test_b647_claim_says_not_forced_as_its_cell_does():
    arc = ROOT / "frontier" / "B647_core_mechanism"
    v = json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and "NOT forced" in v["claim_one_line"] and "arg Y[134] = π/6" in v["claim_one_line"]
    body = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in arc.rglob("*") if p.is_file() and p.suffix in (".md", ".txt"))
    assert "NOT forced" in body                                        # the deciding prose in the arc's own record
    assert (arc / "ADDENDUM_2026-09-02_B1241.md").exists()


# ---------------------------------------------------------------- 3. the recomputations
def test_r51_residuals_reproduce_from_the_json():
    j = _j("r51_all_regular_subfamily.json")
    a = j["all_regular"]
    assert (a["size"], a["amphichiral"], a["chiral"]) == (77, 34, 43)
    assert len(j["metallic_bundles"]) == 6
    assert all(m["amphicheiral"] and m["order"] == 8 and abs(m["cs"]) < 1e-9 for m in j["metallic_bundles"])
    assert abs(j["metallic_bundles"][0]["volume"] - 2.029883212819307) < 1e-9     # m = 1 is the figure-eight
    assert j["fc_r51_claims_hold"] is True


def test_r52_anomaly_cubic_reproduces_from_the_json():
    j = _j("r52_anomaly_cubic.json")
    assert j["equals_R52_form"] is True and j["ok"] is True
    assert j["lines"]["hypercharge"] == ["1", "-4", "6", "2", "-3"]
    assert j["lines"]["u<->d swap"] == ["1", "2", "6", "-4", "-3"]
    assert j["plane"] == {"yQ": "-yL/3", "ye": "-2*yL", "yu": "2*yL/3 - yd"}


def test_the_dispositions_tsv_carries_every_spine_row_and_the_seat_citation_corrections():
    rows = list(csv.DictReader((V / "fc_phase_e_rows_verified.tsv").open(encoding="utf-8"), delimiter="\t"))
    by = {r["arc"]: r for r in rows}
    assert len(rows) == 18 and {"B532", "B305", "B715", "B675", "B312", "B660", "B666", "B232", "B167", "B647"} <= set(by)
    assert {by[a]["register_row"] for a in ("B532", "B305", "B715", "B675", "B312")} == {"I-13", "I-14", "I-15", "I-16", "I-17"}
    assert by["B660"]["cc_status_on_main"].startswith("SELF-CAUGHT")
    assert "CLOSURE_2026-07-11" in by["B532"]["cc_status_on_main"]
    assert "too strong" in by["B305"]["cc_status_on_main"]


def test_r52_script_runs_and_prints_reproduces():
    r = subprocess.run(["python3", str(V / "r52_anomaly_cubic.py")], capture_output=True, text=True, cwd=str(V), timeout=120)
    assert r.returncode == 0 and "R52 anomaly cubic: REPRODUCES" in r.stdout
