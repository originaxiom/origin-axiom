# W3-188r (H114 kappa-naming: tiers) -- wave-2 carry, corrected patch proposal
(PATCH PROPOSAL ONLY; no banked file edited. `cc`, the merge gate, applies at its discretion.)

## What this cell fixes

Wave-2 cell `W2-188` (`frontier/B771_phase1_wave1/cells/W2-188/`) explicitly marked TIER
out of scope for its own re-derivation (its `compute.py` line ~282: *"tier omitted here --
tier needs the interaction-form Galois-channel computation, out of scope for kappa_q
re-derivation"*), and yet its "READING" narration and its **Patch 6** (a proposed edit to
the flagship paper, `papers/P4_markov_stage/DRAFT_v8.md` S4.1) then went on to assert
specific tier labels anyway:

> "(2,6)=15dark vs (4,6)=15dark [same], (2,12)=15dark vs (4,12)=15qrs [DIFFERENT TIER,
> same value] ... **the tier at gx=4 is invisible** ... **They first diverge in tier at
> gy=12**"

This is a hand-read value dressed as a computed one, headed straight into the flagship
paper. This cell (W3-188r) locates the paper's ACTUAL tier definition and printed table
(S4.3, Theorem G(ii) -- NOT S4.1's 5x5 value sample, which W2-188 conflated it with),
computes every one of the 240 order-torus points' tiers from the interaction-form
definition itself via two independent code routes, and adjudicates the W2-188 claims
against the computed truth. Full derivation and every assertion: `compute.py` /
`output.txt` in this cell dir.

## Computed result (the discriminating fact)

* The paper's own printed S4.3 36-cell table is **exactly correct** -- 0/36 disagreements
  against a from-scratch recomputation (exact cyclotomic arithmetic, cross-checked by an
  independent floating-point route with 4-fold Galois averaging, max error 3e-14; a
  vacuity self-test with a corrupted construction produces 40/240 mismatches, confirming
  the diff check is discriminating, not tautological). **No paper edit is needed for
  S4.3.**
* The gx=2 vs gx=4 row comparison (the actual object of the H114 "missing-4" orphan),
  computed exactly for all 6 gy in {1,2,3,4,6,12}:

  | gy | gx=2 (val,tier) | gx=4 (val,tier) | tier same? |
  |----|------------------|------------------|------------|
  | 1  | (3, free)   | (3, free)   | yes |
  | 2  | (3, free)   | (3, dark)   | **no** |
  | 3  | (15, dark)  | (15, dark)  | yes |
  | 4  | (3, dark)   | (3, free)   | **no** |
  | 6  | (15, qrs)   | (15, dark)  | **no** |
  | 12 | (15, dark)  | (15, qrs)   | **no** |

  Tiers agree at gy in {1,3} and differ at gy in {2,4,6,12} -- **4 of the 6** gy-columns
  show a tier difference. W2-188's specific claims are wrong on two counts: (i) the cell
  (gx=2,gy=6) is **qrs**, not dark as claimed; (ii) the rows do NOT "first diverge in
  tier at gy=12" -- they first diverge at **gy=2** (and again at gy=4), gy=12 is actually
  the *last* of four divergent columns, not the first or only one.

## Patch -- papers/P4_markov_stage/DRAFT_v8.md (S4.1, lines 414-426): the missing-4
cross-reference, CORRECTED (supersedes W2-188's Patch 6; that patch should NOT be
applied as written -- see the two wrong claims above)

**File:** `papers/P4_markov_stage/DRAFT_v8.md`
**Lines:** 414-426

**OLD (current banked text, unchanged since before W2-188):**
```
### 4.1 The commutator table

tr[W₁ʲ, W₂ˡ], 1 ≤ j, l ≤ 5 (exact in ℚ(ζ₆₀); verified in three independent lifts —
the commutators are lift-independent by Proposition 4.0):

|      | l=1 | l=2 | l=3 | l=4 | l=5 |
|------|-----|-----|-----|-----|-----|
| j=1  | −1  | 3   | −5  | 3   | −1  |
| j=2  | 3   | 3   | 15  | 3   | 3   |
| j=3  | −1  | 3   | −5  | 3   | −1  |
| j=4  | 3   | 3   | 15  | 3   | 3   |
| j=5  | −5  | 15  | −5  | 15  | −5  |
```

**NEW:**
```
### 4.1 The commutator table

tr[W₁ʲ, W₂ˡ], 1 ≤ j, l ≤ 5 (exact in ℚ(ζ₆₀); verified in three independent lifts —
the commutators are lift-independent by Proposition 4.0). **Row j=4 is IDENTICAL to
row j=2 in this 5×5 sample; this is a computed coincidence of the divisor-lattice
census of S4.3, not a duplication: rows j=2 and j=4 are the DISTINCT lattice points
gx=gcd(2,20)=2 and gx=gcd(4,20)=4 (ord(W₁)=20), which merely agree on VALUE (not on
tier — see S4.3) at every gy = gcd(l,12) sampled here (l=1..5, i.e. gy∈{1,2,3,4,1}).
The two rows' TIER already diverges within this very sample: (gx=2,gy=2)=free vs
(gx=4,gy=2)=dark, and again at gy=4: (gx=2,gy=4)=dark vs (gx=4,gy=4)=free. Two more
divergences occur outside the 5×5 window, at gy=6 ((gx=2,gy=6)=qrs vs (gx=4,gy=6)=dark)
and gy=12 ((gx=2,gy=12)=dark vs (gx=4,gy=12)=qrs). Of the full 36-cell lattice's six
gy-columns for gx∈{2,4}, tier AGREES only at gy∈{1,3} and DIFFERS at gy∈{2,4,6,12} —
four of six. Computed exactly (exact cyclotomic construction, cross-checked by an
independent floating-point route with 4-fold Galois averaging to <1e-13; 0/36
disagreements against this section's own S4.3 table), B771 Phase-1 Wave-3, W3-188r.**

|      | l=1 | l=2 | l=3 | l=4 | l=5 |
|------|-----|-----|-----|-----|-----|
| j=1  | −1  | 3   | −5  | 3   | −1  |
| j=2  | 3   | 3   | 15  | 3   | 3   |
| j=3  | −1  | 3   | −5  | 3   | −1  |
| j=4  | 3   | 3   | 15  | 3   | 3   |
| j=5  | −5  | 15  | −5  | 15  | −5  |
```

---

## Note on W2-188's other patches

Only W2-188's **Patch 6** contains a tier claim (the rest -- Patches 1,2,3,4,5,7 -- are
either pure value/identity re-derivations already independently confirmed by W2-188's
own `compute.py` (Parts 0-3, no tier language) or a HINT_LEDGER status line with no
specific tier assertion). Those patches are not touched here; only Patch 6 is superseded.
The recommended merge action for `cc` is: apply W2-188's Patches 1-5 and 7 as proposed,
and apply THIS cell's corrected S4.1 patch in place of W2-188's Patch 6.

## Residual (named, not silently dropped)

This cell only computed and adjudicated the TIER claims (the wave-2 carry's stated
scope). It does not re-litigate W2-188's Parts 0-3 (kappa-naming identity, the half-chain
3-phase quasi-invariant, the silent-word field shadows) -- those were value-only claims,
already independently re-derived in W2-188/compute.py with no tier language, and are not
implicated in the defect this cell was asked to fix.
