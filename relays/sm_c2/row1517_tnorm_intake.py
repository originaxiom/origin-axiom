#!/usr/bin/env python3
"""SM-C2, harvest row 1517 (the T-NORM intake @ ce2a3a6e3): this seat's own check of the intake's metadata. It recomputes
from git objects (run from a clone that has the lane's branch and main): (a) every sha256 the custody receipt
SELF_AUDIT_CUSTODY_2026_11_01.json pins for the P210 sources and execution artifacts, at the commits it names or at
the intake commit; (b) the P210 event counts, recounted from the pinned attempt_01.jsonl: ten distinct tests, each
started and passed once, equal to the receipt's counts; (c) the two scope statements the intake makes, by quoting:
main's B1822 record says H = I is a CHOSEN input; the lane's coefficient-metric note confines its scalar result to the
constant, fibre-parallel, move-invariant class and exhibits a nonconstant positive covariant family. Planted: one
pinned digest altered by one hex digit must be reported as a mismatch. Usage: row1517_tnorm_intake.py OUT.json [REPO]"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

repo = sys.argv[2] if len(sys.argv) > 2 else "."
C = "ce2a3a6e3"
D = "reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17"


def show(rev_path):
    return subprocess.run(["git", "-C", repo, "show", rev_path], capture_output=True, check=True).stdout


rec = json.loads(show(f"{C}:{D}/SELF_AUDIT_CUSTODY_2026_11_01.json"))
out = {"receipt_kind": rec["kind"], "pins": [], "artifacts": []}


def check(entry, bucket, alter=False):
    path = entry.get("path")
    exp = entry.get("expected_sha256")
    if not path or not exp:
        out[bucket].append({"entry": entry, "skipped": "no path/expected_sha256"})
        return None
    rev = entry.get("commit") or entry.get("source_commit") or C
    try:
        blob = show(f"{rev}:{path}")
    except subprocess.CalledProcessError:
        out[bucket].append({"path": path, "rev": rev, "result": "MISSING"})
        return False
    act = hashlib.sha256(blob).hexdigest()
    want = (exp[:-1] + ("0" if exp[-1] != "0" else "1")) if alter else exp
    ok = act == want
    if not alter:
        out[bucket].append({"path": path, "rev": rev, "match": ok})
    return ok


pin_results = [check(e, "pins") for e in rec["p210_source_pin_checks"]]
art_results = [check(e, "artifacts") for e in rec.get("p210_execution_artifact_checks", [])]
out["pins_checked"] = sum(1 for r in pin_results if r is not None)
out["pins_matching"] = sum(1 for r in pin_results if r)
out["artifacts_checked"] = sum(1 for r in art_results if r is not None)
out["artifacts_matching"] = sum(1 for r in art_results if r)
ev = rec["p210_event_counts"]
out["p210_event_counts"] = ev
events = [json.loads(x) for x in show(f"{C}:{D}/verification_p210/results/attempt_01.jsonl").decode().splitlines()
          if x.strip()]
kinds = {}
for e in events:
    k = e.get("stage") or "record:" + next(iter(e))
    kinds[k] = kinds.get(k, 0) + 1
out["event_counts_recounted_from_jsonl"] = kinds
ids_start = sorted(str(e.get("test") or e.get("test_id") or e.get("name")) for e in events
                   if e.get("stage") == "test_start")
ids_pass = sorted(str(e.get("test") or e.get("test_id") or e.get("name")) for e in events
                  if e.get("stage") == "test_pass")
out["recount_ok"] = (kinds.get("test_start") == ev["test_start"] == 10
                     and kinds.get("test_pass") == ev["test_pass"] == 10 and len(ids_start) == 10 and ids_start == ids_pass
                     and len(set(ids_start)) == 10)
out["recorded_flags"] = {k: rec[k] for k in ("expected_test_set_equals_recorded_starts_and_passes",
                                               "each_recorded_test_starts_and_passes_once", "new_scientific_execution",
                                               "foundational_inputs_removed_by_this_checkpoint")}
note = show(f"{C}:{D}/COEFFICIENT_METRIC_CONSTRAINTS_AND_PHYSICAL_PRICES.md").decode()
log = show("origin/main:CHANGELOG.md").decode()
out["quotes"] = {
    "main_B1822_H=I_CHOSEN": "H = I is a CHOSEN input" in log,
    "note_constant_move_invariant_class": "Forced in the constant fibre-parallel, move-invariant class" in note,
    "note_nonconstant_positive_family": "explicit positive nonconstant family" in note,
}
first_pin = next(e for e in rec["p210_source_pin_checks"] if e.get("path"))
out["PLANTED_altered_digest_reported"] = check(first_pin, "pins", alter=True) is False
ok = (out["pins_checked"] > 0 and out["pins_matching"] == out["pins_checked"]
      and out["artifacts_matching"] == out["artifacts_checked"] and all(out["quotes"].values())
      and rec["expected_test_set_equals_recorded_starts_and_passes"]
      and rec["each_recorded_test_starts_and_passes_once"]
      and out["recount_ok"])
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_altered_digest_reported"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k not in ("pins", "artifacts")}, indent=1, default=str))
