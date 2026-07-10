# B516 — the golden-3d ladder: reachable, NOT cap-selected, but golden-SPECIFIC (and why)
**Computed 2026-07-11, establishing ground around the B515 reopening. Two nearly-repeated
binary-scan errors caught (the §7 lesson, twice more). Lock `tests/test_b516.py`.**

## Finding 1 — 3d is NOT selected by a dimension cap (deflation, honest)
Golden-field Pisot inflation numbers exist at **dim 1** (φ), **dim 3** (β=φ(1+√φ), B515), AND **dim 5**
(found in the {0,1,2} coupling scan of three Fibonacci copies). The specific recursion x→x(1+√x) is
Pisot only at dims 1,3 (breaks at 7, conjugates 1.209>1) — but that is CONSTRUCTION-specific; other
couplings give golden order at dim 5. **So golden aperiodic order is not capped at 3; the "3 spatial
dimensions forced by a Pisot ceiling" reading is DEAD.** (Note: my binary-only scans falsely showed 0
golden at dim 3 AND dim 5 — corrected both times by rescanning {0,1,2}; the exact error that hid β.)

## Finding 2 — golden 3d IS golden-SPECIFIC, and the reason is φ's minimality (real ground)
Via self-reference x→x(1+√x), among the metallic family ONLY golden gives a PISOT number:
| metallic | x(1+√x) | Pisot? |
|---|---|---|
| **golden φ=1.618** | 3.676 | **YES** (→ β=φ(1+√φ), clean 3d) |
| silver 2.414 | 6.165 | NO |
| bronze 3.303 | 9.305 | NO |
| m=4  4.236 | 12.955 | NO |
**Mechanism (exact):** β's conjugates are x(1±√x) and x'(1±√x') (x'=−1/x the metallic conjugate). The
binding one is **x(√x−1)**: <1 for golden (φ(√φ−1)=0.440) but >1 for silver (1.337) and beyond. **φ is
the UNIQUE metallic number small enough (closest to 1) that self-reference stays quasicrystalline.**
Golden 3d is a privilege of the golden ratio's minimality — echoing the McKay ladder's golden-specificity.

## Net status of the D1 reopening (honest, tiered)
- **PROVEN:** golden 3d is real (β, B515) and golden-SPECIFIC (only φ among metallics, because it's the
  smallest — exact conjugate mechanism).
- **DEFLATED:** 3d is NOT dimension-selected (golden order at 1,3,5); "3 forced by a cap" is dead.
- **OPEN (the edge):** is the two-Fibonacci-copy bootstrap FORCED? and is silver's failure robust to
  ALL couplings (not just the recursion)? Firewalled; β through B398 only.
