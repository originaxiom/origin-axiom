#!/usr/bin/env python3
"""sense-census -- is a technical CONCEPT in the corpus, or merely its WORD?  (the cloud seat's memo 172 instrument; ADOPTED B1307)

PROVENANCE. Designed and first run by the cloud seat (`outside_bench/memos/THE_SENSE_CENSUS.md`, `certificates/sense_census.py`,
2026-09-08); re-implemented independently on main in B1305 (`b1305_sense_census.py`, all fourteen counts reproduced on the cloud's
tree) and NOT ADOPTED twice because the negative control failed on main -- each time through files that DOCUMENT the instrument
("logarithmic CFT" in this bench's own DESIGN, hint row and generated views). B1307's third pre-registration fixed two routes and
both passed: (A) the SELF-NAMING EXCLUSION -- every prose file whose text names the instrument is dropped at run time -- on HEAD;
(B) the unmodified census on the last pre-instrument commit (31dd52b9). Route A is what this file runs.

THE QUESTION. For every occurrence of a term in the prose (.md/.tex under frontier/ docs/ papers/; the cloud's `outside_bench`
excluded), does a marker of the technical sense occur within +-WINDOW characters?  A term present >= 5 times with < 2 % technical
contexts is FALSE COMFORT (the word is in the corpus, the concept is not); < 10 % is THIN; else GENUINE.  Two-sided control: the
positive term (`Chern-Simons`) must read GENUINE and the negative terms (`logarithmic`, `non-semisimple`: the sigma-bridge
literature the corpus never engaged) must read FALSE COMFORT, or the instrument is void on this tree. `--selftest` plants the
three MB12 controls on a scratch copy of docs/. A research instrument, not a gate: it answers register questions 8 and 10 of
FRESH_EYES_2026-09; it changes no verdict by itself.

Usage: sense_census.py [<tree-root>] [--selftest] [--json PATH] [--term TERM --marker REGEX]...
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
WINDOW = 130
CASES = [("logarithmic", r"\bCFT\b|\bVOA\b|Virasoro|vertex algebra|primary field", "neg"),
         ("non-semisimple", r"tensor categ|\bTQFT\b|modular categ|fusion", "neg"),
         ("character", r"\bVOA\b|Virasoro|vertex algebra|q-series|conformal", None),
         ("modular", r"tensor categ|S-matrix|\bVOA\b|fusion", None),
         ("non-rational", r"\bCFT\b|\bVOA\b|vertex algebra", None),
         ("resurgence", r"Borel|Stokes|transseries", None),
         ("Chern-Simons", r"\bCS\b|level|action|invariant", "pos")]
SELF_NAME_RE = re.compile(r"sense[ _-]?census", re.I)     # a file that names the instrument documents it; never scanned
SKIP_DIRS = ("outside_bench", ".git", "__pycache__")
PROSE_ROOTS = ("frontier", "docs", "papers")


def prose(root):
    kept, excluded = [], []
    for base in PROSE_ROOTS:
        for dp, dns, fns in os.walk(os.path.join(root, base)):
            dns[:] = sorted(d for d in dns if d not in SKIP_DIRS)
            for f in sorted(fns):
                if not f.endswith((".md", ".tex")):
                    continue
                p = os.path.join(dp, f)
                try:
                    txt = open(p, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                (excluded if SELF_NAME_RE.search(txt) else kept).append((p, txt))
    return kept, sorted(os.path.relpath(p, root) for p, _ in excluded)


def census(root, cases=CASES):
    files, excluded = prose(root)
    size = sum(len(t) for _, t in files)
    res = {}
    for term, marker, kind in cases:
        tre = re.compile(re.escape(term), re.I); mre = re.compile(marker, re.I); tot = hit = 0
        for _, t in files:                       # per file: a window never crosses a file boundary
            for m in tre.finditer(t):
                tot += 1
                if mre.search(t[max(0, m.start() - WINDOW): m.end() + WINDOW]):
                    hit += 1
        frac = hit / tot if tot else 0.0
        verdict = "FALSE COMFORT" if (tot >= 5 and frac < 0.02) else ("thin" if frac < 0.10 else "genuine")
        res[term] = dict(occurrences=tot, technical=hit, frac=round(frac, 4), verdict=verdict, kind=kind)
    return dict(files=len(files), excluded=excluded, mb=round(size / 1e6, 1), terms=res)


def two_sided(res):
    pos = [v for v in res["terms"].values() if v["kind"] == "pos"]
    neg = [v for v in res["terms"].values() if v["kind"] == "neg"]
    return all(v["verdict"] == "genuine" for v in pos), all(v["verdict"] == "FALSE COMFORT" for v in neg)


def planted(root):
    """three MB12 controls on a scratch copy of docs/: +1 with a marker counts, +1 without does not, a marker outside the window does not"""
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(root, "docs"), os.path.join(tmp, "docs"))
    for d in ("frontier", "papers"):
        os.makedirs(os.path.join(tmp, d))
    base = census(tmp)["terms"]["logarithmic"]

    def plant(text):
        p = os.path.join(tmp, "docs", "PLANTED.md"); open(p, "w").write(text)
        r = census(tmp)["terms"]["logarithmic"]; os.remove(p); return r
    a = plant("x " * 50 + "a logarithmic CFT appears here " + "x " * 50)
    b = plant("x " * 50 + "the logarithmic derivative of the volume " + "x " * 50)
    c = plant("logarithmic " + "y " * 70 + "CFT")
    ok = (a["technical"] == base["technical"] + 1 and a["occurrences"] == base["occurrences"] + 1
          and b["technical"] == base["technical"] and b["occurrences"] == base["occurrences"] + 1
          and c["technical"] == base["technical"] and c["occurrences"] == base["occurrences"] + 1)
    shutil.rmtree(tmp)
    return dict(base=base, with_marker=a, no_marker=b, marker_outside_window=c, ok=ok)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=str(ROOT))
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--term", action="append", default=[])
    ap.add_argument("--marker", action="append", default=[])
    a = ap.parse_args()
    if a.selftest:
        pl = planted(a.root)
        print(f"  sense-census selftest: planted +marker {pl['with_marker']['technical'] - pl['base']['technical']:+d}, "
              f"no marker {pl['no_marker']['technical'] - pl['base']['technical']:+d}, outside window "
              f"{pl['marker_outside_window']['technical'] - pl['base']['technical']:+d} -> {'PASS' if pl['ok'] else 'FAIL'}")
        return 0 if pl["ok"] else 1
    cases = list(CASES) + [(t, m, None) for t, m in zip(a.term, a.marker)]
    res = census(a.root, cases); okp, okn = two_sided(res)
    print(f"  sense-census on {a.root}: {res['files']} prose files ({res['mb']} MB); {len(res['excluded'])} self-naming file(s) excluded")
    for term, v in res["terms"].items():
        print(f"    {term:<18}{v['occurrences']:>8}{v['technical']:>8} ({v['frac']*100:5.1f}%)  {v['verdict']}" + (f"   [{v['kind']}]" if v["kind"] else ""))
    print(f"    control + (Chern-Simons genuine): {'PASS' if okp else 'FAIL'}; control - (logarithmic, non-semisimple false comfort): "
          f"{'PASS' if okn else 'FAIL'}; TWO-SIDED: {'PASSED' if okp and okn else 'FAILED -- the instrument is VOID on this tree; read nothing from it'}")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(dict(root=a.root, census=res, two_sided=okp and okn), indent=1), encoding="utf-8")
    return 0 if (okp and okn) else 1


if __name__ == "__main__":
    sys.exit(main())
