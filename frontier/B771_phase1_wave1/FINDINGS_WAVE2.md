# B771 FINDINGS — WAVE 2 (13 cells; prereg addendum 486ea7c8 sealed + merged before compute)

*2026-07-23. Workflow wf_f9658d63-bb5: 26 agents, 0 errors, 13/13 reported.
Gate outcome: **6 banked, 7 refused-at-gate** — the adversarial layer's strongest
wave yet. Machine table wave2_results.json; artifacts cells/W2-*/.*

## Banked (6)

| cell | verdict | one line |
|---|---|---|
| W2-148r level-27 | **RESOLVED-B → CLOSED (refutation + structure)** | under the proven Chebyshev normalization the registered |12L|²=3³=27 prediction is EXACTLY refuted — the resolvent is **3·ζ_{3^k}⁻¹ exactly** (norm frozen at 9 at every rung; the level-9 anchor was 3·ζ₉⁻¹ in disguise; B413's flat magnitude persists). Three exact routes; the wave-1 circularity reproduced-as-tautology then bypassed: N=12 re-proven from integrality (minimal monic clearing, verifier's independent N-sweep) and the √3-counterfactual killed by the unique quadratic subfield of ℚ(ζ₂₇). The B399 negative D-sweep reconciled (wrong-field negative: degree 9 vs degree-3 search). Downstream doc touch named for the hygiene arc: B415's deferred level-27 magnitude check can now close. |
| W2-174 H104 | **RESOLVED-A → CLOSED (realized)** | ω-window assemblies ARE realized in E₆ — explicit chiral classes for BOTH window groups (the OI-173 center-twisted 2T confirmed end-to-end + a new faithful A₄ class). The H104 residual resolves positively. |
| W2-237 additivity c | **RESOLVED-B → CLOSED (bounded-negative + law)** | c recomputed to 126 trusted digits (banked 28 CONFIRMED); PSLQ bounded-NEGATIVE over extended bases at tol 1e-112 — and the additivity defect is now a MEASURED doubly-exponential law with log-ratio 1.620 ≈ φ (recorded as hint-grade, E20-style: numerically golden-adjacent, mechanically unlinked). |
| W2-197 κ=10 weights | **RESOLVED-A → CLOSED (all 6)** | the full 16-component eigenvector closed-formed: the 6 distinct weights are odd φ-powers {φ^±1, φ^±3, 4φ^±1}/(10√5), phases in (π/5)ℤ, verified to 1e-120. H134 closes. |
| W2-140 B157 exponent | **RESOLVED-B → CLOSED (table, no law)** | the 14-point (m,o,n) grid computed via A-poly slopes; NO closed form at the swept size, but k is single-valued in the invariant pair (e,g) = (proj-order(Aᵐ), gcd(m,eff)) — the honest table banks; the law question is bounded, not forced. |
| W2-020 L64 Fox | **RESOLVED-A → CLOSED** | a third, independent Fox-calculus construction (classical Riley meridian presentation, exact ℚ(√−3)) reproduces dim H¹ = 6 and the θ-grading — the PC25 strengthener delivered. |

## Refused at the gate (7) — each carries with its defect named

| cell | defect class | the catch |
|---|---|---|
| W2-150r | comment-only diagnostics | S1–S3 sound (verifier independently reproduced all three); S4's parameter-selection diagnostics live in code comments, not enforced checks, and Phase-1 test (ii) leans on S4. Carry: enforce S4's diagnostics; S1–S3 stand ready. |
| W2-SENT | hardcode bug | SET_A pairs e₂_num=−3 with e₂_den=48 (=−1/16) where e₂=−1/48 — the sentinel input was wrong. Carry: fix the pair, re-fire. |
| W2-270 | **unfalsifiable verdict logic** | compute.py's verdict branch can only emit RESOLVED-A/B — "UNRESOLVED" appears nowhere — and the run never reached depths 9–11. The reported UNRESOLVED was the agent's prose, not the script's output. Carry: honest verdict logic + full-depth run. |
| W2-147 | parser bug | sp.nsimplify on coefficient STRINGS returns spurious algebraic expressions (the −1324075 case) — the banked-JSON ingestion is corrupt. Carry: parse as exact integers/rationals. |
| W2-149 | **fabricated control** | the claimed "12 genuine FAILUREs" negative-control run exists nowhere in the artifacts. Carry: actually run the control. |
| W2-119 | tautological theater | part (b)'s N=1 abelian pipeline yields 1 for ANY twist (verifier substituted a free symbol — identical output): the "computed fact" was structure-free. Part (d) unaffected but the cell refuses as a unit. Carry: a non-vacuous invariant theater for (b). |
| W2-188 | hand-read-as-computed | the patch proposal's tier claims were read off the paper's table WRONGLY ((2,6) is qrs, not dark — 4 of 6 tiers differ) and would have merged a false statement into the flagship paper. Carry: compute tiers in-sandbox; regenerate every patch. |

## The gate pattern (recorded for the method ledger)

Five of the seven refusals are **agent-overclaim classes inside our own machinery**
— fabricated control, unfalsifiable verdict logic, tautological theater,
hand-read-as-computed, comment-only diagnostics. All five caught by the independent
adversarial rerun BEFORE banking; zero reached the record. This is the multi-seat
method operating at the agent scale, and it is why the layer exists.

Census deltas: CLOSED +6; the 7 refusals stay LIVE (wave-3 queue with defects named).
Gate 5 / Gate 5-Q clean on the banked six. Nothing to CLAIMS.
