# B1639 — PREREGISTRATION: THE GOLDEN IDENTITY FROM RAMANUJAN'S QUINTIC MODULAR EQUATION

cc (main), 2026-10-13. **Sealed before `golden_from_ramanujan.py` runs.** No data. 0 of 19.

**Why it matters.** B1638 showed numerically, to 49 digits, that H(τ) = Σ_p g_p(τ)·g_p(Nτ) = 8 everywhere, with
g_p = (θ_p/η)² and N = [[−1, −2], [2, −1]] (determinant 5). On the tick's axis that is F = Σ|θ_p/η|⁴ = 8, which makes
the weave's lowest coupling golden. A proof turns B1636's golden spectrum on every discriminant-5 geodesic from numerical
into a theorem, and it names the mathematics that ties the masses' φ to the tick's φ.

**The derivation, by hand, written before the run.** Let λ = θ₂⁴/θ₃⁴.
1. Jacobi's θ₂θ₃θ₄ = 2η³ gives g₃¹² = 2⁸/(λ(1−λ))², g₂ = g₃·s and g₄ = g₃·c, with s² = λ and c² = 1 − λ.
2. So H = g₃g₃′(1 + ss′ + cc′), where ′ is evaluated at Nτ, and
   H¹² = 2¹⁶(1 + ss′ + cc′)¹²/(αβ(1−α)(1−β))², with α = λ(τ) and β = λ(Nτ).
3. Ramanujan's form of the degree-5 modular equation (Berndt, *Ramanujan's Notebooks* III, ch. 19, Entry 13(xii),
   pp. 280–282) states: if β has degree 5 over α, then
   (αβ)^{1/2} + ((1−α)(1−β))^{1/2} + 2(16αβ(1−α)(1−β))^{1/6} = 1.
   With the branches of ss′ and cc′ fixed as the instrument reports, this gives (1 + ss′ + cc′)⁶ = 2¹⁰αβ(1−α)(1−β).
4. Hence H¹² = 8¹² at every τ. H is continuous on the connected upper half-plane and takes values in 8 × (twelfth roots
   of unity), so it is constant, and one evaluation (B1638) fixes it at 8.
5. On a discriminant-5 axis, conj(g_p(τ)) = g_p(Nτ) (B1638, I5), so F = H = 8 there, and the masses are exactly
   1 : φ⁻¹ : φ⁻². By the SL(2, ℤ)-invariance of F, this holds on every geodesic of discriminant 5.

## Seen first

`VERDICT topic-sweep /Ramanujan|quintic|Jacobi|modular equation|golden identity/: 24 of 1410 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 17)` — B1635, B1636, B1638; B672 (a level-5 relative on the record: a ratio of weight-5 streams is the Rogers–Ramanujan continued fraction, not this identity). **Literature:** Berndt, *Ramanujan's Notebooks* Part III (1991), ch. 19,
Entry 13(xii), seen through Bairy (Gen. Math. 17 (2009), which cites it with that statement) and Guadalupe (Integers
2026). The book itself was not opened. The statement is used as cited, and the branch is identified numerically (R3).

## Disclosed

- **The proof rests on a cited classical theorem.** It does not re-derive Jacobi's or Ramanujan's degree-5 equation.
- **Two steps are mechanical checks, not proofs:** R1, that N relates α and β by degree 5, and R2, the λ-forms of the
  g_p. They are exact identities checked here numerically at 50 digits.
- **The "only if" direction is not addressed.** F = 8 nowhere off the discriminant-5 geodesics stays B1636's numerical
  conjecture.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **R1** | N = G₁·D·G₂ with D ∈ {diag(1, 5), diag(5, 1)} and G₁, G₂ ∈ Γ(2) (so β = λ(Nτ) has degree 5 over α = λ(G₂τ) = λ(τ)) | 80% |
| **R2** | at 20 random τ, g₃¹²(α(1−α))² = 2⁸, (g₂/g₃)² = α and (g₄/g₃)² = 1 − α, within 10⁻⁴⁰ | 97% |
| **R3** | (1 + ss′ + cc′)⁶ = 2¹⁰αβ(1−α)(1−β) within 10⁻⁴⁰ relative at the same points; and exactly one consistent sign-and-branch pattern of Ramanujan's relation vanishes at all of them | 85% |

**The reading, written before the run (the cells can only lower it).**
- **If R1–R3 hold, B1636's golden spectrum is a theorem on every geodesic of discriminant 5**, given Ramanujan's
  Entry 13(xii). The lowest coupling the weave allows has masses exactly 1 : φ⁻¹ : φ⁻² on the principle's own closed
  geodesic, because Jacobi's quintic modular equation holds there.
- **If R1 fails,** N's relation to the degree-5 correspondence needs a different factorisation, which this arc then
  names.

## Instruments

`verification/golden_from_ramanujan.py`; hashes in `ARTIFACT_HASHES.txt`.
