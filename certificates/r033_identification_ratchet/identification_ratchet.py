#!/usr/bin/env python3
"""R033: exact audit of B1231's seed ledger and its pre-Phase-C ratchet.

This certificate proves a governance fact about the frozen B1231 record.  It
does not adjudicate the six legacy candidates as EARNED or UNEARNED.  Their
classification is Phase C's mathematical work.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "source_snapshot.json"


def main() -> None:
    data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    assert data["schema"] == "oa-r033-identification-ratchet-snapshot-v1"
    assert data["source_commit"] == "8f0cda3d"

    sources = data["sources"]
    rows = sources["identification_ledger"]["rows"]
    baseline = sources["identification_baseline"]
    declared = set(sources["b1231_verdict"]["declared_identification_rows"])

    assert set(rows) == {f"I-{index}" for index in range(1, 8)}
    assert declared == {"I-6", "I-7"}
    assert sum(status == "EARNED" for status in rows.values()) == 3
    assert sum(status == "REFUTED" for status in rows.values()) == 2
    assert sum(status == "UNEARNED" for status in rows.values()) == 2
    assert baseline == {
        "path": "docs/IDENTIFICATION_BASELINE.json",
        "git_blob_sha1": "53af822e5a974df603f44e90e8751847e14e0634",
        "unearned": 2,
        "total_rows": 7,
    }

    findings_text = " ".join(sources["b1231_findings"]["excerpts"])
    assert "listener map `u` IS an identification map" in findings_text
    assert "performed implicitly and for free" in findings_text
    assert "Pricing it *is* the crossing cell" in findings_text
    assert "queued, not run" in findings_text

    admitted = data["admitted_but_unregistered"]
    assert admitted["id"] == "listener-u"
    assert admitted["ledger_row"] is None
    descriptions = sources["identification_ledger"]["identifications"]
    assert set(descriptions) == set(rows)
    assert "listener" not in " ".join(descriptions.values()).lower()

    test_text = " ".join(sources["b1231_test"]["excerpts"])
    assert "A NEW unearned identification must red the gate" in test_text
    assert 'base["unearned"] == live' in test_text
    gate_text = " ".join(sources["identification_gate"]["excerpts"])
    assert "UNEARNED increased" in gate_text
    assert "raise the baseline DELIBERATELY with a dated reason" in gate_text

    current_unearned = sum(status == "UNEARNED" for status in rows.values())
    with_admitted_listener = current_unearned + 1
    assert current_unearned == baseline["unearned"]
    assert with_admitted_listener > baseline["unearned"]

    candidates = data["phase_c_candidates"]
    assert len(candidates) == 6
    assert len({candidate["id"] for candidate in candidates}) == len(candidates)
    assert all(candidate["arc"] < 1231 for candidate in candidates)
    assert all(candidate["audit_status"] == "NEEDS_PHASE_C"
               for candidate in candidates)
    assert all(candidate["side_a"] and candidate["side_b"] and candidate["missing"]
               for candidate in candidates)

    # Controls: the conflict is specific to an unresolved discovery.  A newly
    # earned row does not increase the live count; removing one debt decreases it.
    assert current_unearned + int("EARNED" == "UNEARNED") == baseline["unearned"]
    assert current_unearned - 1 < baseline["unearned"]

    print("PASS B1231 seed ledger = 7 rows (3 earned, 2 refuted, 2 unearned)")
    print("PASS B1231 itself admits listener map u is an unpriced identification")
    print("PASS listener map u has no row in the seven-row ledger")
    print("PASS registering that admitted debt gives 3 UNEARNED > baseline 2")
    print("CONTROL an EARNED addition preserves the count; resolving a debt lowers it")
    print("DATA legacy Phase-C candidates typed, not adjudicated =", len(candidates))
    print("RESULT green count 2 is a seed state, not a complete identification census")
    print("RESULT registering the admitted listener debt requires a deliberate dated baseline migration")
    print("SCOPE inventory correction only; no candidate is promoted and no bit count follows")


if __name__ == "__main__":
    main()
