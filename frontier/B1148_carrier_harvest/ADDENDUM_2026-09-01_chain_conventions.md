# ADDENDUM (2026-09-01, fresh physics seat; finding for the banking seat to re-verify) — the printed chain "6615 → 4 → 1" mixes conventions; in the full ordered tensor the su(3)³ rung is 9, and the theorem is unchanged

**Scope.** This note corrects the *prose* of memo 48 (`FINDINGS.md` lines 20 and 41–42) and
nothing else. The endpoint theorem (Y = ε⊗C unique, survivor automatically symmetric) is
confirmed by independent blind code. The banked FINDINGS and `b1148_results.json` are left
unedited; nothing here is banked by this seat.

## Recomputed (Ring R3 cell R22, `reports/fresh_physics_seat_2026-09-01/recompute/R22_harvest_chain/`; exact, own construction)

| rung | banked | recomputed | status |
|---|---|---|---|
| π₁ alone, invariant trilinears on Ψ×Ψ×27, Ψ = C²⊗27 | 6615 | **6615**, four ways: sl₂ Clebsch count; direct nullspace on the full 78 732-dim ordered tensor (16 470 weight-zero unknowns, rank 9855, two primes); fixed space of the figure-eight holonomy over ℚ(ω); fixed space of the finite 2T image | MATCH |
| + trinification su(3)³ | 4 ("memo 35 × the unique ε") | **9** in the full ordered tensor = ε ⊗ {det A, det B, det C, and the six orderings of tr(ABC)}; its 27-symmetric (Sym³) part has dimension **4** = ε ⊗ {det A, det B, det C, tr ABC} | MATCH under memo 35's Sym³ convention; **9 ≠ 4** if read as "full tensor, no symmetry assumed" |
| + full e₆ | 1, 270 ordered triples, survivor automatically symmetric | **1**; 78 own e₆ generators (stabilizer of the cubic in gl(27), exact 2475×729 nullspace); survivor support 270/270, coefficients {−1,+1}, automatically symmetric, = ε ⊗ I exactly, antisymmetric under Ψ↔Ψ | MATCH (also = R14) |

## What is wrong in the prose (R3_REPORT D11)

1. 6615 and 1 are full-ordered-tensor counts; **4 is memo 35's Sym³ count.** The certificate
   does not compute the middle rung — it reuses memo 35 × ε. The phrase "the trinification
   gauge cuts to 4 … no symmetry assumed" is therefore not what was computed. The honest
   all-full-tensor chain is **6615 → 9 → 1**; the honest all-Sym³ chain would have a different
   first rung. Either is fine; the mix is not.
2. "by DIRECT full-tensor nullspace" applies only to the e₆ rung. The cert's 6615 is a Clebsch
   count from the sl₂ content (Ψ|_diag = 6·1 + 15·½ + 6·0; 27 = 6·½ + 15·0). R22 now supplies
   the direct 78 732-space nullspace for 6615, two primes.

The theorem is unchanged: endpoint 1, survivor ε⊗I, symmetry is an *output* of the e₆ rung
(the 270-support survivor is automatically symmetric). Error-class: E23 (convention mixing in
prose), not a computational error.

## Committed-tree fence (not a finding)

B1148's certificates live only on `origin/claude/outside-bench @ d3c99640`; the π₁ action on
the 27 is not defined in the committed tree. R22 pinned it blind (holonomy a = [[1,1],[0,1]],
b = [[1,0],[−ω,1]] over ℚ(ω); C² = the holonomy's fundamental) and confirmed it post-run.
**Proposal (owner action):** land the certs on main so the arc's numbers have a generator in
the committed tree.
