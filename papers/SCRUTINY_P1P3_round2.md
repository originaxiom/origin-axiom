# P1/P3 re-panel (round 2) — adjudication, incl. a BANKED-error correction (2026-07-09)

**The re-panel of the CORRECTED drafts (P1 v3, P2 v2, P3 v3) — 6 seats, every finding
adversarially verified — returned 14 confirmed defects: P1 (1 MAJOR + 2 MINOR), P2 (5 MINOR),
P3 (6 MAJOR). Several P3 findings are in the banked results (B479/T-BREATH-TORSION) and several
were INTRODUCED by my own v2/v3 "corrections." All key findings re-verified by CC in Sage. This is
the "true fact one level too strong" pattern recurring — and this time it is mine. Verdict: P1 and
P3 need genuine rework (not a light patch); P2 needs precision fixes; B479 is corrected in the bank.**

## P3 — 6 MAJOR (thesis-level; two are banked errors)
1. **The determinant register is THREE-valued, not ℤ/6.** det(Par·W(w)) = −ω^{#L−#R}: Par is fixed
   with det Par = −1 always, so the image is the coset **−μ₃ = {−1, −ω, −ω²}** (three values); +1,+ω,+ω²
   are never attained (verified: reproducer rf3_quantum.py decodes only 3 symbols). My v2 "fix"
   (v1 "ℤ/2" → v2 "ℤ/6, six values") **over-corrected**: the honest count is 3. FIX: state −μ₃, three
   values, a fixed −1 sign times a ℤ/3 character of the imbalance mod 3.
2. **"norm = parity = one and the same residue" is overstated.** T-2REG itself is correct —
   det(Par@N) = sign(σ@N) = (−1)^{(N−1)/2}, the two *quantizations* agree at each level (verified:
   br1_br2.py PASS at 15/45/75/225). BUT the value **alternates** (−1 at N≡3, +1 at N≡1: 15→−1,
   45→+1, 75→−1, 225→+1) while the norm N(λ_m) is **constant −1**. So norm and parity are DIFFERENT
   ℤ/2's indexed by different things (m vs N); they coincide only at N≡3 mod 4. The paper's "one residue
   through three instruments" thesis is false — there are THREE distinct invariants (constant norm;
   alternating parity; three-valued word-det) that agree only in special cases. FIX: present three
   distinct-but-related invariants, not one.
3. **[BANKED ERROR] d=5 held-breath field is NOT ℚ(√41).** The order-5 held-breath character has
   minpoly **z⁴−3z³+7z²−4z+4** — a **degree-4** field (field disc 5²·41, quadratic subfield **ℚ(√5)**,
   no real roots). B479 read "41" from the squarefree part of the poly discriminant 16400=2⁴·5²·41 and
   mislabeled the field. CORRECT: d=3 ⟹ ℚ(√−7) (z²−z+2, genuinely quadratic, τ_3=−1 rational) STANDS;
   d=5 ⟹ a degree-4 field over ℚ(√5). Registry T-BREATH-TORSION corrected.
4. **The "closed-form field Δ_d=τ²(τ²−8)" has scope τ_d ∈ ℚ only.** It gives a clean quadratic field
   only when τ_d is rational (d=3; degenerate d=4,6); for irrational τ_d (d=5,…) the character field is
   degree 4 and Δ's norm is a discriminant factor, not the field. FIX: state the scope.
5. **F7 "EXACTLY" is only ⊇.** The mechanism (a^d=I ⟹ σ_m=swap ⟹ fixed=symmetric locus) proves
   torsion ⊆ Fix; the ⊆ direction (no non-torsion fixed) is NOT proven. FIX: downgrade "exactly" to ⊇,
   or prove ⊆.

## P1 — 1 MAJOR
6. **[central object mis-defined] the seam form does not take values in ℚ(√5,√−3).** The object defined
   in §2, tr(Par·P_a·Q_b), is a degree-8 element of ℚ(ζ₆₀), non-real, at all 49 support points
   (verified: solve_H(raw)=None everywhere). The reported 4-vector is the **Galois average / ℚ(√5,√−3)-
   projection** H_avg(t) — the engine docstring literally says "Galois-averaged to H." So S1/abstract
   ("the seam form takes 30 values in ℚ(√5,√−3)") are true only of the *projection*, not the defined
   observable — the SAME field-labeling class v2 claimed to fix. FIX: redefine the seam form as the
   ℚ(√5,√−3)-isotypic projection (Galois average) of the seam trace; all downstream (30 values, 49
   support, channels, selection rule, dark locus) hold verbatim for the projection. (Two MINOR: the
   54/70 dark-at-closure number isn't produced by verify_patterns.py — needs its own reproducer; §3-vs-§8
   both use "Galois equivariance" — the §8 signed-permutation argument must be worded to not collide.)

## P2 — 5 MINOR (the v2 corrections were imprecise)
7. **"disc not a square ⟹ no quadratic subfield" is an invalid inference** (C₄/D₄ quartics have
   non-square disc yet DO have a quadratic subfield). The CONCLUSION (x⁴−x−1 has no quadratic subfield)
   is TRUE — but because its Galois group is **S₄** (point-stabilizer S₃ is maximal), not because of the
   discriminant. FIX: justify by the S₄ Galois group.
8. **The ℚ(√−3)-absence is itself vacuous.** If the child has no quadratic subfield at all, "ℚ(√−3) is
   absent" is trivially true — my v2 "non-vacuous replacement" is vacuous by its own logic. FIX: state
   the honest content — the child's trace field is an S₄-generic quartic sharing no subfield with the
   parent's ℚ(√−3); the laundering is "distinct parents → the same S₄-generic child," not "field X is
   absent." (And "invariants of the child depend only on the child" is definitional; the non-trivial
   content is the collision itself.)

## Verdict + what I'm doing
The re-panel paid for itself again: it caught a **banked** field error (B479 ℚ(√41)) and multiple
overclaims **I introduced while "correcting" v1.** Immediate integrity actions taken: registry
T-BREATH-TORSION corrected; this record banked. Next (done carefully, each fix re-verified, NOT rushed
— rushing is exactly how the v2 errors entered): P3 → v4 (three-distinct-invariants; three-valued det;
d=3 ℚ(√−7) / d=5 degree-4-over-ℚ(√5); ⊇ not "exactly"); P1 → v4 (seam = projection); P2 → v3 (S₄
justification; honest laundering framing). P4 remains the only paper that has cleared this gauntlet
clean. The honest status of P1–P3: **NOT publication-ready; the underlying computations are sound but
the write-ups repeatedly state them one categorical level too strong.**
