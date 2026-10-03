#!/usr/bin/env python3
"""B1529 post-run (written after the census finished; disclosed in FINDINGS): the census's per-manifold record, kept in the tree.

census.py writes census.jsonl, one line per manifold, appended as each finishes; read_out.py reads it.  The repository ignores
*.jsonl (the chronicle-harvest firewall in .gitignore), so that file stays on the bench.  This writes census_records.json: the
541 records in the file's order, unchanged, with the sha-256 of the census.jsonl they came from.  The lock rebuilds a
census.jsonl from it in a temporary directory and runs read_out.py's census reader there.
Note: census.py's list of states reads sm:B1523's route_f_seeded.jsonl, which is also untracked; each record carries its
state and the word it was read as, so census.one can re-run any manifold without that list."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    src = HERE / "census.jsonl"
    raw = src.read_bytes()
    lines = raw.decode().splitlines()
    recs = [json.loads(line) for line in lines]
    assert len(recs) == 541 and len({r["state"] for r in recs}) == 541
    out = {"source": "census.jsonl", "sha256 of the source": hashlib.sha256(raw).hexdigest(), "records": recs}
    (HERE / "census_records.json").write_text(json.dumps(out, indent=0, default=str) + "\n")
    back = json.loads((HERE / "census_records.json").read_text())["records"]
    assert [json.dumps(r, sort_keys=True) for r in back] == [json.dumps(r, sort_keys=True) for r in recs]
    print(f"census_records.json: {len(recs)} records, source sha-256 {out['sha256 of the source'][:16]}...")


if __name__ == "__main__":
    main()
