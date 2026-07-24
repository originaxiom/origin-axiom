# B775 FINDINGS — PHASE 2 WAVE 2 (8 structural cells; addendum cc7e3b48)

*2026-07-23. Workflow wf_aa0b4622-1f6: 15 agents. **6 banked, 1 downgrade-carry, 1
dropped** (P2W2-DARKHYP hit the structured-output cap — re-runs in Wave 3). cc
hand-verified the MIRROR empty-set + (2,3) stabilizer. Machine table wave2_results.json.*

## Banked (6)

| cell | verdict | result |
|---|---|---|
| **P2W2-MIRROR** | **RESOLVED-A** | TWO mechanisms, each reproduced twice. (A) the mirror is NON-Galois because it is the ANTI-diagonal axis map (a,b)→(a,−b): realizing it as a diagonal index-scaling σ_c needs c≡1 mod 20 AND c≡−1 mod 12 — impossible (1≢3 mod 4, empty set, hand-verified) — so the mirror is carried only emergently as field conjugation τ₃ after the DFT. (B) the (2,3) stabilizer is exactly **Gal(ℚ(ζ₆₀)/ℚ(√5))** = the √5-fixing half-group {1,11,19,29,31,41,49,59}, via the phantom unit **49** (uniquely index-and-value-trivial at orders (12,6)). |
| **P2W2-PADIC** | **RESOLVED-A** | the single-seed tower measure is 3-adically BOUNDED, so its Amice–Mazur p-adic L-function A_μ(T)=Σc_n T^n EXISTS in ℤ_3[[T]] — computed (unblocked by the exact e₃). |
| **P2W2-GIESEKING** | **RESOLVED-A** | B469 Phase 2b CLOSES: the parity column is completed and the Gieseking non-orientable descent goes through for both family-ends. |
| **P2W2-DARKBRIGHT** | **UNRESOLVED → partial/EXTERNAL** | a verified EFFECTIVE bright/dark test exists, but no closed-form seed criterion — the effective test banks, the closed form is the EXTERNAL residual. |
| **P2W2-PERLETTER** | **RESOLVED-B → TOMBSTONE** | **no non-arbitrary per-letter hearing weight is forced**: the hearing amplitude factors as q(RL)=θ_fund·q(L) with the per-letter split a FREE knob. The one legitimate H-ITERATED-HEARING path (after the α_s kill) is tombstoned — the weight is not object-derivable. (Gate 5: no SM comparison; the pin untouched.) |
| **P2W2-SPECTRIPLE** | **RESOLVED-B → formulation obstruction** | the Connes triple is FORMULATED precisely (A=R(E6) character ring, D=Fox-coboundary on the figure-eight E6-cochain complex) but a formulation obstruction is named (the specific gap) — an honest boundary, not a hidden gap. |

## Downgrade-carry (1)
| cell | the catch |
|---|---|
| **P2W2-LATIN** | claimed the WHOLE hearing-matrix Latin square is FORCED by the ℤ/3 simple current — **downgraded to RESOLVED-B** by the verifier's B772-class catch: only the CURRENT ROW is genuinely forced (=√3·S00·qd-vector, exact); the other two rows' 3-valuedness is MEASURED (the brute B629 fact), and "orbit-constancy ⟹ 3-valuedness" is a non-sequitur — an explicit NON-Latin solution exists in the 1-parameter family. **Honest status: the Latin square is confirmed exact and its current row explained by the ℤ/3 center, but NOT forced end-to-end by E6₂ fusion.** The forcing overclaim is the cell's whole point, so it carries; the genuine partial (current-row derivation) is real. Re-run in Wave 3 targeting only the non-current-block 3-valuedness. |

## Dropped (1)
P2W2-DARKHYP (the N=p² dark-hyperbola all-p proof) hit the structured-output cap with
no verdict — re-runs in Wave 3.

Gate 5 / Gate 5-Q clean. Nothing to CLAIMS; the one-number pin untouched.
