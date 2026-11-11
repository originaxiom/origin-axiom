#!/usr/bin/env python3
"""B1879 (Re-Audit 3, t7): Complete census and classification of every tracked file outside ARTIFACT_HASHES*.txt
carrying `<sha256> <filename>` entries, plus verification of secondary seal hash lists gated by `artifact-hashes`."""
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "gates"))
import gates as g

HEUR_RE = re.compile(r"^[0-9a-f]{64}\s+\S+", re.M)


def main():
    tracked = set(subprocess.check_output(["git", "-C", ROOT, "ls-files"], text=True).splitlines())
    other_state = g.other_hash_list_state(ROOT)
    gated_files = sorted(
        f for f in tracked
        if f.startswith(("frontier/", "outside_bench/"))
        and not (os.path.basename(f).startswith("ARTIFACT_HASHES") and f.endswith(".txt"))
        and os.path.basename(f) not in g.OTHER_INTAKE_BASENAMES
        and g.OTHER_SEAL_HASH_RE.match(os.path.basename(f))
    )
    heur_rows = []
    for f in sorted(tracked):
        if os.path.basename(f).startswith("ARTIFACT_HASHES") and f.endswith(".txt"):
            continue
        if not f.endswith((".txt", ".sha256", ".sums", ".manifest")):
            continue
        txt = open(os.path.join(ROOT, f), encoding="utf-8", errors="replace").read()
        lines = HEUR_RE.findall(txt)
        if not lines:
            continue
        base = os.path.basename(f)
        if base in g.OTHER_INTAKE_BASENAMES:
            cat = "INTAKE_OR_LARGE_OUTPUT_MANIFEST"
        elif f in gated_files:
            cat = "GATED_SECONDARY_SEAL_LIST"
        else:
            cat = "RUN_OUTPUT_LOG"
        heur_rows.append((f, len(lines), cat))

    verifies = [x for x in other_state if x[3] == "VERIFIES"]
    broken = [x for x in other_state if x[3] != "VERIFIES"]
    summary = {
        "heuristic_files_total": len(heur_rows),
        "heuristic_lines_total": sum(x[1] for x in heur_rows),
        "category_file_counts": {
            c: sum(1 for x in heur_rows if x[2] == c)
            for c in sorted({x[2] for x in heur_rows})
        },
        "gated_secondary_files_matched": len(gated_files),
        "gated_secondary_entries_total": len(other_state),
        "gated_secondary_entries_verifies": len(verifies),
        "gated_secondary_entries_broken": len(broken),
        "gated_secondary_distinct_broken_keys": len({x[0] for x in broken}),
        "gated_secondary_mismatch_disk_pinned": len(g.OTHER_HASH_LISTS_BROKEN_DISK),
    }
    out_json = os.path.join(os.path.dirname(__file__), "other_hash_lists_census.json")
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump({"summary": summary, "heuristic_files": heur_rows}, fh, indent=2)

    if "--write-doc" in sys.argv:
        lines_md = [
            "# Secondary Seal Hash Lists and Intake Manifests (`B1879`; Re-Audit 3 `t7`)",
            "",
            "Measured at `015be0cc7` in `B1879` (`frontier/B1879_reaudit3_enforcement_and_p670_closure/verification/measure_other_hash_lists.py`).",
            "Re-Audit 3 (`t7`) found `70`+ tracked non-`ARTIFACT_HASHES*.txt` files holding `<sha256> <filename>` lines.",
            "`gate_artifact_hashes` now enforces all secondary seal hash lists (`OTHER_SEAL_HASH_RE` under `frontier/` and `outside_bench/`,",
            f"`{len(gated_files)}` matched files, `{len(other_state)}` hash entries: `{len(verifies)}` verify, `{len(broken)}` pre-existing historical",
            f"entries frozen by key in `OTHER_HASH_LISTS_BROKEN` with `{len(g.OTHER_HASH_LISTS_BROKEN_DISK)}` present-disk SHA-256 digests pinned in `OTHER_HASH_LISTS_BROKEN_DISK`),",
            "and holds every secondary seal hash list immutable in git history from `OTHER_HASH_LISTS_IMMUTABLE_FROM` (`015be0cc7`).",
            "",
            "## 1. Classification of the 71 heuristic `<sha256> <file>` files",
            "",
            "| Category | Files | Lines | Disposition |",
            "|---|---:|---:|---|",
            f"| `GATED_SECONDARY_SEAL_LIST` (`*SEAL*.txt`, `*SHA256*.txt`, `*.sha256`, `*HASHES*.txt`, `*.sums`, etc.) | {summary['category_file_counts'].get('GATED_SECONDARY_SEAL_LIST', 0)} | {sum(x[1] for x in heur_rows if x[2] == 'GATED_SECONDARY_SEAL_LIST')} | Gated by `artifact-hashes` (`other_hash_list_state` + `other_hash_lists_immutable_problems`) |",
            f"| `INTAKE_OR_LARGE_OUTPUT_MANIFEST` (`ORIGINALS_MANIFEST.txt`, `SHA256_RECEIVED.txt`, `SHA256_AS_RECEIVED.txt`, `LARGE_OUTPUTS_SHA256.txt`) | {summary['category_file_counts'].get('INTAKE_OR_LARGE_OUTPUT_MANIFEST', 0)} | {sum(x[1] for x in heur_rows if x[2] == 'INTAKE_OR_LARGE_OUTPUT_MANIFEST')} | Provenance intake / gitignored large-output manifests (record external ZIP / pre-consolidation intake hashes, not live seal instruments) |",
            f"| `RUN_OUTPUT_LOG` (`cell1_output_partial.txt`) | {summary['category_file_counts'].get('RUN_OUTPUT_LOG', 0)} | {sum(x[1] for x in heur_rows if x[2] == 'RUN_OUTPUT_LOG')} | Partial stdout transcript, not a seal hash list |",
            "",
            "## 2. Pre-existing non-verifying entries in secondary seal hash lists (frozen at `015be0cc7`)",
            "",
            "| Key | List path | Entry / resolved path | State |",
            "|---|---|---|---|",
        ]
        for k, lst, nm, st in sorted(broken):
            nm_cell = f"`{nm}`" if (nm and st == "MISMATCH") else (nm or "(no name)")
            lines_md.append(f"| `{k}` | `{lst}` | {nm_cell} | `{st}` |")
        lines_md.append("")
        with open(os.path.join(ROOT, "docs", "OTHER_HASH_LISTS.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_md))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
