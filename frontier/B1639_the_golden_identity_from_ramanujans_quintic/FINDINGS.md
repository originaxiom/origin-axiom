# B1639 — THE GOLDEN IDENTITY FROM RAMANUJAN'S QUINTIC MODULAR EQUATION: given Ramanujan's form of Jacobi's degree-5 modular equation (Berndt, *Ramanujan's Notebooks* III, ch. 19, Entry 13(xii)), Σ_p g_p(τ)g_p(Nτ) = 8 is a theorem, and so is the golden spectrum of the weave's lowest coupling on every geodesic of discriminant 5

**Verdict: PROVED** (given the cited classical theorem). R1 and R2 hold. R3 holds in its substantive clause. Its second
clause, a fixed principal-branch sign pattern, fails as sealed; that is explained in §2 and is not used by the proof.
cc (main), 2026-10-13. Sealed `081a02663` before the run. No data. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /Ramanujan|quintic|Jacobi|modular equation|golden identity/: 24 of 1410 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 17)`
— B1635, B1636, B1638; B672, a level-5 relative on the record (the Rogers–Ramanujan continued fraction), which is not
this identity. **Literature:** Berndt, *Ramanujan's Notebooks* III (1991), ch. 19, Entry 13(xii), pp. 280–282. It was
seen through Bairy (Gen. Math. 17, 2009) and Guadalupe (Integers, 2026); the book was not opened.

## 1. The sealed run (`golden_from_ramanujan.py`, unchanged)

| cell | prediction | prior | result |
|---|---|---|---|
| **R1** | N = G₁·D·G₂, D of determinant 5, G₁ and G₂ in Γ(2) | 80% | **HOLDS** — 174 factorisations in the search box, 46 with both factors in Γ(2), e.g. N = [[1, 4], [4, 17]]·diag(5, 1)·[[−5, −6], [6, 7]] (checked by hand) |
| **R2** | g₃¹²(α(1−α))² = 2⁸, (g₂/g₃)² = α, (g₄/g₃)² = 1 − α at 20 points | 97% | **HOLDS** — the largest residual is 1.1·10⁻⁴⁶ |
| **R3** | (1 + ss′ + cc′)⁶ = 2¹⁰αβ(1−α)(1−β); and one principal-branch sign pattern of Ramanujan's relation vanishing at all points | 85% | **HOLDS in its first clause** (relative 2.0·10⁻⁴⁹). **FAILS in its second as sealed**: no fixed pattern vanishes at all 20 points; three patterns each vanish at some |

## 2. The proof

1. **Degree 5.** λ = θ₂⁴/θ₃⁴ is invariant under Γ(2). With N = G₁·diag(5, 1)·G₂ (R1), α = λ(τ) = λ(τ₂) and
   β = λ(Nτ) = λ(5τ₂) with τ₂ = G₂τ. So β has degree 5 over α.
2. **The λ-forms.** Jacobi's θ₂θ₃θ₄ = 2η³ gives g₃¹² = 2⁸/(α(1−α))², g₂ = g₃·s and g₄ = g₃·c, with s² = α and
   c² = 1 − α (R2). So H = g₃g₃′(1 + ss′ + cc′), and (g₃g₃′)¹² = 2¹⁶/X², where X = αβ(1−α)(1−β).
3. **Ramanujan.** Entry 13(xii) gives √(αβ) + √((1−α)(1−β)) + 2(16X)^{1/6} = 1 for real α, β in (0, 1). λ omits 0
   and 1 on H, so each root has an analytic continuation on the simply connected H, and the relation continues with
   them. ss′ and cc′ are analytic and square to αβ and (1−α)(1−β), so they are ±(those continuations) with constant
   signs. R3's first clause, (1 + ss′ + cc′)⁶ = 2¹⁰X, identifies the signs as both negative, which is (1 − √αβ − √…)⁶
   = 2⁶·16X.
4. **Hence** H¹² = 2¹⁶·2²⁰X²/X² = 8¹² on all of H. H is continuous on a connected set with values in 8 × (twelfth roots
   of unity), so it is constant, and B1638's evaluation fixes the constant at 8.
5. **On a discriminant-5 axis** conj(g_p(τ)) = g_p(Nτ) (B1638, I5), so F = H = 8. In units of |η|², the coupling's
   characteristic polynomial is λ³ − Fλ − 8. At F = 8, scaled by 2, it becomes μ³ − 2μ − 1 = (μ + 1)(μ² − μ − 1), so
   the masses are exactly 1 : φ⁻¹ : φ⁻². By the SL(2, ℤ)-invariance of F this holds on every geodesic of
   discriminant 5.

**Why R3's second clause failed.** The principal branches of √(αβ), √((1−α)(1−β)) and the sixth root jump across their
cuts as τ moves, so no single fixed principal-branch sign pattern can hold at every point. Step 3 uses the analytic
continuations, which is what the first clause checks. The clause was badly posed, not the mathematics.

## 3. What it says

**THEOREM (given Entry 13(xii)).** On every geodesic of discriminant 5 in the upper half-plane (the axis of the
principle's tick and all its images), Σ_p |θ_p/η|⁴ = 8. There the weave's lowest symmetric coupling has normalized
masses exactly 1 : φ⁻¹ : φ⁻² (the masses' φ is the tick's φ, through Jacobi's quintic modular equation).

The converse (F = 8 only on those geodesics) stays B1636's numerical conjecture.

## 4. Disclosed

- The classical theorem is cited through secondary sources, not read in the book.
- R1 and R2 are exact identities checked numerically at 50 digits.
- The branch signs in step 3 are a discrete choice. They are fixed by evaluation, which is legitimate because both
  candidate relations are analytic and differ by O(1).

## 5. Files

`verification/golden_from_ramanujan.py` (sealed, unchanged) with `golden_from_ramanujan.json` and
`golden_from_ramanujan_run.txt`; the lock `tests/test_b1638_b1639_the_golden_identity.py`.
