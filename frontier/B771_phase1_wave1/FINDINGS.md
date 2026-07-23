# B771 FINDINGS — PHASE 1, WAVE 1 (13 cells; prereg 7955049f sealed first)

*2026-07-23. Workflow wf_a76cd64a-384: 25 agents; every returned verdict
adversarially verified by an independent rerun; cc spot-verified OI-031 (identity
residual 0 to 167 digits), OI-200 (minpoly reproduced verbatim), OI-186 (Fricke 15)
by hand. Cell artifacts under cells/OI-xxx/; full machine table wave1_results.json.*

## The wave table — 11 verdicts banked, 2 cells carry

| cell | verdict | one line |
|---|---|---|
| OI-055 B685 3-int | **RESOLVED-B → EXTERNAL** | the conditional kill PROVED all-n in-cell (5 inert in ℤ[ω], norm valuation ≥0 vs the hearing law's ≥1); the single premise (all-order 3-integrality) is EXACTLY the GSWZ Habiro-ring theorem (arXiv:2412.04241) — obstruction computed, not asserted: prime support of the r-stream grows (no termwise induction), pure-3 fails in the h-variable, and a ℤ-perturbation breaks pure-3 while preserving every formalizable feature. Depth extended u⁵→u⁷; r₆ recognized on two disjoint ladders; the pre-derived Q₆ congruence prediction VERIFIED (pin+25); r₇ honestly stopped. Verifier reproduced r₁–r₆ on a THIRD disjoint ladder with fresh code. |
| OI-031 B399 e₃ | **RESOLVED-A → CLOSED** | **e₃ = cos(2π/9)/864 exactly** — the depth-5 triple cubic closes as t³ − t/48 − cos(2π/9)/864, roots {cos(2πk/27)/6 : k=1,10,19}; u=12t gives u³−3u = 2cos(2π/9): **the level-1215 triple IS the ζ₂₇ rung of the Chebyshev trisection tower**. Three independent routes (CRT/LLL batch-split on the 20 banked primes; exact symbolic in ℚ[z]/Φ₂₇; from-scratch float 13.8 digits). Named follow-up: run the armed B403/B405/B406 sentinels on this value (Wave 2). |
| OI-043 −1/16 sum | **RESOLVED-A → STALE** | census-lag: the CRT closed form was already proven (B386/P66); re-derived in-cell to confirm; the ROADMAP checkbox was the stale surface. |
| OI-063 L39 | **RESOLVED-A → CLOSED (theorem)** | the all-t symbolic Gauss-sum proof of P(γ)=lcm(t−2,t+2)/content(γ) completed via the exact two-sector form of the WRT trace; L39 promoted from exhaustive-at-f=8 to theorem. |
| OI-092 genus-2 CS | **RESOLVED-A → CLOSED** | the re-run succeeds (the historical None was a usage artifact): vol equal, CS opposite, CS≠0 — the banked orientation-reversal structure numerically confirmed on two triangulations. |
| OI-146 B332 index | **RESOLVED-B → CLOSED (refutation)** | the quarantined [Γ:Γ∩gΓg⁻¹]=3 is REFUTED: the true index is **10**, confirmed 5 independent ways. The quarantine resolves as a kill. |
| OI-148 level-27 μ∞ | **VERIFY-REFUTED → stays LIVE** | the verifier caught a circular scale choice: N=12 was tautological given banked e₂=−1/48 and contradicted by B399's own negative D-sweep. NOTE: OI-031's identification retroactively supplies the true normalization (the Chebyshev form) — the cell re-derives under it in Wave 2. The 9-vs-27 arithmetic is real; what it compares is not yet established. |
| OI-150 B178/B171 | **REPORT-LOST → re-run Wave 2** | the compute ran to completion on disk (1467s; weak-coupling rank-3 gaps corroborated on two metallic pairs) but the structured report died and the run's own check-labels are ambiguous; re-runs clean rather than hand-reconstructed. |
| OI-151 torsion-one | **RESOLVED-A → CLOSED** | det(N−I)=2−tr(N) proven basis-free in SL(2); applied to the trace-map Jacobian's transverse factor (independently re-derived, not the assumed companion form). |
| OI-173 H103 | **RESOLVED-B → CLOSED (refutation)** | **Level 3 IS reachable**: the center-twisted trinification ρ'(g)=ω^{ε(g)}·ρ_b(g) is a non-σ-stable (chiral) 2T subgroup of E₆ with 27|_2T giving n₁=9≠n₂=0 — the hoped-for clean theorem is dead by explicit counterexample. |
| OI-186 H112 | **RESOLVED-B → CLOSED (independent)** | the family law **tr(A_mA_n)=(mn)²+(m+n)²+2** is exact (15 at (1,2)); but the seam-conductor pairing dies at m=2 (seam(2)=8 unattainable) and beyond — the two 15s are INDEPENDENT; base-rate honesty held. |
| OI-189 H115 | **RESOLVED-A → CLOSED (promoted)** | g_n = D^{n−1}(g₁) reconstructs e_n = det(I−M_n) exactly for n=2..5 with the resultant-transitivity lemma proven symbolically — the n=1 closed form promotes. |
| OI-200 D4 ceiling | **RESOLVED-A → CLOSED (identified)** | **1.7849887… = √(5+2√3−2√2−√6)**, minpoly x⁸−20x⁶+98x⁴−172x²+97, verified both directions to 120 digits after an independent recompute (not trusting the banked 8 digits). The last unidentified ceiling value falls. |

## Gate notes
- The verification layer earned its keep twice: OI-148's circularity catch (upheld=false
  with the in-repo contradiction named) and OI-055's third-ladder reproduction.
- Census deltas (census.json stays frozen; this table is the delta record): CLOSED +9,
  STALE +1, EXTERNAL +1 (OI-055 with its in-cell theorem banked), LIVE −11+2 carries.
- Wave 2 inherits: OI-148-r (re-derive under the OI-031 normalization), OI-150-r
  (clean re-run), the B403/B405/B406 sentinel firing on e₃, and the remaining
  mechanical rows per the prereg.

Gate 5 / Gate 5-Q clean on every cell (verifiers grepped). Nothing to CLAIMS.
