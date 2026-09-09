"""B1242 — L199 closed: both priced identifications paid, both refuted, the containment earned."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1242_l199_two_earning_computations"
LEDGER = ROOT / "docs" / "IDENTIFICATION_LEDGER.md"

def _rows():
    out = {}
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        import re
        m = re.match(r"\|\s*(I-\d+)\s*\|", line)
        if m:
            st = re.search(r"\*\*(EARNED|UNEARNED|REFUTED)\*\*", line)
            out[m.group(1)] = st.group(1) if st else "?"
    return out

def test_both_priced_rows_are_now_refuted_and_the_containment_is_earned():
    r = _rows()
    assert r["I-15"] == "REFUTED" and r["I-16"] == "REFUTED", r
    assert r["I-19"] == "EARNED", r
    assert r["I-12"] == "EARNED" and r["I-13"] == "UNEARNED"   # nothing else moved

def test_the_ratchet_was_lowered_by_EARNING_not_by_relabelling():
    """B1242's lowering 10 -> 8 came from REFUTING two rows, not from relabelling them.

    Originally this pinned `unearned == 8` literally. That is a SNAPSHOT, not the invariant:
    it went red at B1250 when a documented raise 8 -> 9 registered I-23 (a PRE-EXISTING debt
    named for the first time -- B919's Y-anchoring). Replaced with a STRICTLY STRONGER check:
    replay the whole documented raise/lowering history and require it to land exactly on the
    live count. That audits the entire audit trail rather than one number, so an undocumented
    change to `unearned` now reds the suite even if someone edits the count to match the ledger.
    """
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    live = _rows()
    live_unearned = sum(1 for v in live.values() if v == "UNEARNED")

    # the ratchet is kept TIGHT: baseline == live, rows and totals agree
    assert b["unearned"] == live_unearned
    assert set(b["rows"]) == {k for k, v in live.items() if v == "UNEARNED"}
    assert b["total_rows"] == len(live)

    # B1242's own lowering is history and must stay recorded as EARNING, not relabelling
    low = next(x for x in b["_baseline_lowerings"] if x["to"] == 8)
    assert low["from"] == 10 and "I-15" in low["rows"] and "I-16" in low["rows"]
    assert "REFUTED" in low["reason"] and "not by relabelling" in low["reason"]

    # EVERY movement of the count must be documented, and the trail must reconstruct it
    moves = sorted(
        [(x["date"], x["from"], x["to"], "raise") for x in b["_baseline_raises"]]
        + [(x["date"], x["from"], x["to"], "lower") for x in b["_baseline_lowerings"]]
    )
    cur = moves[0][1]
    for date, frm, to, kind in moves:
        assert frm == cur, f"audit trail broken at {date}: {kind} claims from={frm}, running={cur}"
        cur = to
    assert cur == live_unearned, f"trail ends at {cur} but the ledger has {live_unearned} UNEARNED"

    # every raise carries a reason -- an undocumented raise is the failure the ratchet exists for
    for x in b["_baseline_raises"]:
        assert x.get("reason"), f"raise {x['from']}->{x['to']} has no reason"
        assert x.get("row"), f"raise {x['from']}->{x['to']} names no row"

def test_the_arc_reproduces_by_RUNNING_its_script_not_reading_a_string():
    r = subprocess.run([sys.executable, str(ARC / "verification" / "l199_two_earning_computations.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert r.stdout.rstrip().endswith("REPRODUCES"), r.stdout[-500:]

def test_the_two_load_bearing_numbers():
    j = json.loads((ARC / "verification" / "l199.json").read_text(encoding="utf-8"))
    d = j["B"]["dynkin_index_principal_sl2"]
    assert d["route_adjoint"] == d["route_27"] == d["route_rho"] == 156, d
    assert j["B"]["B715_trace_reproduced"] is True
    a = j["A3_discriminant_forms"]
    silver = a["silver cusp, minimal even rescaling (x2)"]
    A3 = a["A3 root lattice (Cartan matrix)"]
    # THE REFUTATION, as data: the two discriminant forms differ on group AND level
    assert silver["group"] == [2, 8] and A3["group"] == [4], (silver["group"], A3["group"])
    assert silver["level"] == 16 and A3["level"] == 8, (silver["level"], A3["level"])
    assert A3["generator_q"] == ["3/8"], A3            # B675's A3 datum WAS right

def test_B675_and_B715_are_corrected_at_source_not_only_in_the_log():
    for arc, frag in (("B675_hcusp_sweep", "REFUTED"), ("B715_native_gauge", "I-15")):
        v = json.loads((ROOT / "frontier" / arc / "arc_verdict.json").read_text(encoding="utf-8"))
        assert "B1242" in json.dumps(v), f"{arc}: correction never reached its verdict file (E53)"
        assert (ROOT / "frontier" / arc / "ADDENDUM_2026-09-03_B1242.md").exists()

def test_the_verdicts_of_the_corrected_arcs_are_NOT_reversed():
    for arc, want in (("B675_hcusp_sweep", "PROVED"), ("B715_native_gauge", "PROVED")):
        v = json.loads((ROOT / "frontier" / arc / "arc_verdict.json").read_text(encoding="utf-8"))
        assert v["verdict"] == want, f"{arc}: the lattice/trace facts stand; only the identification fell"
