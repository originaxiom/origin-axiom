# B1728 — THE LINE'S ORDER AS A QUOTIENT OF HYPERCHARGE (P-296): B1703'S COINCIDENCE LAW DERIVED — ON A FLAT LINE OF ORDER N THE FRAME SEES THE CHARGES 6Y MOD N, UP TO SWAP AND SIGN, BECAUSE A CHARGE SHIFT BY N IS A PHASE, THE SWAP IS A TRANSPOSE AND THE SIGN IS THE TORUS'S INVOLUTION

**Verdict: PROVED** (the "if" direction: three identities proved from B1656's definitions and checked to machine
precision; the "only if" direction is B1703's census, re-checked order by order here, not proved). cc (main),
2026-10-23. No physical quantity. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /five-ality|hypercharge mod|6Y mod|line census|swap and negation|d ?= ?e|Y_e ?= ?Y_d|coincide on a (flat )?(hypercharge )?line/ (full text): 13 of 1500 arcs on main match (NEGATIVE 5, OPEN 2, PROVED 5, RETRACTED 1)`.
Bearing on it:
- **B1703 (the line census) found the law by computation:** d = e iff N ∣ 4 or 5, u = d iff N ∣ 6, u = e iff N ∣ 2 or
  7, "their twist pairs agree modulo the lattice up to swap and negation", on 1 224 lines of order ≤ 16 at two τ. It did
  not derive it.
- B1698 (the order-5 lines: minimal SU(5)'s Y_e = Y_dᵀ); B1716 (the frame's exact zeros, which mask orders 4 and 12);
  B1712, B1713, B1723 (the censuses whose rows show the coincidences).

P-296 (S190) restated the law as read off B1723's stored rows, without citing B1703 and without u = e; this arc corrects
that (a dated note on P-296) and supplies the derivation P-296 asked for. **Literature:** the theta functions'
quasi-periodicity; SU(5)'s five-ality and the Standard Model's ℤ₆ centre; standard.

## 1. The setting

B1656's frame (the functions B1723 sealed). On the flat line w = ατ + b, with (α, b) of exact order N in (ℚ/ℤ)², a
field of charge q (6Y: Q 1, u −4, d 2, L −3, e 6) has the twist twist_of(qw, τ) = (qα, 2qb). A sector (f, g) takes the
left field's twist x and the right field's twist y, builds bil(x, y; u), its four channel pairings P_s = ⟨εC_s, bil⟩,
their residues R_s and regularised norms c_s, the weights u_s = √(2πL + c_s)·R_s, M = Σ u_s E_s* and Y = coupling(S, M).

## 2. The three identities (`verification/the_quotient.py`)

**Step 1, a charge shift by N is a phase.** thc(a + k, b + 2m; u) = e^{4πima} thc(a, b; u) for integers k, m (re-index
the sum; e^{2πi(n+a)·2m} = e^{4πima}); bil's own factors e^{iπb} see b only mod 2. A charge shift q → q + N moves the
twist by (Nα, 2Nb) ∈ ℤ × 2ℤ, so each sector's bil, its residues, its weights, M and Y are multiplied by one phase; the
norms c_s are unchanged. The singular values, ∣V∣ and J are unchanged.
- Checks: the shift identity to 1.1 × 10⁻¹⁴; on five lines (orders 3, 4, 5, 6, 10), every sector, both readings, a
  shift by N changes no ratio (1.5 × 10⁻¹³ in log) and Y by one phase (1.4 × 10⁻¹⁴).

**Step 2, the swap is a transpose.** bil(y, x) = bil(x, y)ᵀ entry by entry. Under the transpose ⟨εC₁, ·⟩ changes sign and
⟨εC_s, ·⟩ for s = i, j, k does not, and the dual basis obeys the same signs (E₁*ᵀ = −E₁*, E_s*ᵀ = E_s*), so R₁ → −R₁,
c_s is unchanged and **M(y, x) = M(x, y)ᵀ**. Then coupling(S, Mᵀ) = coupling(S, M)ᵀ exactly when εS is symmetric, which
holds for every S in span(i, j, k), so for both of the frame's readings S and S̃: **Y(y, x) = Y(x, y)ᵀ**.
- Checks: bil 3.3 × 10⁻¹⁶, M 4.4 × 10⁻¹⁶, Y with S 6.5 × 10⁻¹⁶ and with S̃ 9.1 × 10⁻¹⁶; the control S = 1 (εS
  antisymmetric) breaks it (2.0).

**Step 3, the sign is the torus's involution.** bil(−x, −y; u) = −bil(x, y; −u): the theta series give
thc(−a, −b; u) = thc(a, b; −u); in the entries at u + τ the quasi-periodicities of thc under v → v − 2τ and of θ₁ under
u → u + τ supply cancelling phases; θ₁ is odd. So P_s(−x, −y; u) = −P_s(x, y; −u): the residues are unchanged
(Res f(−u) = −Res f), and so are the norms on the centrally symmetric cell (a₀ → −a₀ leaves ∣a₀∣²). Hence **M and Y are
unchanged** when both twists are negated.
- Checks: bil 4.9 × 10⁻¹⁵, M 1.3 × 10⁻¹⁵, Y 1.2–1.3 × 10⁻¹⁵ (both readings).

## 3. The law

Two sectors (f₁, f₂) and (g₁, g₂) have the same singular values whenever (6Y(f₁), 6Y(f₂)) ≡ ±(6Y(g₁), 6Y(g₂)) or
±(6Y(g₂), 6Y(g₁)) mod N, with Y equal up to a phase in the first case and transposed in the second. With the charges
(Q 1, u −4, d 2, L −3, e 6):

| pair | agree mod N when | so |
|---|---|---|
| down (1, 2), leptons (−3, 6) | same: N ∣ 4; swapped: N ∣ 5 (Y_e = Y_dᵀ); negated: N ∣ 2 | **d = e if N ∣ 4 or N ∣ 5** |
| up (1, −4), down (1, 2) | same: N ∣ 6; negated: N ∣ 2, swapped and negated: N ∣ 3 | **u = d if N ∣ 6** |
| up (1, −4), leptons (−3, 6) | same: N ∣ 2; negated: N ∣ 2; swapped and negated: N ∣ 7 | **u = e if N ∣ 2 or N ∣ 7** |

This is B1703's law, now derived in the "if" direction. **Checks:** on two lines of every exact order 1–12 at one τ,
both readings, 59 of 59 sector pairs not masked by an exact zero agree with the law (coincident to < 10⁻⁸ in log where
it predicts, apart by ≥ 0.08 elsewhere); the masked ones are B1716's zeros (orders 4 and 12). **The converse** (no other
coincidence) is B1703's census (1 224 lines of order 8–16 at two τ, and fresh data) and this check; it is not proved.

## 4. Reading (labelled)

- Mod 5, 6Y is SU(5)'s five-ality: the 10 = {Q, u^c, e^c} has 6Y ≡ 1 and the 5̄ = {d^c, L} has 6Y ≡ 2 (up to sign), so
  an order-5 line imposes minimal SU(5)'s Y_e = Y_dᵀ, which the data break in the second generation by the
  Georgi–Jarlskog factor 3 (P-294).
- Mod 4: Q ≡ L and d^c ≡ e^c, the lepton-as-fourth-colour pairing of Pati and Salam.
- Mod 6: 6Y mod 6 carries the Standard Model's ℤ₆ centre, which does not tell u^c from d^c up to sign, so Y_u = Y_d.
- The coincidences are the frame reading hypercharge only through its quotient by the line's order; from order 8 on
  (B1703) the quotient is fine enough to split every sector.

## Files

- `verification/the_quotient.py` → `the_quotient.json`, `the_quotient_run.txt`.
- The lock: `tests/test_b1728_the_lines_order_as_a_quotient_of_hypercharge.py`.
