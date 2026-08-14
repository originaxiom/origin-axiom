#!/usr/bin/env python3
"""Derive a motif lexicon FROM the corpus, and diff it against the 18 authored terms.

B806 established that the atlas lexicon is 18 hand-authored regex sets, frozen 2026-07-01,
grounded in K001..K022, with 409 arcs banked since -- so an arc matching none of the 18 is
invisible by construction, and the instrument is self-sealing.

This derives candidate motifs from the 734 FINDINGS themselves. The gap against the 18 is the
closest available answer to "what did the programme learn and never name?"

WHAT THIS PRODUCES, STATED PRECISELY:

  CANDIDATES, NOT MOTIFS.

Two calibrations in this session already showed keyword methods over-predict badly on this
corpus: verdict classification scored 7/20 with three of those wrong, and face attachment scored
precision 0.45 / exact-set 13%, over-predicting by 55%. The same caution applies to THIS
extractor and is not exempted by having written it. Every candidate below needs reading before
it is called a motif.

METHOD
  - document frequency (how many ARCS mention a term), never raw count: a term repeated 200
    times in one arc is that arc's vocabulary, not a motif
  - a term is a candidate only if it recurs across MANY arcs but is NOT already matched by any
    of the 18 authored patterns
  - technical shapes only: multiword capitalised phrases, hyphenated compounds, math-ish tokens
"""
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

STOP = set("""the a an and or of to in is are was were be been for with that this these those
it its as at by on from not no nor but if then than so such which who whom what when where how
all any both each few more most other some only own same too very can will just should now
we our us they them their there here has have had do does did done being one two three
paper section theorem lemma proof result results verified computed banked arc note case
status date nothing claims gate firewall owner seat run runs ran see also per via etc
""".split())


def load_lexicon_patterns():
    """The 18 authored patterns, read from the atlas source itself."""
    src = open(os.path.join(ROOT, "scripts", "atlas", "atlas.py"), encoding="utf-8").read()
    pats = []
    for m in re.finditer(r"patterns=\[(.*?)\]", src, re.S):
        for p in re.findall(r'r?"([^"]+)"', m.group(1)):
            pats.append(p)
    return pats


def covered(term, pats):
    for p in pats:
        try:
            if re.search(p, term, re.I):
                return True
        except re.error:
            continue
    return False


def harvest():
    fdir = os.path.join(ROOT, "frontier")
    docs = {}
    for d in sorted(os.listdir(fdir)):
        m = re.match(r"(B\d+)[a-zA-Z]?_", d)
        fp = os.path.join(fdir, d, "FINDINGS.md")
        if m and os.path.isfile(fp):
            docs[m.group(1)] = open(fp, encoding="utf-8").read()
    return docs


def terms_of(text):
    """Technical shapes only: hyphenated compounds and capitalised/greek multiword phrases."""
    t = set()
    # hyphenated technical compounds: zero-intertwiner, gap-labeling, level-rank ...
    for w in re.findall(r"\b[a-zA-Z][a-zA-Z]+(?:-[a-zA-Z][a-zA-Z]+)+\b", text):
        w = w.lower()
        if len(w) > 6 and not any(p in STOP for p in w.split("-")):
            t.add(w)
    # single distinctive technical words (long, lowercase, not stopwords)
    for w in re.findall(r"\b[a-z]{7,}\b", text.lower()):
        if w not in STOP:
            t.add(w)
    return t


def main():
    pats = load_lexicon_patterns()
    docs = harvest()
    df = Counter()
    for txt in docs.values():
        for w in terms_of(txt):
            df[w] += 1
    n = len(docs)
    floor = max(20, int(0.03 * n))                 # must recur across >=3% of arcs
    cands = [(w, c) for w, c in df.most_common() if c >= floor and not covered(w, pats)]

    print("=" * 78)
    print("DERIVED LEXICON — candidates the 18 authored motifs do not cover")
    print("=" * 78)
    print(f"  arcs scanned: {n}   authored patterns: {len(pats)}   df floor: {floor} arcs")
    print(f"  distinct technical terms: {len(df)}   UNCOVERED and recurring: {len(cands)}")
    print(f"\n  {'term':34} {'arcs':>5}  {'% of corpus':>11}")
    for w, c in cands[:45]:
        print(f"  {w:34} {c:>5}  {c/n*100:>10.1f}%")
    out = {"floor": floor, "arcs": n, "candidates": cands}
    json.dump(out, open(os.path.join(ROOT, "scripts", "checks", "derived_lexicon.json"), "w"),
              indent=1, ensure_ascii=False)
    print(f"\n  CANDIDATES, NOT MOTIFS. Two calibrations this session showed keyword methods")
    print(f"  over-predict on this corpus (verdicts 7/20 with 3 wrong; faces precision 0.45).")
    print(f"  That caution applies to this extractor too. Read before naming.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
