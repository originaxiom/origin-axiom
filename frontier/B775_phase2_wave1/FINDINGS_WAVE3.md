# B775 FINDINGS — PHASE 2 WAVE 3 (8 structural cells; addendum a8a8bd82)

*2026-07-24. Workflow wf_64d54a0e-529: 16 agents. **7 banked, 1 carry.** cc hand-checked
the OCTA/L56/L53 claims. Machine table wave3_results.json.*

## Banked (7)

| cell | verdict | result |
|---|---|---|
| **P2W3-L53** | **RESOLVED-A → formality** | E6 all-orders local smoothness REDUCED to named theorems (Menal-Ferrer–Porti + Poincaré–Lefschetz half-lives-half-dies + Kostant), with an independent pure-python certificate: h*(4₁,e6)=(0,6,6), meridian regular (ker(μ−I)=1 per Kostant exponent, total 6=rank E6), dim H¹(M)=6=½·dim H¹(∂M) forces the restriction Lagrangian-injective ⟹ smooth 6-dim germ filling H¹ ⟹ the Goldman–Millson map vanishes to all orders (unobstructed). L53 closes. (Verifier's 2 non-material flags noted: "formal" is loose for "unobstructed"; the E6-MFP is assembled from Kostant+PL rather than black-boxed — both terminological.) |
| **P2W3-SL5** | **RESOLVED-B → EXTERNAL** | the SL(5) ε-pinv route reproduces k=2 (char(M²)) at multiplicity 1 but STALLS on the second copy at the pinv-discontinuity — the known B81 doubly-degenerate wall. The numerical tower is genuinely EXTERNAL at SL(5) (the exact-symbolic k stays NEEDS-SPECIALIST). |
| **P2W3-OCTA** | **RESOLVED-A → structural** | a GENUINE octahedral parent EXISTS for the conductor-40 family: the projective mod-3 Galois representation of the figure-eight has image the octahedral group S₄ (order 24). The B225-revived question resolves POSITIVE — there is a real octahedral parent, not the disc≡a² tautology. |
| **P2W3-S031A** | **RESOLVED-A → sealing generalizes** | the SL(3) φ-fixed locus is ENTIRELY REDUCIBLE at the full locus (all eigenvalue strata) — no irreducible fixed point; the S031a sealing conjecture generalizes to the full locus. |
| **P2W3-N1** | **UNRESOLVED → partial** | eₙ mod 5 is provably a SQUARE (residues 2,3 excluded via the golden-norm + ramification of 5 in ℚ(√5)); the mod-7 exclusion does NOT close (the norm argument is 5-specific). Partial result banked, mod-7 the residual. |
| **P2W3-H4** | **RESOLVED-B → EXTERNAL** | object-natively, arithmeticity is SCATTERED across the metallic tower ({m=1 ℚ(√−3), m=2 ℚ(i)}, off-family RRL/RLL ℚ(√−7)); there is no object-native reason the figure-eight is uniquely minimal along arithmeticity — that is Reid's separate deep theorem (the figure-eight is the unique arithmetic knot). EXTERNAL, honestly. |
| **P2W3-L56** | **RESOLVED-A → reality THEOREM** | the gauge-invariant triple-phase class tr(P_iQ_jR_k) is PROVEN real for all 605 triples via a structural *-argument (Hermiticity/conjugation-invariance) — no longer just numerically-real, a theorem. |

## Carry (1)
| cell | the catch |
|---|---|
| **P2W3-1/4WALK** | the CRT mechanism is GENUINE (W1 = A⊗B factorizes exactly, discriminating — verified), but the load-bearing headline "the frozen 1/4 is the CRT-product of a CONSTANT 5-local × growing 3^k-local" is CONTRADICTED at N=405 (the cell's own next rung — the 1/4 doesn't persist there). The MECHANISM (CRT/Weil-rep tensor factorization) banks; the "frozen forever" framing over-claimed. Carry: re-frame as "the support walk is CRT-multiplicative; the 1/4 holds at N=15,45,135 but not N=405" — the walk mechanism is real, its frozenness is level-bounded. |

## What this wave produced
Two theorems (L53 formality-reduction, L56 reality), one structural positive (OCTA — a
genuine octahedral parent), one sealing-generalization (S031A), two honest EXTERNAL walls
(SL5 pinv-discontinuity, H4 = Reid's theorem), one partial (N1 mod-5 proven / mod-7 open),
one carry (the 1/4-walk mechanism real, its frozenness level-bounded).

Gate 5 / Gate 5-Q clean. Nothing to CLAIMS.
