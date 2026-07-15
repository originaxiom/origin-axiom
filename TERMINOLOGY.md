# TERMINOLOGY — the project's inner vocabulary, glossed (Review 18, 2026-07-15)

This project developed a working vocabulary across hundreds of AI-assisted
sessions. **These are INTERNAL WORKING NAMES, not established mathematical
terminology.** Every load-bearing statement behind a name below is banked as
ordinary mathematics in the referenced artifacts. If a term reads poetic,
that is what it is — the mathematics is in the definition column.

| Inner term | What it actually is |
|---|---|
| **the object** | The figure-eight knot complement 4₁ (once-punctured-torus bundle, monodromy [[2,1],[1,1]]), and by extension its character varieties and quantum invariants. |
| **bank / banked** | Committed to the repository with a passing lock (test) and ledger entries; the project's unit of "result". |
| **B-number (B598, …)** | A banked frontier arc, numbered sequentially; lives in `frontier/B*/FINDINGS.md`. |
| **seat / chat-N / cc2** | One AI assistant session among several run in parallel by the owner; seats cross-check each other (INTERNAL verification — see `PROVENANCE.md` §0). |
| **lock** | A pytest test that recomputes a banked fact (heavy ones gated behind `OA_SLOW=1`). |
| **gate** | A repo-wide consistency check (`scripts/gates/`), or, inside a script, a failure-enforcing assertion. |
| **prereg / sealed** | A preregistration document written and SHA-256-hashed before the outcome-bearing computation runs (`ARTIFACT_HASHES.txt`). |
| **firewall** | The governance rule separating mathematics from physics speculation: no Standard-Model quantity is claimed from the mathematics; speculative motivation lives quarantined in `speculations/`, `philosophy/`. |
| **the stage** | A finite quantum model attached to the object: theta functions / Weil representation at level κ, or an affine-Lie-algebra modular datum (e.g. SU(3)₂ ↔ "golden stage" κ=5; "E₆ level 2" = E₆₂). |
| **the fold / θ** | The order-2 outer automorphism (diagram fold) of E₆; "θ-even/odd" = its ±1 eigenspaces. f₄ is the fixed subalgebra. |
| **the dial** | The six peripheral-centralizer directions v_m (one per adjoint block V_m of e₆ under the principal sl₂, m ∈ {1,4,5,7,8,11}); "θ-odd slots" = m ∈ {4,8}. |
| **the weld / the double** | The figure-eight glued to its mirror along the cusp torus (the mirror-double), optionally with a twist exp(t·v_m) at the gluing ("bending", Johnson–Millson). |
| **hearing / deaf** | Whether a (twist-)deformed amplitude differs from the untwisted one at order ε²: "the hearing law" A^tw − A^plain = −2ε²(u†M_odd u) (B593); sectors where this vanishes identically are "deaf". |
| **the sign-flip theorem** | P_odd·C = −P_odd: conjugation flips the θ-odd block of the open weld matrix exactly (B592-OPEN). |
| **the clock** | The order of a monodromy image in a finite stage (e.g. ord(ρ(A₁))); "the clock is not the cat-map period" = B596's null. |
| **width / τ-labels** | Reidemeister-torsion magnitudes per block; used as non-degenerate labels ("width-respect" = a map must not permute them). |
| **the chain / readiness chain** | The 9-step audited checklist (B598) that had to be fully green before the sealed P3 comparison was allowed to run. |
| **arc / campaign** | A themed sequence of banked steps (e.g. "the L85 campaign" = the D1 existence question). |
| **L-numbers, K-numbers, P-numbers, PC-numbers, S-numbers** | Ledger indices: open leads (L), knowledge notes (K), proven claims in `CLAIMS.md` (P), paper candidates (PC), synthesis sessions (S). |
| **the universal boundary ratio** | I_λ/I_μ = −2√−3: the gauge-invariant content of the peripheral restriction, equal at all six blocks (B598 step 3). |
| **the hearing lines / the two integers** | The θ-odd bending responses: rank-2, supported on m ∈ {4,8}, column law N₄(1+√−3) / N₈(1−√−3) with N₄ = 2⁹·3²·5·7·13, N₈ = 2¹⁵·3⁵·5³·7²·11 (B598 step 4b). |
| **outcome A/B/D** | The locked verdict table of the sealed P3 prereg (existence / structure-with-recorded-defect / no map). L85 resolved as B. |
| **vacuity check (MB12)** | The rule that a preregistered test must be able to both pass and fail — applied to the target, the OPERATION, and the CRITERION (two sealing errors of exactly this kind are on record in B598, amended with hashed errata). |
| **verify-don't-trust** | Every cross-seat claim is recomputed in-sandbox before being banked, including claims marked "verified" by another seat. |

For how verification works and what it does NOT imply, read `PROVENANCE.md`
§0. For how to run the checks yourself, read `REPRODUCIBILITY.md`.

## The four mirror manifolds (permanent names; audit Gate 2, 2026-07-15)

No invariant may be transferred between these without an explicit map.

| name | construction | H₁ | notes |
|---|---|---|---|
| **M_Sol(−A₁)** | the closed torus bundle of the mirror-twisted lift −A₁ | ℤ ⊕ ℤ/5 | SOL geometry (B591-M5); the conductor carrier; the C-twisted quantum play (Z_C = +1/φ) |
| **L(5,2)** | the branched double cover Σ₂(4₁) | ℤ/5 | the classical mirror-pairing manifold (B591-M3) |
| **D_g(M)** | the cusp-complement double M ∪_g M̄ per explicit gluing g | g = ±I → ℤ; g = ±A₁ → 0 (homology sphere) | ±A₁ is peripherally INCOMPATIBLE with the banked 27 local system; the B605 D₄-intertwiner gluings are named D_g(M) with g stated |
| **D_bent(M; m)** | the representation-bent B582/B598 amalgam at bend m | — (local-system object) | h¹(D;27) = 2 at m = 4, 8; 5 at none/1/5/7/11 (B635-reproduced) |
