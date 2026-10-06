#!/usr/bin/env python3
"""LOAD BEARING -- the record behind LOAD-BEARING MATHEMATICS IS RE-DERIVED BY OWN CODE, EVEN WHEN PUBLISHED (WORKING_RULES,
2026-10-06).  The owner, verbatim: "we should verify all load bearing math even if a published paper, because we cant bet our
whole project against some possible errors bugs or mistakes".

An input is load-bearing when a verdict, a count, a cap, an identification or a headline changes if the input is false: a
theorem or lemma (from a paper, a textbook or another arc), a table or census value, or a library's output.  Each one is either
re-derived by the arc's own code, on the instances the arc uses, or carried as a hypothesis of the verdict.  A citation alone
supports nothing.

    python3 scripts/checks/load_bearing.py --check frontier/BNNNN_x/arc_verdict.json
    python3 scripts/checks/load_bearing.py --selftest

THE RECORD (arc_verdict.json, required from B1542 on; tests/test_arc_verdict_schema.py calls validate() below):

  "load_bearing": [
    {"id": "LB1", "input": "<the statement used>", "source": "<paper with section, arc, library, or census>",
     "status": "VERIFIED" | "CONDITIONAL",
     "check": "<repo path of the own code that re-derives it>",          (VERIFIED)
     "how": "<what that code computes, on which instances>",            (VERIFIED)
     "why": "<why it is not re-derived>"},                              (CONDITIONAL)
    ...]

  VERIFIED     own code re-derives the input on every instance the verdict uses, by a route that does not assume it (a second
               presentation, a direct enumeration, exact arithmetic, or several primes), and the check is in the repo.
  CONDITIONAL  not re-derived; the entry's id must appear in scope.hypotheses, so the verdict is read as conditional on it.

THIS INSTRUMENT CHECKS THE FORM OF THE RECORD AND THAT EACH CHECK EXISTS; WHETHER THE CHECK IS ADEQUATE STAYS WITH THE SEAT AND
ITS REVIEWERS.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
STATUSES = ("VERIFIED", "CONDITIONAL")
_ID = re.compile(r"^LB\d+$")


def validate(block, scope=None, root=ROOT):
    """Problems with a load_bearing block, as a list of strings (empty means well formed)."""
    if not (isinstance(block, list) and block):
        return ["load_bearing must be a non-empty list (an arc with no load-bearing input says so in one entry)"]
    p, seen = [], set()
    hyps = " ".join(h for h in ((scope or {}).get("hypotheses") or []) if isinstance(h, str))
    for i, e in enumerate(block):
        if not isinstance(e, dict):
            p.append(f"entry {i} must be an object")
            continue
        eid = e.get("id")
        if not (isinstance(eid, str) and _ID.match(eid)) or eid in seen:
            p.append(f"entry {i}: id must be a unique LB<n>")
        seen.add(eid)
        for k in ("input", "source"):
            if not (isinstance(e.get(k), str) and e[k].strip()):
                p.append(f"{eid}: {k} is required")
        st = e.get("status")
        if st not in STATUSES:
            p.append(f"{eid}: status must be one of {STATUSES}")
        elif st == "VERIFIED":
            chk = e.get("check")
            if not (isinstance(chk, str) and chk.strip()):
                p.append(f"{eid}: VERIFIED needs the check's repo path")
            elif not (root / chk).is_file():
                p.append(f"{eid}: the check {chk} is not a file in the repo")
            if not (isinstance(e.get("how"), str) and e["how"].strip()):
                p.append(f"{eid}: VERIFIED needs how the check re-derives it")
        else:
            if not (isinstance(e.get("why"), str) and e["why"].strip()):
                p.append(f"{eid}: CONDITIONAL needs a why")
            if not re.search(rf"\b{re.escape(str(eid))}\b", hyps):
                p.append(f"{eid}: a CONDITIONAL input must be named in scope.hypotheses")
    return p


def _selftest():
    good = [{"id": "LB1", "input": "x", "source": "y", "status": "VERIFIED", "check": "scripts/checks/load_bearing.py",
             "how": "z"},
            {"id": "LB2", "input": "x", "source": "y", "status": "CONDITIONAL", "why": "w"}]
    assert validate(good, {"hypotheses": ["conditional on LB2"]}) == []
    assert validate(good, {"hypotheses": []}), "an unnamed CONDITIONAL input passed"
    assert validate([]), "an empty record passed"
    assert validate([dict(good[0], check="no/such/file.py")]), "a missing check passed"
    assert validate([dict(good[0], status="TRUSTED")]), "an unknown status passed"
    assert validate([good[0], dict(good[0])]), "a repeated id passed"
    assert validate([{k: v for k, v in good[0].items() if k != "how"}]), "a VERIFIED entry without how passed"
    print("load_bearing selftest: ok")


def main():
    a = sys.argv[1:]
    if "--selftest" in a:
        _selftest()
        return 0
    if "--check" in a:
        d = json.loads(pathlib.Path(a[a.index("--check") + 1]).read_text())
        probs = validate(d.get("load_bearing"), d.get("scope"))
        for e in d.get("load_bearing") or []:
            if isinstance(e, dict):
                print(f"{e.get('id')}  {e.get('status')}  {e.get('input')}")
        print("\n".join(probs) if probs else "well formed")
        return 1 if probs else 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
