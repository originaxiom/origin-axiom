"""B1425 evidence -- the E83 sweep: every tracked .py that hands an unordered collection somewhere order matters.

A set has no order, so `list(some_set)` produces a different list per interpreter run. Where that list is a
solver's unknowns, a basis, or an index, the ANSWER's normalisation moves with PYTHONHASHSEED. This lists the
sites and separates the ones that can bite (multi-element, feeding a solver or an index) from the ones that
cannot (single-symbol indexings, or sorted at the point of use).
"""
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent / "order_sensitivity_sweep.json"
PATTERNS = [
    (r"list\(\s*[A-Za-z_][\w.]*\.free_symbols\s*\)", "list(free_symbols) -- unordered unknowns"),
    (r"list\(\s*[A-Za-z_][\w.]*\.atoms\(", "list(atoms(...)) -- unordered"),
    (r"\.free_symbols\s*\)\s*\[", "free_symbols indexed directly"),
    (r"for\s+\w+\s+in\s+[A-Za-z_][\w.]*\.free_symbols\b", "iteration over free_symbols"),
    (r"list\(\s*set\(", "list(set(...)) -- order lost"),
]


def main():
    files = subprocess.run(["git", "ls-files", "*.py"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    hits = []
    for rel in files:
        try:
            lines = (ROOT / rel).read_text(errors="replace").split("\n")
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            if line.lstrip().startswith("#"):
                continue
            for pat, why in PATTERNS:
                if re.search(pat, line):
                    sorted_here = "sorted(" in line
                    hits.append({"file": rel, "line": i, "why": why, "text": line.strip()[:160],
                                 "sorted_at_use": sorted_here,
                                 "is_lock": rel.startswith("tests/")})
                    break
    res = {
        "files_scanned": len(files),
        "sites": hits,
        "site_count": len(hits),
        "unsorted_sites": [h for h in hits if not h["sorted_at_use"]],
        "locks_touched": sorted({h["file"] for h in hits if h["is_lock"]}),
    }
    res["unsorted_count"] = len(res["unsorted_sites"])
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    print("scanned %d tracked .py; %d order-sensitive site(s), %d of them unsorted at the point of use"
          % (res["files_scanned"], res["site_count"], res["unsorted_count"]))
    for h in res["unsorted_sites"]:
        print("  %s:%d  %s" % (h["file"], h["line"], h["why"]))
    print("locks touched: %s" % (", ".join(res["locks_touched"]) or "none"))


if __name__ == "__main__":
    main()
