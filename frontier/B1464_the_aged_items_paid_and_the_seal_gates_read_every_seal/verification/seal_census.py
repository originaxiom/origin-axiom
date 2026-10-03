#!/usr/bin/env python3
"""B1464 -- the seal census behind Review 59's headline: how many digests each parser read, how many seals in the rule's
range carry the provenance halves, and the frozen baseline.  Reads main's own files through the gates module."""
import sys, os, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "gates")); import gates
import re
def old_parser_rows(text):
    out = []
    for line in text.splitlines():
        if not re.match(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|", line): continue
        out.append(line)
    return out
def main():
    led = gates._read("docs/SEAL_LEDGER.md"); rows = gates._seal_ledger_rows(led)
    out = dict(digest_strings_in_ledger=len(re.findall(r"`[0-9a-f]{64}`", led)), rows_old_parser=len(old_parser_rows(led)), rows_both_shapes=len(rows),
               distinct_sealed_paths_with_digest=len({r for _, r, g in rows if g}))
    files = gates.sealed_files(); inr = [(a, r) for a, r in files if a >= gates.SEAL_PROVENANCE_FROM_ARC]
    markers = sections = neither = 0
    for a, r in inr:
        t = open(ROOT / r, errors="replace").read()
        m = "BANKED IDENTITY:" in t and "PRIOR ART:" in t; s = a >= gates.SEEN_FIRST_FROM_ARC and re.search(r"(?m)^##[^\n]*Seen first", t) and re.search(r"(?m)^##[^\n]*Disclosed", t)
        markers += bool(m); sections += bool(s and not m); neither += (not m and not s)
    out.update(sealed_files=len(files), in_rule_range=len(inr), with_markers=markers, with_sections=sections, with_neither=neither, baseline=len(gates.SEAL_PROVENANCE_BASELINE))
    out["gates"] = {g: gates.GATES[g]() for g in ("seal-provenance", "seal-digests", "seal-ledger-current", "pretense-phrases")}
    ok = out["with_neither"] == out["baseline"] and all(v[0] for v in out["gates"].values()) and out["rows_both_shapes"] > out["rows_old_parser"]
    out["verdict"] = "PASS" if ok else "FAIL"
    json.dump(out, open(HERE / "seal_census.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str)); print("VERDICT seal-census: %s" % out["verdict"]); return 0 if ok else 1
if __name__ == "__main__":
    sys.exit(main())
