#!/usr/bin/env python3
"""The supersession generator for the frozen tier (register row P-319; the building session's card C20, 2026-11-14).

The frozen paper P9 takes errata only, and the foundation changes only by its versions; both cite arcs. This lists, for
each arc a tier document cites, the later arcs that say something of it in words of supersession: a line of a later
arc's verdict line or page that names the cited arc together with one of the words below. It reads; it decides nothing.
Whether a citation is an error is main's to decide, arc by arc; an errata entry follows only that decision.

    python3 scripts/checks/supersession_tier.py            # P9 and GENESIS.md
    python3 scripts/checks/supersession_tier.py --p9       # P9 only

A text search: a successor that says so in other words is not seen, and a word of supersession on the same line as an
arc's name may be about another arc on that line. Each flag is a line to read, not a finding."""
import glob, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TIER = {"P9": "papers/P9_what_a_grammar_fixes/tex/sections/*.tex", "GENESIS": "GENESIS.md"}
WORDS = re.compile(r"\b(supersed\w*|re-?graded|correct(?:s|ed|ion)|refut\w*|retract\w*|withdrawn|scoped|narrow(?:s|ed))\b", re.I)
ARC = re.compile(r"(?<![\w:])B(\d{1,4})(?![\d\w])")


def cited(pattern):
    """the arc numbers a tier document cites"""
    out = set()
    for p in sorted(glob.glob(os.path.join(ROOT, pattern))):
        out |= {int(n) for n in ARC.findall(open(p, encoding="utf-8", errors="replace").read())}
    return out


def said_of():
    """{arc number: [(the later arc's number, where, the line)]} for every line of a verdict line or a page that names an
    arc of a lower number together with a word of supersession"""
    out = {}
    for v in glob.glob(os.path.join(ROOT, "frontier", "B*", "arc_verdict.json")):
        folder = os.path.dirname(v)
        m = re.match(r"B(\d+)_", os.path.basename(folder))
        if not m:
            continue
        me = int(m.group(1))
        texts = []
        try:
            texts.append(("verdict line", json.load(open(v, encoding="utf-8")).get("claim_one_line") or ""))
        except Exception:
            pass
        page = os.path.join(folder, "FINDINGS.md")
        if os.path.isfile(page):
            texts.append(("page", open(page, encoding="utf-8", errors="replace").read()))
        for where, text in texts:
            for line in re.split(r"(?<=[.;])\s+|\n", text):
                if not WORDS.search(line):
                    continue
                for n in {int(x) for x in ARC.findall(line)}:
                    if n < me:
                        out.setdefault(n, []).append((me, where, line.strip()[:240]))
    return out


def report(tiers, said=None):
    said = said_of() if said is None else said
    rows = []
    for name in tiers:
        for n in sorted(cited(TIER[name])):
            for later, where, line in sorted(set(said.get(n, []))):
                rows.append((name, n, later, where, line))
    return rows


if __name__ == "__main__":
    tiers = ["P9"] if "--p9" in sys.argv else ["P9", "GENESIS"]
    rows = report(tiers)
    for name, n, later, where, line in rows:
        print("%s cites B%d; B%d's %s: %s" % (name, n, later, where, line))
    print("%d line(s) to read, over %s" % (len(rows), " and ".join(tiers)))
