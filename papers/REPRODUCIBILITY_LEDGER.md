# Reproducibility ledger — every paper theorem is machine-checked (74/74 green, 2026-07-04)

Each theorem in Papers 1 & 2 is backed by an exact lock test loading a committed JSON of
exact results produced by a self-contained frontier script. Verified: `pytest` over the
locks below passes 74/74 in ~15s. No floats in the load-bearing arithmetic (exact ℚ(ζ₆₀) /
ℤ[φ] / fp-with-reconstruction); numeric only for envelope/growth comparisons, gated.

## Paper 1 (value theory)
| Thm | lock | reproducer |
|---|---|---|
| T1 order law | test_b376 (P59) | frontier/B376_*/… |
| T2 twist invariant | test_b381 (P62) | frontier/B381_twist_isolation |
| T3 trace formula / 1/12 | test_b382, test_b396 | frontier/B382_why_one_twelfth, B396_allpairs_gate |
| T4 closed form | test_b386 | frontier/B386_crt_closed_form |
| T5 locality | test_b390 | frontier/B390_criterion_tensor |
| T6 existence law | test_b377_existence, test_b377_acceptance | frontier/B377_existence_law_derivation |
| T7 root-of-unity gate | test_b404 | frontier/B404_gate_derivation |
| T8 row-16 reality | test_b383 | frontier/B383_row16_reality |
| T9 Galois covariance | test_b379, test_b380 | frontier/B379_*, B380_* |
| T10 class-field organization | test_b401 | frontier/B401_sixth_angle |
| T11 walls | test_b408, test_b413, test_b400, test_b422 | frontier/B408, B413, B400, B422 |

## Paper 2 (the trinity)
| Thm | lock | reproducer |
|---|---|---|
| T1 cornerstone | test_golden_cat_map_principle (+B67 banked; Reid 1991 cited) | knowledge/… |
| T2 dynamics | test_b416 | frontier/B416_tw2_dynamics |
| T3 symbolic | test_b417 | frontier/B417_tw3_symbolic |
| T4a dynamical zeta=periodic orbits (golden, monodromy) | test_b423, test_golden_cat_map_principle | frontier/B423_gateB_torsion |
| T4b geometric torsion at holonomy (Eisenstein, −3; = V30/V31 Porti form) | test_b425 | frontier/B425_geometric_torsion |
| T5 Hessian | test_b424 | frontier/B424_gateB_hessian |
| T6 quantum invariant | test_b419, test_b384 | frontier/B419_tw5_quantum, B384_kashaev_bridge |
| T7 measure | test_b413, test_b415 | frontier/B413_scale_genesis, B415_behavior_tracking |
| T8 L-function | test_b420, test_b401 | frontier/B420_tw6_lfunctions, B401_sixth_angle |
| T9/10 walls | test_b408, test_b422 | (shared with Paper 1 T11) |

## Standing
Deferred footnote: e₃ (the 1215 singles-tower triple's third symmetric function) — its sum
rule (e₁=0) and e₂=−1/48 are exact; the exact e₃ ∈ ℚ(√5) needs a lattice reconstruction
beyond brute exact-LLL (a computational footnote, not a theorem). Everything the papers
assert is green.
