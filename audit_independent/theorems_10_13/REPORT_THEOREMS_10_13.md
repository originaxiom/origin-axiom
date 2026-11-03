# Independent verification of agy Theorems 10–13 (commit `dcae538ab`, 2026-11-03 11:01)

**Branch:** `audit/independent-2026-11-03`. **Script:** `t10_13_check.py`. **Output:** `t10_13_results.json`.

**What I ran.** The agy code is run from a frozen extract of `dcae538ab`. The 2-loop SM RGE is my own: written from the literature (d/d ln μ, top-only Yukawa, including the electroweak 2-loop terms) and integrated with `scipy.solve_ivp`. It shares no code with agy. The pole matching uses the fit formulas of Buttazzo et al. (arXiv:1307.3536).

## Summary

| Theorem | Mathematical statement | Verdict | What it does *not* establish |
|---|---|---|---|
| **10**: A³ + I involution; T⁸ equivalence | Holds. det(A³ + I) = 20, A³(2/5, 1/5) ≡ −(2/5, 1/5), and the Yukawa identities hold to about 1e-13 | **CONFIRMED (algebra) / REFUTED as a selection** | T⁸ makes **all five** lines (2/5, j/5) equivalent to (2/5, 0) at shifted τ, including the four that are *not* eigenlines. So it cannot select (2/5, 0). It also shows that "Re τ = 1/√5" depends on the labelling. |
| **11**: amphichiral conjugation; θ̄ | The identity Y(−τ̄, −c̄) = P·conj(Y)·P holds | **CONFIRMED (identity) / REFUTED as strong-CP solution** | The doubled determinant is \|det Y\|², which is real for *any* matrix. The "Wilson-line relaxation" is a quark rephasing that only moves the phase into θ_QCD. θ̄ stays undetermined. |
| **12**: 2-loop closure, m_H = 125.01, "no M_Z / m_τ input" | Benchmark reproduced; the RGE is now correct | **RGE CONFIRMED / prediction REFUTED** | y_t²(M₁₂) = 1/5 is a new post-hoc boundary condition. With proper matching it gives **M_t = 169.3 GeV (−11σ) and M_h = 120.2 GeV (−30σ)**. The 125.01 comes from tree-level matching at μ = M_Z. |
| **13**: basis-invariant Weinberg PMNS | Basis invariance holds (1.7e-15) | **CONFIRMED method → NEGATIVE result** | sin²θ₂₃ = 0.0003 (−29σ), sin²θ₁₃ = 0.0139 (−14σ), sin²θ₁₂ = 0.277 (−2.5σ). The frame fails PMNS, which retracts the Phase 6 "PMNS closure". |

**Net:** these commits fix real methodology (a correct RGE, a basis-invariant PMNS, matrix-computed phases), and that is genuine progress. **No SM parameter is derived.** The scoreboard stays at **0 of 19**. Theorem 13 is an honest negative and should be banked as one.

---

## Theorem 10

**The algebra holds** (exact integer computation). With A_sig = [[2,−1],[−1,1]]:
- A³ = [[13,−8],[−8,5]] and det(A³ + I) = 20.
- (A³ + I)(2/5, 1/5) = (4, −2) ∈ 2ℤ².
- Among the five (2/5, j/5) lines, only j = 1 satisfies A³x ≡ ±x mod 5.
- agy's operator identities rerun at 1e-14 to 1e-13: c_s invariance, Y_d and Y_e invariance, Y_u picking up e^{−4πi/5}, and the T⁸ phases.

**The T⁸ "gauge equivalence" is a relabelling, so it selects nothing.** Since w = p₁τ − p₂, the line (p₁, p₂) at τ + k is the same as (p₁, p₂ − k·p₁) at τ. I checked the observables numerically:

| line at shifted τ | eigenline? | max relative difference of the 10 observables from (2/5, 0) at τ |
|---|---|---|
| (2/5, 1/5) at τ + 8 | yes | 4.8e-13 |
| (2/5, 2/5) at τ + 16 | **no** | 5.0e-13 |
| (2/5, 3/5) at τ + 24 | **no** | 6.1e-13 |
| (2/5, 4/5) at τ + 32 | **no** | 2.3e-13 |

At *fixed* τ the five lines are physically distinct; their observables differ by 93% to 835%. So "(2/5, 0) is equivalent to the eigenline" holds in exactly the same way for every non-eigenline. The eigenline property therefore cannot single out (2/5, 0). It also undercuts Theorem 8: in the eigenline's own labelling, the "Golden" point sits at Re τ = 1/√5 + 8, so "Re τ = 1/√5 is the codifferent of ℚ(√5)" is a statement about one chosen labelling, not about the model.

## Theorem 11

- **The identity is confirmed.** Y_s(−τ̄, −c̄_s) = P·conj(Y_s)·P holds, and agy's rerun gives errors below 1e-14. The audit-lane referee check (d), which goes through main's `b1656_funcs`, is a genuinely independent pipeline.
- **The "parity-doubled θ̄ = 0" is true for any matrix.** It is det(D) = det Y · det(P·conj(Y)·P) = |det Y|². On a random complex 3×3 matrix I get arg = 5.6e-17. Doubling the quark content also gives a different theory, not the SM.
- **The "Wilson-line relaxation" changes nothing physical.** It multiplies Y_u by e^{−i·arg/3}. That leaves all ten flavour observables unchanged (max relative change 3.1e-13) and sets arg det to −3.5e-12. Since θ̄ = θ_QCD − arg det(Y_uY_d) is rephasing-invariant, the phase just moves into θ_QCD, which the model never computes. A *dynamical* relaxation would need a potential for that Wilson line, and none is given.
- **The status is unchanged:** single-sheet arg det(Y_uY_d) = **−2.9204 rad**, and θ̄ is not determined.

