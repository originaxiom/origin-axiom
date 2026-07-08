# P4 panel round 2 — adjudication (structure seat complete; four seats re-queued)

**Round 2 ran on draft v4. The structure/clarity seat returned a full report (7 findings,
each verified in-session by the agent). The correctness, novelty, overclaim, and hostile
seats did not complete this pass and are re-queued — round 2 is therefore PARTIAL; the
draft is not yet panel-clean and does not advance to the owner voice pass until they run.**

## CONFIRMED — the two math errors (verified by CC this session; fixed in draft v5)

1. **[FATAL] The (2,3)-minimality clause was false as printed.** The draft said (2,3) is
   the minimal closure address "with both exponents nontrivial." But A₂⁶ ≡ 11·I (mod 15)
   is central and non-identity, so [A₁, A₂⁶] ≡ I (mod 15) — verified — making (1,6) a
   closure address with both exponents nonzero, lexicographically below (2,3). The §4.3
   master table (15-dark at gx=1, gy=6) already contradicted the §4.1 prose, which only
   sees the 5×5 window. **Fix (v5):** "nontrivial" → "non-central mod 15"; (2,3) is
   minimal among addresses whose BOTH powers are non-central. Abstract, §1, and F(iii)
   all corrected.

2. **[MAJOR] The Theorem E″ witness word was misprinted.** "LLLRRLRRRLLL′" has trace 73
   and is not rooted (a stray trailing letter/prime). The correct second rooted class at
   trace 146 is **LLLRRLRRRLLR** (balanced, non-word-mirror), verified with root
   X = [[1,3],[4,11]], det −1, X² = B, det(B−I) = −144 giving (ℤ/12)² torsion. **Fixed
   (v5).**

## CONFIRMED — prose/definitional (fixed in draft v5)

3. **[MAJOR] "breathable/breather/rooted" never defined.** Added a definition block at the
   head of §3; "breather" clarified as the root X, not B.
4. **[MAJOR] Master-table legend undefined (qs/rs/qrs/free/dark).** Added the legend line
   mapping the four letters to the four Galois channels (q=√5, r=√−3, s=√−15), with the
   counts 120/20/20/10/70. Resolves the "qs vs rs undisambiguable" gap.

## ACCEPTED — deferred to the owner voice pass + appendix-writing (no math impact)

5. **[MAJOR] Editorial scaffolding still present** (⟡ stubs; empty Appendix A/B). These are
   the owner's voice pass and the reproducibility appendix — written after the panel is
   complete, per the charter cadence. Recorded, not yet actioned.
6. **[MAJOR] Open-problem-3 constants (c, λ_chain) undefined in-body; "tower" overloaded
   (chain vs Fibonacci letter tower).** A definitions pass for §6 + disambiguating "tower"
   is queued for v6.
7. **[MAJOR] Lemma 3.3 provenance parenthetical clutters + the proof gap (orientation
   bookkeeping) is where the announced Morimoto trap lives.** v6: move provenance to a
   remark; either display the orientation step or cite it as "closed case, transplants,
   proof omitted." Queued.

## Status
Draft v5 fixes the two verified math errors and the two definitional gaps. Findings 5–7
are prose/structure debt scheduled for v6 and the owner pass. **The panel is not complete:
the four attacking seats (correctness/novelty/overclaim/hostile) must run before the draft
is called referee-clean.** Re-queued for the next pass.
