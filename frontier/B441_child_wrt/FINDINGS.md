# B441 — C5: the child's WRT/quantum invariant — field content is surgery-forced (Bin 3)

**Status: banked (C5). Tool validated (τ(S³)=1, amphichirality), field method validated
(τ(S³) reads rational), result verified across r. Verdict: Bin 3 (laundering). Firewalled.**

## The question and the instrument

WRT is the Chern–Simons partition function — the deepest, physics-touching, and first
commensurability-*non*-invariant channel of the campaign. For each odd r, τ_r(4₁(5,1)) ∈
ℚ(ζ_{4r}) via the Kirby surgery formula on the parent's (validated) colored Jones. The tool
`wrt.py` was validated two ways before any result — τ_r(S³)=1 and amphichirality
τ_r(4₁(5,1))=conj τ_r(4₁(−5,1)) — catching two build bugs (colored-Jones convention; a
factor-of-2 in the framing twist). "Verify before headline" ran *before* the number, not after.

## The forced-vs-residual split (the golden-inversion lesson, applied)

The **forced skeleton** is τ_r(L(5,1)) = τ_r(unknot(5,1)) — what H₁=ℤ/5 + the slope-5 surgery
force into *every* knot's child. Field content read by the **Galois-twist stabilizer**:
Field(τ) = Fix{a ∈ (ℤ/4r)* : σ_a(τ)=τ}. Only the residual τ(child)/τ(skeleton) is compared.

## Result (verified)

- **Field(τ_r(4₁(5,1))) = Field(τ_r(L(5,1))) — the SAME Galois subgroup, at EVERY r tested
  (7, 9, 11, 13, 15, 21).** The residual τ(child)/τ(skeleton) lies in that same forced field
  (trivial residual). The figure-eight adds **no** field content at its forced slope.
- At **r=15** that field is degree 8 and contains **√5, √−3, √−15** — but all three are
  **forced**: present already in L(5,1) *and* in trefoil(5,1). None is figure-eight-specific.
- The knot-dependence is entirely in the **value**: τ(child) ≠ τ(skeleton) as numbers
  (|diff| ≈ 7.8 at r=15) — a distinct *element* of the *same* forced field.

## Verdict — Bin 3 (laundering) — STRENGTHENED by adversarial review

The child's WRT **field content is surgery-forced, not figure-eight-specific**. The √5/√−3/√−15
one might read as "the child speaking the parent's languages" are numerator-forced — the unknot's
child speaks them identically. The Inversion Law holds at the WRT floor, the deepest channel:
surgery launders identity down to a specific element of a forced field, and nothing finer.

**Strengthening (independent adversarial recompute, exact cyclotomic engine, 2026-07-05).** The
field is not just "child = skeleton" — it is **exactly ℚ(ζ_r)** for both, at every r (15 values
tested: {5,7,9,11,13,15,17,19,21,23,25,27,33,35,45}). The stabilizer is universally **{1, 2r+1}**,
and σ_{2r+1}: ζ_{4r} ↦ −ζ_{4r} has fixed field ℚ(ζ_{2r}) = ℚ(ζ_r) (r odd), degree φ(r). So the
child's WRT lands in the *canonical level-r WRT field*, knot-independently; the √5/√−3/√−15 at
r=15 are just ℚ(ζ_15) ⊇ those quadratics — fully forced. **No Bin-1 break exists** in the wider
sweep. The negative is robust and now mechanized.

**Framing correction (same review).** The `τ_r(S³)=1` validation is **structurally tautological**
(with cj_unknot≡1 and p=1, F_L *is* F_{U+}); it did not catch bugs and is not cited as doing so.
The genuine validations are amphichirality (non-trivial, passes to 1e-43) and the Kashaev match
(⟨4₁⟩₅ = 46+2√5) — those caught the two build bugs.

**Observation, recorded NOT built on (small sample, artifact-suspect by discipline):** at the
*unforced* slope 7 the child sometimes adds field content beyond its skeleton (r=5, r=15) while
the forced slope 5 never does. Two data points — noted as a lead, not a result. Building a
"the forced slope launders more completely" story on it is exactly the striking-shape trap.

**Bar note:** forced ✓, unsought ✓ (registered three-bin), control ✓ (skeleton + trefoil + slope-7).
A NEGATIVE at the physics-touching channel — no bar cleared, no promotion. Trefoil colored Jones
used as a secondary control (agrees) but not independently validated; the core child-vs-skeleton
result uses only the validated cj_fig8 / cj_unknot.

**Provenance.** wrt.py (validated), field_content.py → field_content.json; lock
tests/test_b441_child_wrt.py (4/4). Prereg: PREREGISTRATION.md. Cross-refs: B384/B419 (colored
Jones), B208/B214 (parent √5 at 5|N), B434 (the forced slope), the Inversion Law (B437/B438/B440).
