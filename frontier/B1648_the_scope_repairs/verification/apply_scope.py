#!/usr/bin/env python3
"""B1648 -- apply Review 63's scope repairs to the verdict files and THE_WEAVE (P-120, P-121, P-122). Each edit asserts
its anchor is present exactly once and is idempotent-guarded (it refuses to apply twice)."""
import glob, json, os, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
TAG = "[Scoped at Review 63 (B1648, 2026-10-14):"


def verdict(b):
    return glob.glob(os.path.join(ROOT, "frontier", "%s_*" % b, "arc_verdict.json"))[0]


def _save(p, d, raw):
    out = json.dumps(d, indent=1)
    open(p, "w", encoding="utf-8").write(out + ("\n" if raw.endswith("\n") else ""))


def edit_claim(b, anchor, insert):
    p = verdict(b); raw = open(p, encoding="utf-8").read(); d = json.loads(raw); c = d["claim_one_line"]
    assert TAG not in c, (b, "already scoped"); assert c.count(anchor) == 1, (b, anchor)
    d["claim_one_line"] = c.replace(anchor, insert + anchor, 1); _save(p, d, raw)


def edit_field(b, key, old, new):
    p = verdict(b); raw = open(p, encoding="utf-8").read(); d = json.loads(raw); v = d["scope"][key]
    assert v.count(old) == 1, (b, key, old); d["scope"][key] = v.replace(old, new, 1); _save(p, d, raw)


# P-120: B1630's "never three distinct" holds where the inner automorphisms act
edit_claim("B1630", " 0 of 19.", " " + TAG + " the residual group of order 32 includes the inner automorphisms' lifts; on the ruled branch, where they are not moves, the residual at i is cyclic of order 8 and the lowest symmetric coupling O+ at k = 1 has three distinct masses (1, 1/phi, 1/phi^2) at i (B1634 P3, B1635 K5(ii), B1636)]")
# P-121: B1634's convention and post-seal headline; B1636 and B1638 for the record's hand
edit_field("B1634", "hypotheses", "the convention rho(g) = lift(g)^-1 forced by the lifts composing in reverse",
           "the convention rho(g) = lift(g)^-1, one of two reverse-composing homomorphisms (B1640: a convention, not forced)")
edit_claim("B1634", " The hand is not derived.]", " The identification with the multiplier of eta^21 (theta2^2, theta3^2, theta4^2), the sign diagnosis of B1632, the census at length 12 and the residuals are post-seal (P2-P6, labelled on the page).")
edit_claim("B1636", " 0 of 19.", " " + TAG + " for the record's hand only: under the conjugate hand the weight-1 symmetric space is empty (B1640 cell B); 'lowest' is weight 1 under the holomorphic modular-flavour ansatz]")
edit_claim("B1638", " 0 of 19.", " " + TAG + " the identity is unconditional; its reading as 'the weave's lowest coupling is golden' is for the record's hand under the holomorphic ansatz (B1640)]")
# P-122: B1641's agreement checked at Delta^4 alone; M_{1,2} the seat's reading
edit_claim("B1641", " 0 of 19.", " " + TAG + " 'the only lifts that agree with the ruled moves' rests on the Delta^4 check alone, coherence over Aut+(F2) being the Banking Seat's Gate 12 (P-074), still owed; 'the two objects are one' takes the weave's surface to be M_{1,2}, the SM seat's reading (W19, verified in part, B1624)]")

# P-120 on THE_WEAVE's B1630 bullet
p = os.path.join(ROOT, "docs", "THE_WEAVE.md"); s = open(p, encoding="utf-8").read()
old = "with the single on the clock's line: the line the\n  rule's word singled out."
assert s.count(old) == 1, "THE_WEAVE anchor"
s = s.replace(old, old + " *(Scoped at Review 63: where the inner automorphisms act. On the ruled branch the residual at\n  i is cyclic of order 8, and the lowest symmetric coupling there has three distinct masses, the golden ones; B1635,\n  B1636.)*", 1)
open(p, "w", encoding="utf-8").write(s)
print("applied")
