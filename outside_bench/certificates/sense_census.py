#!/usr/bin/env python3
"""THE SENSE CENSUS -- a term census that tells WHICH MEANING, not just presence.

THE DEFECT IT FIXES (found 2026-09-07, memo 171 addendum 2): a plain term census returns
FALSE COMFORT when a word is already in use with a different meaning. 'logarithmic' is present
in the corpus and every occurrence means 'logarithm of a number'; the corpus has never met
logarithmic CFT. memo 153's already_banked rule cannot see this, and the MORE MATURE the
corpus the likelier the collision -- a mature vocabulary is exactly what hides a missing one.

METHOD: for each occurrence take a +-130 character context and ask whether a marker pinning the
TECHNICAL sense appears in it. Present-but-never-technical = FALSE COMFORT.

SCOPE: prose only (.md/.tex) in frontier/ docs/ papers/. outside_bench/ is EXCLUDED -- this
bench's own memos now discuss these very terms and would contaminate the measurement.

Two-sided control is mandatory and reported first.  Gate 5: text only.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
WINDOW = 130
files = []
for base in ("frontier", "docs", "papers"):
    for dp, dns, fns in os.walk(os.path.join(ROOT, base)):
        dns[:] = [d for d in dns if d not in ("outside_bench", ".git")]
        files += [os.path.join(dp, f) for f in fns if f.endswith((".md", ".tex"))]
blob = "\n".join(open(f, encoding="utf-8", errors="replace").read() for f in files)
print(f"prose scanned: {len(files)} files, {len(blob)/1e6:.1f} MB   (outside_bench EXCLUDED)\n")

CASES = [
 ("logarithmic",    r"\bCFT\b|\bVOA\b|Virasoro|vertex algebra|primary field", "FALSE-COMFORT"),
 ("non-semisimple", r"tensor categ|\bTQFT\b|modular categ|fusion",            "FALSE-COMFORT"),
 ("character",      r"\bVOA\b|Virasoro|vertex algebra|q-series|conformal",    "?"),
 ("modular",        r"tensor categ|S-matrix|\bVOA\b|fusion",                  "?"),
 ("non-rational",   r"\bCFT\b|\bVOA\b|vertex algebra",                        "?"),
 ("resurgence",     r"Borel|Stokes|transseries",                              "?"),
 ("Chern-Simons",   r"\bCS\b|level|action|invariant",                         "GENUINE"),
]

print("=" * 78)
print(f"{'term':<16}{'occurrences':>12}{'technical sense':>18}   verdict")
print("=" * 78)
rows = []
for term, mk, expect in CASES:
    tre = re.compile(re.escape(term), re.I); mre = re.compile(mk, re.I)
    tot = hit = 0
    for m in tre.finditer(blob):
        tot += 1
        if mre.search(blob[max(0, m.start()-WINDOW): m.end()+WINDOW]): hit += 1
    frac = hit/tot if tot else 0.0
    v = "FALSE COMFORT" if (tot >= 5 and frac < 0.02) else ("thin" if frac < 0.10 else "genuine")
    rows.append((term, tot, hit, frac, v, expect))
    print(f"{term:<16}{tot:>12}{hit:>10} ({frac*100:>5.1f}%)   {v}"
          + (f"   [expected {expect}]" if expect != "?" else ""))

pos = [r for r in rows if r[5] == "GENUINE"]; neg = [r for r in rows if r[5] == "FALSE-COMFORT"]
ok_p = all(r[4] == "genuine" for r in pos); ok_n = all(r[4] == "FALSE COMFORT" for r in neg)
print()
print(f"CONTROL +  ({', '.join(r[0] for r in pos)}): " + ("PASSES" if ok_p else "FAILS -- misses a real technical use"))
print(f"CONTROL -  ({', '.join(r[0] for r in neg)}): " + ("PASSES" if ok_n else "FAILS -- missed a known collision"))
print("TWO-SIDED CONTROL: " + ("PASSED -- instrument usable" if (ok_p and ok_n) else "FAILED -- NOT ADOPTED"))
fl = [r[0] for r in rows if r[4] == "FALSE COMFORT"]; th = [r[0] for r in rows if r[4] == "thin"]
print(f"\nFALSE COMFORT (word present, concept never met): {fl or 'none'}")
print(f"THIN (<10% technical -- worth a human look): {th or 'none'}")
print("\nA flag means a \"we don't have X\" check on that term would have returned false comfort.")