## Theorem 12

1. **The benchmark gate passes.** From Buttazzo Table 1 my integrator gives λ = 0 at log₁₀ μ = **9.678**, against agy's 9.676. Two unrelated 2-loop codes agreeing confirms that the factor-2 bug I reported earlier is fixed. I did *not* confirm that "9.68" is a figure published in the paper; the gate validates the integrator only, not the boundary conditions.
2. **Cross-check of agy's numbers.** With agy's inputs (gauge couplings from the Vol formulas, y_t²(M₁₂) = 1/5, λ(M₁₂) = 0) I get y_t(M_Z) = 0.951309 and λ(M_Z) = 0.128898, which agrees with agy.
3. **The matching is wrong.** agy reads m_H = √(2λ(M_Z))·v, which is tree level at μ = M_Z. It also applies the 1-loop pole factor directly to m_t^MS(M_Z), skipping the running from M_Z to M_t.
   - I ran instead to μ = 173.34 GeV and inverted Buttazzo's matching fits for λ(M_t) and y_t(M_t).
   - That gives **M_t = 169.3 GeV** against 172.69 ± 0.30, and **M_h = 120.2 GeV** against 125.25 ± 0.17.
4. **The boundary condition was chosen after the fact.** y_t²(M₁₂) = 1/5 first appears after my audit and agy's own concession showed that the fixed RGE gives 118.8 GeV. m_H is very sensitive to it:

   | y_t²(M₁₂) | 1/8 | 1/7 | 1/(2π) | 1/6 | **1/5** | 2/π² | 1/φ³ | 1/4 | 1/3 |
   |---|---|---|---|---|---|---|---|---|---|
   | m_H (agy-style tree) | 83.8 | 95.8 | 105.3 | 109.3 | **125.0** | 126.1 | 138.9 | 143.6 | 166.2 |
   | M_t (properly matched) | 146.9 | 153.3 | 158.5 | 160.7 | **169.3** | 170.0 | 177.0 | 179.6 | 192.1 |

   - The menu spans 84 to 166 GeV, and dm_H/dy_t² ≈ 370 GeV. Choosing the menu entry that lands on 125 is a fit with about 1 continuous parameter's worth of freedom; it is not a closure.
   - **What the honest content reduces to.** If M_t is set to the PDG value instead, λ(M₁₂) = 0 gives a matched M_h = 126.2 GeV. This is the well-known SM near-criticality, not a model output.
5. **M_Z/v.** The tree relation ½√(g₂² + g_Y²), evaluated with the *exact* PDG MS-bar couplings, gives 0.37165 (+0.35%), which is the precision the relation itself has. agy's +0.06% comes from compensating errors in its fitted α_em (+0.48%) and sin²θ_W.
6. **"Zero imported M_Z / m_τ" is relabelling.**
   - The gauge inputs are the Vol formulas, which were fitted to the PDG 1-loop crossing.
   - m_b and m_τ still go through the hand constants `I_top = 0.1462`, `exp(-0.0170)` and the PDG α_em / sin²θ_W inside `theorem8`.
   - `imported_MZ_count = 0` is a literal (guardrail 2).

## Theorem 13

- **The method is right, and it reproduces.** Basis invariance under Haar rotations holds at 1.7e-15. U_PMNS = U_e,L† U_ν,L is now the physical construction.
- **The result is negative.** Pulls against NuFIT 5.2 (normal ordering):

  | angle | value | pull |
  |---|---|---|
  | sin²θ₁₂ | 0.2770 | −2.5σ |
  | sin²θ₁₃ | 0.01393 | **−14.5σ** |
  | sin²θ₂₃ | 0.00029 | **−28.6σ** |

- **What this retracts.** It retracts the earlier Phase 6 "PMNS closure" (θ₁₂ to 0.22σ, and so on), which read a basis-dependent left–right overlap. The relay calls θ₂₃ "suppressed, requiring an M_R threshold"; that is a new, unpriced ingredient, and the result as computed is a failure.
- **Stale docstring.** It quotes |b₁₀|² = 1.32049e-5 and |η⁶/4| = 4.55943e-3; the code outputs 0.021434 and 0.004092.

## Tests and the "zero-trust referee" (guardrails 2 and 6)

- **Literal asserts.** The new tests assert literals and agy's own expected numbers, e.g. `imported_MZ_count == 0`, `true_eigenline_w_eig == ("2/5","1/5")`, and `abs(rel_error_mH) < 0.002`.
- **What is independent in the referee:**
  - The Theorem 11 check through `b1656_funcs` is genuinely independent.
  - The Theorem 10 check repeats the same integer arithmetic.
  - The Theorem 12 and 13 entries **echo the producer output** (`sc["theorem12_..."]`). That violates guardrail 6 for the very claims that matter, and it is why the matching error in Theorem 12 went uncaught.
