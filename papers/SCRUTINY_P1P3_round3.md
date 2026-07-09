# P1/P3 re-panel (round 3) — the iteration is not converging (2026-07-09)

**Round 3 (P1 v4 / P2 v3 / P3 v4) found 16 confirmed defects (P1:5, P2:6, P3:5). Several are NEW —
introduced by the v4/v3 "careful, per-fix-verified" rework itself, despite per-fix computation. The
decisive meta-fact: three correction rounds, each fixed the prior round's defects and introduced fresh
ones. Solo iteration is not converging. Recommendation: STOP patching; freeze P1–P3 as internal notes
/ specialist-track. P4 remains the only clean paper. The underlying mathematics is safe in the B-nodes.**

## NEW defects I introduced while "correcting" (the pattern, now undeniable)
- **P1 [MAJOR] "the raw trace is a degree-8 element at all 49 points"** (my v4 line). FALSE: the degree
  distribution over ℚ is {deg 4: 3 points, deg 8: 28, deg 16: 18}. At 18 points the raw trace generates
  *all* of ℚ(ζ₆₀) (degree 16, the opposite of "degree 8"). The correct reason to project is that the
  raw trace is *not in* ℚ(√5,√−3) — not that it is "degree 8" (and not "because non-real", since
  ℚ(√5,√−3) is itself non-real). A precisely-quantified false claim, freshly manufactured in the fix.
- **P3 [MAJOR] "degenerate d = 4, 6"** (my v4 §6). FALSE: d=6 has τ_6 = 2cos(2π/6) = 1 (rational,
  Δ_6 = −7 ≠ 0) — NON-degenerate, giving ℚ(√−7). Degeneracy (τ_d = 0) fails only at d=4. I conflated
  "τ_d rational" (d=3,6,…) with "degenerate" (d=4 only).
- **P3 [MAJOR] §6 "the torsion … no more and no less"** reasserts the ⊆ ("exactly") direction that F7
  was rewritten in v4 to disclaim — internal contradiction left in the same section.
- **P3 [MINOR] "a degree-4 field over ℚ(√5)"** is ambiguous/wrong: that reads as degree 8 over ℚ. The
  field is degree 4 over ℚ, degree 2 over ℚ(√5). Should be "degree-4 field (over ℚ) with quadratic
  subfield ℚ(√5)".
- **P2 [MINOR] "sharing no subfield with the parent"** — literally false (both contain ℚ). Need "no
  common subfield beyond ℚ".
- **P1 [MINOR] the 54/70 dark-closure count IS reproduced** by cross_table.py (B474) — so my v4 "flag
  as needing its own reproducer / not yet reproduced" over-corrected in the *other* direction.

## Pre-existing defects the earlier panels missed (real, not mine)
- **P1 [MAJOR] Theorem S2 (σ₁ = σ₂ = 1/24)** — σ₁, σ₂ are never defined, no reproducer computes them,
  and the one natural seam realization (rational channel of s(0,0)) is pair-dependent (1/24 for (1,2),(3,4);
  0, −1/40, 5/72 for others) — contradicting "independent of the pair." An undefined, unreproduced
  "theorem" with a decorative c/24 gloss. Delete or fully define+reproduce.
- **P1 [MAJOR] S7 dark locus** lives on the dual (x,y) torus while closure [W₁ʲ,W₂ˡ]=I lives on the
  exponent (j,l) torus; the 54/70 rests on a point-wise (x,y)≡(j,l) identification that §1 explicitly
  warns against — asserted, not derived (the gcd-cell factorization is fine; the point-wise intersection is not).
- **P2 [MAJOR] "≤ one bit" is a tautology, not a theorem** — a collision is *defined* as the same
  unoriented child, so every invariant of the unoriented child is shared by construction; orientation
  being the only possible difference is definitional, not a result. The whole thesis needs this stated honestly.
- **P2 [MINOR]** universal wording ("completely / entirely / the family") on one trace-field computation;
  the 5₂ parent's field is the *cubic* x³−x−1 (so "no quadratic" is the wrong frame for that parent);
  "four vacua" is asserted without an in-text definition.
- **P3 [MINOR] "the Markov prime 3"** — 3 is not a Markov number (1,2,5,13,29,…); it is the *coefficient*
  of the Markov cubic x²+y²+z² = 3xyz. Mislabel.

## The verdict (honest, and I am not going to launch round 4)
Three rounds; each round my corrections fixed the prior findings and introduced new ones — round 3's own
crop includes ≥5 defects manufactured by the v4 fix, despite per-fix computation. The evidence is now
conclusive: **I verify numbers reliably and prose statements unreliably, and solo iteration on these
write-ups does not converge.** Continuing to patch is the definition of the mistake. Decision (pending
owner): **freeze P1–P3 as clearly-marked internal notes** ("contains framing errors; NOT publication-
ready; the verified computations live in the cited B-nodes"), or route to a **specialist** who states the
theorems. P4 stands (it cleared this gauntlet clean, twice). The mathematics is not in question — every
underlying number reproduces; the failure is entirely in my rendering of it into paper prose. All three
scrutiny rounds are banked; nothing is lost by stopping here.
