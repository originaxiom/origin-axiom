# B771 FINDINGS — WAVE 3 (13 cells: 7 wave-2 carries + 6 fresh pool)

*2026-07-23. Workflow wf_38367171-452: 26 agents, 0 errors, 13/13 reported.
Gate: **7 banked, 6 refused**. cc hand-verified W3-SENT (minpoly x³−3x+1, e₂
support {2,3}), W3-147r (1324075 = 5²·52963), W3-119r (SnapPy: 4₁(5,1) ≅
4₁(−5,1), the oriented mirror pair). Machine table wave3_results.json.*

## Banked (7)

| cell | verdict | one line |
|---|---|---|
| W3-SENT | **RESOLVED-A → CLOSED** | carry-fix: the e₂ pair corrected (−3/48→−3/144=−1/48); all three sentinels (B403/B405/B406) re-fired on the true (e₁,e₂,e₃) — none fires (Set-A prime pool {2,3}; 17,31 absent). The e₃ sentinel question closes clean. |
| W3-147r | **RESOLVED-A → CLOSED** | carry-fix: the nsimplify string-parse bug found and fixed (exactly one corrupted B581 coefficient — Δ₅'s t³ term, 1324074 vs the true 1324075); T_m(n) recomputed, the adjoint-twisted cyclic-cover torsion is a canonical rational integer (no forced choice) — S032-A Gate A evidence extended. |
| W3-149r | **RESOLVED-A → CLOSED** | carry-fix: the fabricated control is now REAL — 108/108 genuinely-constructed mismatched-κ gluings actually fail closure (0 unexpected successes); κ=tr[A₁,B₁]=tr[A₂,B₂] confirmed the sole interior-1↔interior-2 coupling on the genuine genus-2 surface. |
| W3-119r | **RESOLVED-A → CLOSED** | carry-fix: the tautological theater made non-vacuous (the E₆ twist now enters via link monodromy ω^{ab}, validated where the invariant is not identically 1); part (d) **the Meyerhoff ±5 filling is an ORIENTED MIRROR PAIR** (4₁(5,1)≅4₁(−5,1), hand-confirmed). |
| W3-188r | **RESOLVED-A → CLOSED (patch proposal)** | carry-fix: every S4.3 tier now COMPUTED from the interaction-form definition (two independent routes, 0/36 disagreements with the paper) — the hand-read errors that nearly corrupted the flagship are gone; the κ-naming patch proposals regenerated, all claims computed. |
| W3-068 | **RESOLVED-A → CLOSED** | L11: the metallic bundles' trace-field content lifts predictably to all rank-2 covers (9/9 base/cover pairs — the cover's trace field is the predicted extension). |
| W3-082 | **RESOLVED-B → CLOSED** | N6: the classical (IKZ) Rédei triple symbol is flatly inapplicable to 11≡3 mod 4; the general Rédei–Reichardt 4-rank machinery (the true twisted form) gives the exact gap at p=809. |

## Refused at gate (6) — all carry with defects named

| cell | class | the catch |
|---|---|---|
| W3-270r | **not-done (repeat)** | output truncated at depth 9 again; never reached 10–11; no results.json — the SAME Wave-2 defect. The ≈1.204 vs 1.176 refutation is real but the identification is not run. Carry: run to convergence on a dedicated (uncontended) pass. |
| W3-017 | **overclaim (real)** | Class 10 of the L6a4 SL(3) census falsely reported EMPTY — the verifier found SVD-verified points there (two seedings), contradicting the cell's "17/17" and B461's addendum. The Ruelle gap ≥0.19 leg is sound; the census leg is not. Carry: fix the class-10 solve. |
| W3-150r | math-sound, no verdict block | S4 fix genuine and enforced (verifier confirmed), but compute.py has no VERDICT logic — RESOLVED-A is agent prose, not script output. Carry: add the verdict block (allow-list the 2 known S2 secondary diagnostics with a stated reason). |
| W3-067 | math-sound, framing overclaim | the K016-expected negative (classical fields do NOT fuse to ℚ(ζ₁₂)) is correctly computed; "5 independent seeds" mislabels 5 distinct words as statistical seeds. Carry: reframe as 5 words, one method. |
| W3-078 | math-sound, verdict logic | the KMS ladder βₙ=log λ_PF closed form (λₙ=λ_{n−1}(1+√λ_{n−1}), 3/2 growth) is genuine, but the verdict branch can't emit RESOLVED-B (self-fulfilling). Carry: honest verdict logic. |
| W3-084 | math-sound, missing decisive gate | the AP complex (b₁=4, Ȟ¹=ℤ⁴) is genuinely computed, controls pass — but it never gates on whether the 1-collar actually FORCES the border (the decisive K-theory check). Carry: re-run forces_border() on the collared system. |

## The gate pattern (method ledger)
Four of six refusals are "correct mathematics, incomplete house-method compliance"
(no verdict block, framing overclaim, self-fulfilling verdict, un-gated decisive
condition) — cheap fixes, math ready. Two are substantive (not-run; a false-empty
census class). Zero unearned closures reached the record. The verify layer's
signal is now well-calibrated: it passes clean math (7) and holds process/overclaim
gaps (6) without false rejects.

Census deltas: CLOSED +7 (2 of them carry-fixes completing Wave-2 refusals);
6 stay LIVE (Wave-4 queue). Gate 5 / Gate 5-Q clean on the banked seven.
Nothing to CLAIMS.
