#!/usr/bin/env python3
"""Mechanical integrity checks for the shared programme question map."""

from collections import Counter
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "inventory" / "backbone.json"
ALLOWED = {
    "OPEN", "PROVED", "REFUTED", "CONDITIONAL", "EXTERNAL_BLOCKER",
    "EMPIRICAL", "OUT_OF_SCOPE",
}
EXPECTED_COUNTS = {
    "OPEN": 21,
    "PROVED": 70,
    "REFUTED": 55,
    "CONDITIONAL": 15,
    "EXTERNAL_BLOCKER": 22,
    "EMPIRICAL": 2,
    "OUT_OF_SCOPE": 0,
}
EXPECTED_OPEN = {
    "OA-C1074", "OA-C1115", "OA-C1117", "OA-C1118", "OA-C1132",
    "OA-C1134", "OA-C1140", "OA-C1145", "OA-C1148", "OA-C1149",
    "OA-C1150", "OA-C1151", "OA-C1152", "OA-C1153", "OA-C1154",
    "OA-C1156", "OA-C1157", "OA-C1158", "OA-C1159",
    "OA-C1166", "OA-C1168",
}


def resolve(reference):
    if reference.startswith(("http://", "https://")):
        return None
    return (REGISTRY.parent / reference).resolve()


data = json.loads(REGISTRY.read_text(encoding="utf-8"))
rows = data["items"]
ids = [row["campaign_id"] for row in rows]
known = set(ids)
assert len(rows) == 185
assert len(ids) == len(known)
assert all(re.fullmatch(r"OA-C\d{4}", item) for item in ids)
for row in rows:
    assert row["adjudicated_status"] in ALLOWED, row["campaign_id"]
    assert row["question"].strip().endswith("?"), row["campaign_id"]
    assert row["closure_criterion"].strip(), row["campaign_id"]
    assert row["falsifier"].strip(), row["campaign_id"]
    assert set(row.get("dependencies", ())) <= known, row["campaign_id"]
    assert set(row.get("children", ())) <= known, row["campaign_id"]

counts = Counter(row["adjudicated_status"] for row in rows)
assert {status: counts.get(status, 0) for status in ALLOWED} == EXPECTED_COUNTS
actual_open = {row["campaign_id"] for row in rows
               if row["adjudicated_status"] == "OPEN"}
assert actual_open == EXPECTED_OPEN

# Every locally cited artifact added by the current Wave-2 through Wave-5 extension must be branch-local.
for row in rows:
    if int(row["campaign_id"].split("C", 1)[1]) < 1065:
        continue
    for key in ("sources", "deepest_artifacts"):
        for reference in row.get(key, ()):
            target = resolve(reference)
            if target is not None:
                assert target.exists(), f"{row['campaign_id']} missing {reference}"

print("question_map_rows=185")
print("question_map_statuses=" + json.dumps(EXPECTED_COUNTS, sort_keys=True))
print("question_map_open=" + json.dumps(sorted(EXPECTED_OPEN)))
print("QUESTION MAP INTEGRITY: PASS")
