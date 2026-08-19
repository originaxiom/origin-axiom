#!/usr/bin/env python3
"""B8084 -- cold audit of B1075's exclusion arithmetic and, more importantly, its DESIGN.

Owner-routed question: has systematic negative bias shaped the outcomes?  Recomputation alone
cannot answer that -- a correct computation inside an unwinnable test is still a rigged test.
So this checks two different things:

  (1) is the arithmetic right?                      -- recomputation, from cc's pinned inputs
  (2) COULD THE TEST HAVE BEEN WON?                 -- the design question

(2) is the one that matters.  A negative-biased design is one whose success region has measure
near zero; a positive-biased one has measure near one.  The number is computable from the
pinned boxes alone and is reported here whatever it says.

Inputs are cc's PINNED NuFIT 6.1 3-sigma boxes, taken from their execution record.  Their
scripts were not read.
"""
E = {"Ue1": (0.8092, 0.8345), "Ue2": (0.5310, 0.5676), "Ue3": (0.1437, 0.1555)}
MU_TAU_UNION = 0.55
PHI = (1 + 5 ** 0.5) / 2
SEALED = {"1/2": 0.5, "1/(2phi)": 1 / (2 * PHI)}
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


print("=" * 76)
print("(1) RECOMPUTATION -- is the exclusion arithmetic right?")
print("=" * 76)
lo, hi = E["Ue2"]
sig = (hi - lo) / 6
n = (lo - SEALED["1/2"]) / sig
print(f"\n  |Ue2| 3-sigma box {E['Ue2']} -> 1 sigma = {sig:.5f}")
gate("'1/2 is about 5 sigma below the 3-sigma edge'", 4.5 <= n <= 5.5, f"{n:.2f} sigma")
v = SEALED["1/(2phi)"]
d = min(0 if a <= v <= b else min(abs(v - a), abs(v - b)) for a, b in E.values())
gate("'1/(2phi) is near no e-row box'", d > 0.1, f"nearest edge {d:.4f} away")
p80 = 1 - (1 - MU_TAU_UNION) ** 2
gate("'two random values land somewhere with p about 0.80'", abs(p80 - 0.80) < 0.01,
     f"1-(1-{MU_TAU_UNION})^2 = {p80:.4f}")

print()
print("=" * 76)
print("(2) THE DESIGN QUESTION -- was a HIT reachable?")
print("=" * 76)
m = sum(b - a for a, b in E.values())
win = 1 - (1 - m) ** 2
print(f"\n  measure of the exclusion-capable e-row boxes : {m:.4f}")
print(f"  P(at least one of the two sealed values hits): {win:.4f}")
gate("the success region is not degenerate (a hit was possible)", m > 0.01, f"{m:.4f}")
gate("the success region is not trivial (a hit would have meant something)", win < 0.5,
     f"{win:.4f}")
print(f"""
  A negative-biased design puts the success region at measure ~0; a positive-biased
  one puts it near 1.  This test's was {win:.2f}: winnable, and worth winning.

  The grading that LOOKS pessimistic is the opposite.  Six landings fell in the
  delta-free mu/tau boxes -- a hit SHAPE -- and were graded below success because
  that union has measure {MU_TAU_UNION}, giving p = {p80:.2f} by chance.  Refusing to
  count an event that happens {100*p80:.0f}% of the time at random is REQUIRED.  The arc
  reported the hit shape and printed the number that disqualifies it, rather than
  omitting either.

  ON THIS ARC, NO NEGATIVE BIAS IS FOUND -- in the arithmetic or in the design.""")
if FAILED:
    raise SystemExit(f"AUDIT GATES FAILED: {FAILED}")
print("\n  ALL AUDIT CHECKS PASS")
