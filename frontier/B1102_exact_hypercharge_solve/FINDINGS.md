# B1102 — THE EXACT HYPERCHARGE SOLVE: the landing carries the banked multiset EXACTLY (18 rational directions) — and no color-commuting direction can

**Status: banked (frontier). Verdict PROVED. Gate 5 untouched (the 6Y multiset is
B950's banked integer assignment — the same license B1100 ran under). Lock
`tests/test_b1102_exact_solve.py`. Prereg sealed BEFORE compute (criteria and outcome
grammar typed first; §CE scratchpad staging; the frozen text lands beside this file).**
Run: `python3 frontier/B1102_exact_hypercharge_solve/b1102_adapted_basis.py` then
`b1102_solve.py` from the repo root (~12 s total, fully exact).

## THE PRIZE FIRST — a two-sided theorem, both sides exhaustive

**Side 1 (C1 MATCH-EXACT: PASS).** The A2 landing's rank-4 Cartan carries the banked
6Y hypercharge multiset {1/6×6, 1/3×6, −1/2×4, −2/3×3, −1/3×3, 0×2, 1/2×2, 1×1}
**exactly** — by **18 isolated rational directions**, every denominator dividing 6,
representative **t = (1/6, 1/6, 2/3, −1/3)** in the adapted crystal Cartan. The search
is **provably complete**, not sampled: four of the fifteen exact weight classes are
±standard-basis vectors (all of size 3), so any solving direction is fully determined
by which of the five multiplicity-≥3 target values each of those four classes takes —
all 5⁴ = 625 assignments solved exactly, every candidate verified on all 27 values.
B1100's "exact value-match, the named residual" is **DONE, positively**.

**Side 2 (the sharpener, equally exhaustive).** **No color-commuting u(1) achieves the
values.** A direction commuting with a full su(3) factor must have zero component on
that factor's Cartan — and **zero of the 18 solutions are pure on either ideal**
(forced already at Cartan level; independently re-derived by the banking seat from the
stored data). Root-level confirmation: 36/36 exact checks (both ideals × all 18
solutions) negative. So at this landing, **the exact-valued U(1) necessarily mixes both
su(3) factors' Cartans**: the landing is **hypercharge-VALUED but not
SM-PRODUCT-structured** — a simultaneous unbroken su(3)_color ⊕ su(2) ⊕ u(1)_Y with
the banked values does not exist at the A2 stratum.

**The su(2) side (C3: PASS on its sealed text).** Every one of the 18 solutions has
exactly two Y-neutral roots (one per ideal — universal, checked 18/18). The su(2)
built from the non-color ideal's Y-neutral root satisfies the Chevalley relations
exactly on the full 27×27 representation, commutes with the ENTIRE other ideal and
with the solved Y exactly, and decomposes the 27 as **6 doublets + 15 singlets** (no
triplets — only eigenvalues −1, 0, 1 occur). Six doublets is trinification's doublet
count (3 quark + 3 lepton doublets per generation) at structure level.

**Uniqueness (C2).** Not unique and not a family: a zero-dimensional set of exactly
18. Priced as a bare choice: log₂ 18 ≈ 4.17 bits. An order-36 symmetry lead (which
would organize the 18 into orbits) was **not confirmed** — named open, not claimed.

## Fences and honest notes

- **Chirality-at-count is NOT claimed** (the standing fence, verbatim; THE LOCATION
  THEOREM stands).
- **A float-measure tension with B1100, flagged not resolved:** a fresh 20,000-trial
  float scan in THIS basis found zero degeneracy-pattern hits, while B1100's old-basis
  scan hit the pattern at trial 0. Both arcs' EXACT claims are unaffected (B1100's
  pattern-genericity was float-grade in its own basis; this arc's exact 18-point value
  set supersedes at value level). The pattern-cone's geometry deserves one clarifying
  check; it is queued, not settled here.
- **The adapted-basis win is real:** building the Cartan from the ideal split (crystal
  basis) made all four generators diagonal with small-integer spectra — the whole
  solve ran rational end-to-end; B1100's cubic-CRootOf fallback (named in the prereg)
  was never needed. One centralizer basis vector is genuinely mixed between the two
  ideals — handled, not assumed away.
- **Dependency, vendored:** the e₆ Chevalley bracket/basis convention the stored
  B1098 triple lives in (the paper-lineage verify module) is vendored into this arc
  as `e6_bracket_vendored.py` (provenance header carries the original's sha256), and
  the 27-representation built on it is **re-certified in-arc** (all C(78,2) Chevalley
  pairs, exact) — own certification, not inherited trust.

## Verification chain (verify-don't-trust, three layers)

1. **The compute bench** (independent agent, own scripts): synthetic pre-flight
   validation of the ideal-split machinery; a real `nsimplify` PSLQ hazard caught
   pre-flight and eliminated; stacked-kernel verification of the weight table
   (B1100's proven method) beside the direct diagonal read-off; modular rank
   cross-checks over two primes.
2. **Fresh end-to-end re-runs by the banking seat** (twice: once from staging, once
   in-tree against the vendored module): identical outputs, byte-for-byte on the
   result JSONs.
3. **Independent re-derivation of every verdict-bearing claim by the banking seat's
   own code**: all 18 directions reproduce the banked 27-multiset under an
   independent transcription of the target from B950's banked source; the
   completeness premise (exactly four ±basis-vector classes, all size 3, five
   admissible values) verified; the no-pure-direction fact (Side 2's Cartan-level
   force) re-derived directly from the stored solutions.
4. **Structural cross-anchor:** the 15 weight-class sizes [3×6, 1×9] match B1100's
   independently-computed table in a completely different (cubic-irrational) basis.

## What this changes, and the three named follow-ups (none claimed)

The hatch's door-status sentence sharpens on both sides: the landing carries the
Standard Model's own hypercharge **values** exactly (stronger than B1100's
pattern-compatibility), and the obstruction to the full SM product structure is now
**located precisely** — the color-commutation constraint and the exact values are
incompatible at this stratum. The typed follow-ups: (i) whether another sl₂ stratum
dissolves the incompatibility; (ii) whether a different identification of color
within the centralizer does; (iii) whether the banked 6Y frame (B950's cascade frame)
and the landing's frame differ by a map that reconciles the two sides. Three
questions, all computable, none asserted.
