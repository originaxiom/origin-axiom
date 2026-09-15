#!/usr/bin/env python3
"""CURRENCY PASS on this bench's own three gap documents (2026-08-28) against main @ the pin.
Seal: seals/GAP_DOCS_CURRENCY_PREREG.md.  Mechanical retrieval PROPOSES; the memo adjudicates
by reading.  Gate 5 untouched."""
import os, sys, re
PIN = "89affd5bbd4b900397af2bf3b987ff8f05f5cb80"
os.environ.setdefault("OA_REF", PIN)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _oa_source as OA
A = OA.arc_verdicts()
print(f"arcs at pin: {len(A)}")

# the documents' asserted-open items, extracted by hand and published in the memo
ITEMS = [
 ("N1","derived dynamics / equation of motion", r"equation of motion|derived dynamics"),
 ("N2","S1 -- the E6 Seiberg-Witten curve vs the banked A-polynomial", r"Seiberg-?Witten|SW curve"),
 ("N3","L154's E6-lattice boundary construction (the last live route to sigma=1)", r"E6-lattice|E6 lattice boundary|L154"),
 ("N4","the P^3 adjudication -- reduce or carry permanently", r"P\^?3|\bPP\(B_?0\)|projective Higgs|Higgs line"),
 ("N5","the 953 class-group step -- disc-6237 cubic field", r"6237|class[- ]group|h\(K\) *= *1"),
 ("N6","the 40639 leg of sin^2 theta_W", r"40639"),
 ("N7","the r-supply bridge -- grammar -> disc-48 Gauss-form swap", r"disc[- ]?48|r-supply"),
 ("N8","the branch->r identification + the (Vol,CS) clock-coherence run", r"clock[- ]coherence|branch.{0,12}r identification"),
 ("N9","the selection-theorem assembly for the twist", r"selection[- ]theorem"),
 ("F1","FENCED: S4 (the quine) UNBUILT", r"quine"),
 ("A2","cosmology's three blind rows -- zero dedicated arcs", r"dark matter|inflation|structure formation"),
 ("A3","the E6 boundary bridge -- characters to a record-side q-series", r"q-series|boundary bridge|graded character"),
 ("A6","S-A, the sufficiency criterion for the observer", r"sufficiency criterion|\bS-A\b"),
]
DOC_BAND = 1194   # the documents were written against the B1193/B1194 band, 2026-08-28

def num(k):
    m = re.match(r"B(\d+)$", k); return int(m.group(1)) if m else -1

print("\n" + "="*84)
print("MECHANICAL RETRIEVAL -- candidate closures per asserted-open item")
print("(arcs are split by whether they PREDATE the documents: a hit there means the item was")
print(" stale ON THE DAY IT WAS WRITTEN, which is a different defect from the corpus moving.)")
print("="*84)
for iid, label, pat in ITEMS:
    rx = re.compile(pat, re.I)
    hits = [(num(k), k, v.get("verdict"), v.get("claim_one_line") or "")
            for k, v in A.items() if rx.search(v.get("claim_one_line") or "")]
    hits = [h for h in hits if h[0] > 0]
    hits.sort()
    strong = [h for h in hits if h[2] in ("PROVED", "NEGATIVE")]
    pre  = [h for h in strong if h[0] <= DOC_BAND]
    post = [h for h in strong if h[0] >  DOC_BAND]
    print(f"\n{iid}  {label}")
    print(f"    PROVED/NEGATIVE arcs matching: {len(strong)}"
          f"   | predating the docs (<=B{DOC_BAND}): {[h[1] for h in pre][-6:]}"
          f"   | after: {[h[1] for h in post][:6]}")
    for h in (pre[-1:] + post[:1]):
        print(f"      {h[1]} {h[2]}: {' '.join(h[3].split())[:200]}")
print("\n" + "="*84)
print("This output is a DETECTOR'S OUTPUT, not a result. Every row above is adjudicated by")
print("reading in memos/GAP_DOCS_CURRENCY.md; rows the reading does not confirm are dropped.")
print("="*84)
