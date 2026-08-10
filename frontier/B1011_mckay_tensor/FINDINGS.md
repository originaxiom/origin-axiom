# B1011 — the hearing data IS McKay ⊗ McKay: the tensor factorization, exact at every step

**Date:** 2026-08-10 · **Seat:** cc (verification) · **Sealed:** `fc807f11`, prior OUTCOME A ·
Gate 5-Q. **No SM quantity anywhere in this arc.**

**Verdict: PROVED — OUTCOME A at every sealed cell, with one scope line stated exactly.** An
incoming chat1 derivation, re-derived here under verify-don't-trust in **exact arithmetic** — no
verdict line below rests on a float.

---

## THE HEADLINE

> **On B593's two-sided instrument (R = T, L = S⁻¹T⁻¹S on SU(3)₂'s six primaries), the generated
> representation factorizes exactly:**
>
> ### ρ₆ ≅ (χ ⊗ V₂(2I)) ⊕ (V₂(2T) ⊗ V₂(2I))
>
> **as a 2T×2I representation — the θ-eigenspaces being precisely the two summands. The object's
> hearing data is (E₆ McKay character)⊗(E₈ McKay spin) ⊕ (E₆ McKay spin)⊗(E₈ McKay spin), and
> every forced coupling is a product of a character value and a trace.** The two ends (B248/B261)
> appear *inside the hearing instrument itself*.

## THE CELLS (sealed order, all exact)

**C1 — the group. PASS.** |⟨R,L⟩| = **2880 = |2T×2I| exactly**, by mod-p enumeration at **two**
unramified primes (61, 241; both ≡ 1 mod 60, coprime to the denominator set {2,3,5}) plus **Serre's
injectivity lemma** (reduction mod p > 2 is injective on finite subgroups of GL_n over a p-integral
ring — the named classical input). **63 conjugacy classes = 7 × 9**, sizes summing to 2880, word
representatives tracked (`class_reps.json`). No hidden central extension: the global scalars are ±1.

**C2 — the isotypic splitting. PASS.** The θ-eigenspaces (odd dim 2, even dim 4) are **exactly**
invariant — verified in ℚ(ζ₆₀) arithmetic (`b1011_exact.py`; Σ·Σ† = **75**·I exact, so scalar
normalization cancels in L and the unnormalized Σ is used exactly). The C3 character match below
identifies them as the two isotypic components.

**C3 — the four steps. PASS.** (a) **χ multiplicative on all 576 pairs of 2T, exactly** (the ℤ₃
character with kernel Q₈, built in the quaternion model). (b–d) subsumed by: **the class-by-class
character match is 63/63** — a size-preserving bijection between ⟨R,L⟩'s classes and
classes(2T)×classes(2I) under which **(size, χ_odd, χ_even) agree as exact cyclotomic numbers**,
with the model characters χ(A)·tr V₂(B) and tr V₂(A)·tr V₂(B). Characters determine
representations; the factorization holds.

**C4 — the trace sets. PASS.** 2T: {−2,−1,0,1,2} (5 values). 2I: **{−2, −φ, −1, −1/φ, 0, 1/φ, 1,
φ, 2}** (9 values) — **φ entering only via 2cos(π/5) and 2cos(2π/5), as exact elements of
ℚ(√5) ⊂ ℚ(ζ₆₀)** (√5 = 1 + 2(ζ₅+ζ₅⁴), exact).

**C5 — deriving the banked laws. PASS, scope stated.**
- **Forced counts by inclusion–exclusion, exact:** θ-odd 8·120 + 24·2 − 8·2 = **992**; θ-even
  2·120 + 24·2 − 2·2 = **284** — matching the incoming enumeration.
- **B641's five tones DERIVED:** det ρ_odd = χ²·det V₂(B) = **χ² exactly**, so B641's ζ (ζ² = det)
  **cancels χ**, leaving |value| = |½ tr V₂(B)| ∈ **{0, 1/(2φ), 1/2, φ/2, 1}** — the banked tone
  set, now a consequence of the 2I trace set. Ear-independence is automatic in this phase
  convention (the anti-Hermitian part contributes no real quadratic form).
- **B856's period-5 law DERIVED at character level:** computed exactly for m = 1..15, the class of
  RᵐLᵐ has **period 5 in m**; m ≡ 0 (mod 5) lands on ±1, giving **h(5) = −1 in B856's twisted
  convention** (the weld's C acts as −1 on the odd plane).
- **SCOPE, exactly:** the pointwise map m ↦ h(m) for a *specific listener* u inherits B593/B856's
  listener convention and is **not re-derived here** — what is derived is the period, the forced
  criteria, and the value sets. B856's grade moves **observed → derived (structure)**.

**C6 — the mirror law. DELIVERED.** The θ-even value set, exact:
**{0, ±1/4, ±1/(4φ), ±1/2, ±1/(2φ), ±φ/4, ±φ/2, ±1}** — the five-tone family **plus the quarter
values**, the Re(ω) = −½ classes' contribution. This is the law B593's chiral observable was blind
to **by theorem** (the twist acts trivially on the even eigenspace), stated here in closed form as
a new banked-law candidate.

## WHAT THIS CHANGES

1. **B856/B641 move from observed laws to derived ones** — the derivation chain is the McKay
   tensor structure, i.e. **the coupling layer now has a closed form**, which is what "predict the
   coupling, not the values" (`CROSSING_REQUIREMENTS` R10, L150) needs on the u†Mu side.
2. **The two-ends structure is inside the hearing instrument**: E₆'s McKay group supplies the
   character factor, E₈'s the spin factor. This is a *structural* convergence with B248/B261 —
   and it is exactly the shape L150's junction question should be asked against.
3. **The θ-even mirror is open instrument territory** with its value set already in closed form.

## PROVENANCE AND DISCIPLINE

Incoming from chat1 (machine-precision, 1.6e-14); **exactified end-to-end here**: ℚ(ζ₆₀) as
ℚ[x]/Φ₆₀ with exact `Fraction` coefficients (`b1011_exact.py`), the quaternion model of 2T×2I over
ℚ(√5) ⊂ ℚ(ζ₆₀) built independently (`b1011_match.py`), mod-p enumeration with word tracking
(`b1011_cells.py`). The u†Mu restoration (B1010) is what made this claim *visible* to the
synthesis layer — two days earlier it would have hit a framework that did not know the chain
existed. Cites: B592/B593 (the instrument), B641/B654 (tones), B856 (family law), B238 (modular
data), B248/B261 (the two ends), B1010 (the restoration).

---

**Verdict: PROVED, OUTCOME A as sealed. The five tones and the period-5 law are theorems of the
McKay tensor structure; the mirror law is delivered in closed form; nothing here is a crossing.**
