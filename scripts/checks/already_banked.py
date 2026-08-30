#!/usr/bin/env python3
"""ALREADY-BANKED? -- the pre-flight check against the finished-but-forgotten class.

MANDATORY before writing MISSING / OPEN / "never run" / "no successor" about anything.

Four times the record has been called open when it was already proved (QP-1/B762;
L187's stabilizations/B767; the F2-F8 locks/B1003; R5's proof/B775+B778). Every one
of those would have been caught by searching the CORPUS rather than the REGISTER.
The register is a summary; the corpus is the record. This searches the corpus.

    python3 scripts/checks/already_banked.py "quine self-naming"
    python3 scripts/checks/already_banked.py dark hyperbola N=p^2
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SETTLED = {"PROVED", "NEGATIVE", "RESOLVED", "RESOLVED-A", "THEOREM", "RETRACTED"}


def _terms(argv):
    raw = " ".join(argv).lower()
    return [t for t in re.split(r"[^a-z0-9_^+\-/()=]+", raw) if len(t) > 2]


def scan(terms, exclude=()):
    """exclude: arc-name substrings to skip. A self-documenting instrument quotes its
    own test phrases, so its arc matches them -- excluding it is honesty, not evasion."""
    hits = []
    for vp in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(vp.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        if any(x in vp.parent.name for x in exclude):
            continue
        blob = json.dumps(d).lower()
        n = sum(1 for t in terms if t in blob)
        if n:
            hits.append((n, d.get("verdict", "?"), vp.parent.name,
                         (d.get("claim_one_line") or "")[:220]))
    # the cheap surfaces too: cell-level findings inside arcs (where B775/B778 lived)
    for fp in sorted(ROOT.glob("frontier/*/**/FINDINGS.md")):
        if any(x in str(fp) for x in exclude):
            continue
        try:
            txt = fp.read_text(encoding="utf-8", errors="ignore").lower()
        except Exception:
            continue
        n = sum(1 for t in terms if t in txt)
        if n >= max(2, len(terms) - 1):
            head = fp.read_text(encoding="utf-8", errors="ignore").splitlines()[:2]
            hits.append((n, "FINDINGS", str(fp.relative_to(ROOT)), " ".join(head)[:220]))
    hits.sort(key=lambda h: -h[0])
    return hits


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    argv = [a for a in sys.argv[1:] if not a.startswith("--exclude=")]
    exclude = tuple(a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--exclude="))
    terms = _terms(argv)
    hits = scan(terms, exclude)
    # An instrument that cries wolf gets ignored: a settled arc only counts as a
    # WARNING if it matches a real share of the query, not one incidental word.
    need = max(2, (len(terms) + 1) // 2)
    settled = [h for h in hits if h[1] in SETTLED and h[0] >= need]
    print(f"already-banked: terms {terms}")
    print(f"  {len(hits)} corpus hits; {len(settled)} SETTLED arcs matching >= {need} of {len(terms)} terms")
    for n, verdict, where, claim in hits[:12]:
        mark = "***" if verdict in SETTLED else "   "
        print(f"  {mark} [{n:>2} terms] {verdict:<9} {where}")
        if claim:
            print(f"           {claim}")
    if settled:
        print("\n  *** SETTLED ARCS EXIST FOR THESE TERMS. Read them BEFORE writing MISSING/OPEN.")
        return 1
    print("\n  no settled arc matched -- a MISSING/OPEN claim is admissible (state the terms you searched).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
