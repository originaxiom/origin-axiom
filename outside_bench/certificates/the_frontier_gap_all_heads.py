#!/usr/bin/env python3
"""THE FRONTIER GAP, AGAINST **EVERY** HEAD -- the instrument #34 demanded and
that `the_branch_gap.py` did not supply.

No seal: this cell ASSERTS NOTHING NEW.  It is the anti-rediscovery instrument,
rebuilt after it failed a third time.

WHY IT EXISTS.  `the_branch_gap.py` diffs this branch against ONE sibling
(`origin/claude/paper-verification-ufp0zn`).  #34 was minted as

    "Diff the frontier against EVERY head before calling anything unrun."

and then NOT BUILT INTO THE TOOL.  On 2026-09-14 the reopened-G2-hatch cell was
sealed and run against a question that `origin/claude/standard-model-derivation-0qt6ao`
had already answered in B1353 -- a head this bench had never diffed, carrying 18
arcs absent here.  A rule that lives in a memo and not in an instrument is not a
rule.  This is that rule, in an instrument.

Stdlib + git only.  Usage:
    python3 the_frontier_gap_all_heads.py                  # full gap report
    python3 the_frontier_gap_all_heads.py TERM [TERM ...]  # + grep the gap arcs
"""
from __future__ import annotations

import json
import re
import subprocess
import sys


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def git(*a, check=True):
    r = subprocess.run(["git"] + list(a), capture_output=True, text=True)
    if r.returncode != 0:
        if check:
            raise RuntimeError(f"git {' '.join(a)}: {r.stderr.strip()}")
        return ""
    return r.stdout


def heads():
    out = []
    for ln in git("branch", "-r", "--format=%(refname:short)").splitlines():
        ln = ln.strip()
        if ln and "->" not in ln:
            out.append(ln)
    return sorted(out)


def arcs_of(ref):
    """The set of frontier arc DIRECTORIES on `ref` (not files -- R144's lesson:
    `ls frontier | wc -l` counts loose files and overcounts)."""
    s = set()
    for p in git("ls-tree", "-r", "--name-only", ref, "--", "frontier",
                 check=False).splitlines():
        m = re.match(r"^frontier/(B\d+[^/]*)/", p)
        if m:
            s.add(m.group(1))
    return s


def arc_num(a):
    m = re.match(r"^B(\d+)", a)
    return int(m.group(1)) if m else -1


def verdict_of(ref, arc):
    try:
        d = json.loads(git("show", f"{ref}:frontier/{arc}/arc_verdict.json"))
    except Exception:
        return "-", ""
    return d.get("verdict", "?"), (d.get("claim_one_line") or "")


def main():
    terms = [t.lower() for t in sys.argv[1:]]
    me = git("rev-parse", "--abbrev-ref", "HEAD").strip()
    mine = arcs_of("HEAD")

    rule("HEADS AND THEIR FRONTIER SIZE")
    hs = heads()
    per = {}
    for h in hs:
        per[h] = arcs_of(h)
        mx = max([arc_num(a) for a in per[h]] or [-1])
        print(f"  {h:<52s} arcs={len(per[h]):5d}   max=B{mx}")
    print(f"\n  THIS BRANCH ({me}): arcs={len(mine)}")

    union = set().union(*per.values()) if per else set()
    missing = union - mine

    rule("THE GAP -- arcs present on SOME head and ABSENT here")
    print(f"  union over all heads : {len(union)}")
    print(f"  present here         : {len(mine)}")
    print(f"  ABSENT HERE          : {len(missing)}")
    if not missing:
        print("\n  -> no gap.  Nothing on any head is missing from this branch.")

    # which head supplies each missing arc, and its verdict
    rows = []
    for a in sorted(missing, key=arc_num):
        src = [h for h in hs if a in per[h]]
        v, claim = verdict_of(src[0], a)
        rows.append((a, v, src, claim))

    rule("THE GAP, BY HEAD")
    bysrc = {}
    for a, v, src, _ in rows:
        bysrc.setdefault(" + ".join(h.split("/")[-1] for h in src), []).append(a)
    for k in sorted(bysrc):
        print(f"\n  [{k}]  ({len(bysrc[k])})")
        print("    " + " ".join(sorted(bysrc[k], key=arc_num)))

    rule("THE GAP, WITH VERDICTS")
    for a, v, src, claim in rows:
        print(f"  {v:<9s} {a}")
        if claim:
            print(f"            {claim[:150]}")

    if terms:
        rule("TERM SEARCH ACROSS THE GAP  (memo 153: state the terms with the claim)")
        print(f"  terms: {terms}\n")
        hit_any = False
        for a, v, src, claim in rows:
            body = claim.lower()
            for f in git("ls-tree", "-r", "--name-only", src[0],
                         "--", f"frontier/{a}", check=False).splitlines():
                if f.endswith(".md"):
                    body += "\n" + git("show", f"{src[0]}:{f}", check=False).lower()
            hits = [t for t in terms if t in body]
            if hits:
                hit_any = True
                print(f"  *** {v:<9s} {a}   [{len(hits)}/{len(terms)}] {hits}")
                print(f"      on {src[0]}")
                if claim:
                    print(f"      {claim[:220]}")
                print()
        if hit_any:
            print("  *** ARCS IN THE GAP MATCH THESE TERMS.  READ THEM BEFORE\n"
                  "      WRITING MISSING/OPEN OR SEALING A CELL ON THIS QUESTION.")
        else:
            print("  no arc in the gap matches these terms.")

    rule("WHAT THIS INSTRUMENT DOES NOT DO")
    print("""  It reports PER-ARC PRESENCE, not per-question coverage.  An arc present
  here may still have been superseded by an addendum on another head, and an
  absent arc may be irrelevant.  #35's lesson stands beside #34's: read an
  arc's OWN stated conclusion (FINDINGS + claim_one_line), not a listing and
  not a summary clause.  Absence from this report is not evidence a question
  is open.""")
    print()


if __name__ == "__main__":
    main()
