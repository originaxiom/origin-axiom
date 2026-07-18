# STEP (iii) — THE COEFFICIENT COMPARISON: **KILLED-AT-(iii)**
# (PREREG_W2.md sealed sha b4c9a6bb; step (iii) unlocked by the cc2 gate,
# w2_gate_cc2/GATE_VERIFIED_CC.md; cell script w2_step3.py; full log
# step3_output.txt; exact coefficients coefficients_both_conjugates.json.
# 17/17 internal gates PASS, zero failures; every number below is exact.)

## The sealed comparison, verbatim

- Molien doublet (step-(ii) conventions, used verbatim): M(q) = φ²·Π_{k≥1}Π_t
  (1 − ζ₁₀^t q^k)^{−m_k(t)} (weight-step grading g(k) = k), M′ = Galois
  conjugate (seed t ↦ 3t ≡ √5 ↦ −√5). 120 coefficients, exact in ℚ(√5);
  every M_n lands in ℤ[φ] (verified n < 120), M_n + M′_n ∈ ℤ.
- Grades: k ≤ 40 from the gate artifact eigen_distribution.json ONLY
  (cc2-verified); k = 41..119 from the gate artifact's own closed_form_law,
  verified here to reproduce all 41 banked grades exactly before use.
  The kill is decided at n ≤ 1, entirely inside the gate-verified region.
- Dressing (banked B672, step-(ii) record verbatim): comp_a = q^{ν_a}·η^{48/5}·
  (reduced), ν = (0, 1/5), η^{48/5} = q^{2/5}(q;q)^{48/5}. Targets: reduced
  F₁-, F₂-streams (banked W33 JSON, re-derived from N₁(q;q)^{−3/5},
  N₂(q;q)^{−3/5} and verified against all 42 banked terms) and dressed
  Y^(5)_2̂ = (N₁(q;q)⁹, N₂(q;q)⁹) (all 60 banked terms verified; the banked
  identity Y^(5)_2̂ = (F₁,F₂)·η^{48/5} re-proved as series to n < 120).
  The class bookkeeping {2/5, 3/5} selects the 2̂ doublet (2̂′ lives at
  {1/5, 4/5}, outside the sealed step-(ii) landing).

## The verdict, with the decisive numbers

**All 8 sealed pairings (both conjugates × both components, reduced AND
dressed) diverge at the FIRST coefficient, n = 0.** Both orientations fail
identically; the orientation question left open at step (ii) is moot.

1. **Grade-0 kill of the sealed freedom.** M₀ = φ² = (3+√5)/2,
   M′₀ = (1−φ)² = φ^{−2} = (3−√5)/2; every target stream starts at 1.
   Repair needs c = φ^{∓2} — a **unit of ℤ[φ], not rational**. The sealed
   ONE-rational-constant freedom is unsolvable already at n = 0, shared or
   even per-component, in every orientation.
2. **Even a single ALGEBRAIC constant (diagnostic, outside the freedom)
   dies at n = 1.** Normalizing away the grade-0 unit: M₁/M₀ = −φ,
   M′₁/M′₀ = 1/φ, vs the targets' F₁,₁ = 3/5, F₂,₁ = −2/5. Ratio-drift
   witnesses (M vs F₁): r₀ = (3−√5)/2, r₁ = (6−3√5)/5, r₀ ≠ r₁ (exact).
3. **The structural feature that failed: the coefficient ARITHMETIC (a
   5-adic ring separation), not the support or the symmetry.** The Molien
   doublet is ℤ[φ]-integral (all n < 120); the reduced targets have pure
   5-power denominators with v₅(denom) = 1, 12, 49, 99, 146 at
   n = 1, 10, 40, 80, 119 — growing without bound in-window (the banked W33
   fact, reproduced here). Dressed view: the dressed Molien inherits exactly
   those 5-denominators from (q;q)^{48/5} while the dressed targets are
   integers. Any single constant has fixed v₅ and cannot bridge a v₅-gap
   that grows with n — **the same 5-adic exclusion pattern W33 banked
   against the ladder, now firing against the Molien lift itself.**
4. Paired rational combos (diagnostic, outside the sealed pairings, so the
   bank shows them examined): (M+M′) vs targets — first mismatch n = 0
   (3 vs 1); (M−M′)/√5 — n = 0 agrees (1 = 1, a one-coefficient
   coincidence), first mismatch n = 1 (−2 vs 3/5, −2/5; dressed −58/5 vs
   −9, −10).
5. Growth (recorded as data, no asymptotic claim): |dressed M|/|Y_2̂,₁|
   excess ≈ 5.16 at n = 40, ≈ 26.8 at n = 100 — the in-window kill is
   arithmetic (units + 5-adic), not a growth blow-up.

## The freeness caveat (GATE_VERIFIED_CC.md), addressed precisely

The gate named freeness-through-grade-40 as the first diagnosis point of a
mismatch. **This kill is not a freeness artifact:** n = 0 uses only
V₀ = span(F₁,F₂) (dim 2, free by definition; grade-0 factor φ^{±2} exact),
and n = 1 uses only the gate-verified V₁ distribution (cc2-agreed). No
freeness assumption enters n ≤ 1, where the comparison is already decided;
freeness first affects which higher grades feed n ≥ 2 and cannot repair the
grade-0 unit or the n = 1 drift. The 5-adic separation (3) is likewise
freeness-independent: it is a property of the target streams vs ANY
ℤ[φ]-integral Molien product.

## What survives, exactly

The step-(ii) structure all passed and stands: dressed support classes
{2/5, 3/5}, single-class per component, the doublet swap = Galois
conjugation, grade-0 gap √5. What the candidate gets right is the SHAPE
(support, doublet, swap); what it gets wrong is the first two coefficients
and the coefficient ring. Kill pattern banked alongside wave 1's seven:
**"right support lattice, wrong arithmetic — unit-valued constants (φ^{±2})
and a growing 5-adic denominator gap that no one-constant bookkeeping can
close."**

K020 silver control: NOT triggered (it runs only on MATCH).
