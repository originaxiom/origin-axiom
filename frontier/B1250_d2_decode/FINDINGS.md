# B1250 — THE D₂ DECODE: THE TWIST IS THE SO(10) GRADING OF E₆

**Status: banked (frontier). Verdict PROVED.** Instrument + selftest in
`verification/d2_decode.py` (rc captured directly, E39). Gate 5 clean: no measured value.

**B926's surviving-shapes menu** lists **M1 — the twist crossing** as *"the strongest positive
structure on the menu (identities, not matches)"*, and gives its test in two stages. Stage **(a)** is
marked explicitly **UNAFFECTED BY THE OWNER GATE**: *"MATHEMATICS FIRST … decode D₂ — what IS the
11-flip as a character/Galois object?"* **B916** answered **NO** at a necessary condition and
registered a refined question. **This arc answers it positive.**

## 1. What B916 tested, and the one bit outside it

B916 searched the **plain** character `(−1)^⟨a,w⟩`, `a ∈ 𝔽₂⁶` — 64 candidates — and found none.
**Reproduced here: 0 solutions.** The **affine** form was one bit outside that search space:

> **D₂(w) = (−1)^(⟨w₁₃, w⟩ + 1)**,  **w₁₃ = [1, 0, −1, 0, 1, −1]**

exact on all 27 weights. **w₁₃ is itself one of the 27** — and is itself flipped. **Exactly one
weight of the 27 generates it**, and exactly one `a ∈ 𝔽₂⁶` works in either polarity.

**Not a fit.** 2⁷ = 128 candidate affine characters against 2²⁷ = 134,217,728 sign patterns: a chance
match is **~1 in 10⁶**. **Control (MB12, two-sided): 0 of 4000 random 11-subsets** of the 27 admit an
affine character — the test almost always says NO, so D₂ saying YES is content.

## 2. The decode — earned, not dimension-matched

A root vector sends `w → w + α`, so the flip parity `⟨w₁₃,w⟩ mod 2` changes by `⟨w₁₃,α⟩ mod 2`.
**The roots even against w₁₃ preserve the flip class and generate the character's stabiliser.**
Computed from the B883 rep (**72 roots recovered cleanly; e₆ has exactly 72** — the arc's own check):

| | |
|---|---|
| even roots | **40** → stabiliser dim 6 + 40 = **46 = dim(𝔰𝔬(10) ⊕ 𝔲(1))** |
| odd roots | **32** → complement dim **32 = 16 + 16̄** |

and the **orbits of the 27 under that stabiliser are [1, 10, 16]** — the SO(10) branching, with the
singlet block **exactly {w₁₃}**. Therefore:

> **D₂ FLIPS THE 1 + 10 AND FIXES THE 16.**

This satisfies the **B1223 template**: the subalgebra is **exhibited** (as the character's stabiliser)
and it **acts** (its orbits are computed and give 1+10+16) — it is not matched by dimension.
`T-IDENTIFICATION-IS-AN-INPUT` is respected.

**B916's guess is corrected.** Its *"11 = 8 + 3, one octet block plus the three vacuum lines"* is not
what the structure shows. The split is **11 = 1 + 10**. (The weight-sum grading gives 6/15/6 with
flips 2/7/2 — a *different*, non-invariant slicing, recorded so no seat re-derives it as the answer.)

## 3. Consequence for M1

B926 named the risk precisely: *"the D₂ decode may dissolve the twist into convention (then the shape
dies honestly)."* **It does not dissolve.** A character with a **unique** generator and a **0/4000**
control is a definite algebraic object, not a basis choice. **M1 survives its stage-(a) test**, and
the twist carries the **matter/Higgs split** of the 27.

## 4. Fences — stated because this is the layer where look-elsewhere is deadliest

- **NOT claimed: that this object produces Standard Model matter.** That the **16** "is one
  generation" is **standard GUT nomenclature for the representation**, not a derivation. Reading it
  as physics output is exactly the I-13 debt.
- **No physical gauge theory, no dynamics, no symmetry-breaking sector, no measured value, no
  crossing.** Stage (b) — the sealed comparison against measured ratios — is **RED, owner-only, and
  untouched**.
- The 6/15/6 weight-sum grading has SU(6)×SU(2) *dimensions*; that identification is **NOT made** —
  dimension agreement is not a map.

## Dependencies

B916 (the registered question, and the kill this extends), B926 (M1 and its stage split),
B883 (the 27 and the e₆ rep), B1223 (the exhibit-the-map template), B1225/`T-NO-CANONICAL-SELECTOR`.
