# R23: the source operator supplies normalized anomaly transport, not a boundary completion

## VERDICT AS THE SEAT STATES IT
"The existing charged differential is explicitly mapped to the two-flavour mass operator used in anomaly-inflow calculations. Its mass direction supplies an integrally normalized angular form... This constructs a specific local anomaly-transport candidate from the same operator, not another appended list of fields. It does NOT yet construct the global singular determinant or its boundary sector. Even granting perfect local inflow, dropping the outer-boundary term would fake cancellation of the three-spinor gauge-zero-mode anomaly."

## DECLARED INPUTS AND HYPOTHESES
- Banked identity: "R16's actual exterior/adjoint operator, R18's declared strong maximal complex, R19/R20's charged adjoint sector and R21's root-derived anomaly polynomial." R22 is named as leaving "actual source/inflow as the next join."
- Sourced literature: Kanno–Sugimoto (arXiv:2106.01591) §2, 3.2, 4.1.3, 4.3; Choi–Ohmori (arXiv:2205.02188) (3.21) §3.3.2; Braun et al. (arXiv:1812.06072) (2.2),(2.41)–(2.49) App. A.2; Pantev–Wijnholt (arXiv:0905.1968) §3.4 — "Full relevant sections... read."
- Scope (P0): "the specified commuting charge-q Witten operator on the smooth source complement, local normal charts and compact regulated regions. Local statements at nondegenerate zeros do NOT assume that the actual global source has exactly three such zeros."
- Assumed/expected (P6): "expect a positive local mass/Clifford identification and a unit, not doubled, local angular response. Expect bulk descent to cancel a localized anomaly only by retaining an equal boundary obligation... Expect the whole-torus-to-partition inference in incoming B1351 to fail on explicit relative cochains."
- Seals: original **a726252a**; separate bundle-control seal **2684623c**.

## CONTROLS
- "Known zero, orientation-reversed, conjugate, nontrivial-regulator, and boundary-retaining controls are mandatory."
- Doubling/square-root rejection: "exact controls reject doubling and an extra square root" on the Pfaffian identity fixing the local counting factor.
- Frame-covariance control: "A position-dependent unitary frame change preserves K when Gamma is transformed too; omitting it reverses the displayed local sphere density in the control."
- Gauge-invariance control on the descent argument: "For a gauge parameter constant internally, Stokes gives total outer flux=sum nu_a, so this bulk term's gauge variation is ZERO... Opposite defects with zero total charge also pass the cancellation control."
- Receiving control on incoming SM claim B1351: constructs the disc-partition relative complex and shows "cohomology of a whole torus cannot replace the cohomology of its partition," verified with "exact i and cube-root characters" plus "the trivial-character control" and an essential-annulus control that stays acyclic.

## TESTS ON THIS BENCH
```
24 passed in 7.86s
```
(`tests/test_physical_bridge_mass_inflow*.py`, from `<audit worktree @ 5e063851>`; covers both the original operator/transport module and the separately sealed bundle-control module). No failures.

## CLAIMS FOR MAIN
1. The R16 exterior/adjoint operator maps exactly onto a two-flavour Clifford mass-Dirac operator with kinetic symbol −σ·∂ and Hermitian mass m·σ — PROVED-BY-SEAT (own exact computation, checked against original operator).
2. The induced mass-eigenline first Chern form integrates to exactly ±1 on a reference sphere (unit angular response, not doubled) — COMPUTED.
3. Bulk anomaly descent from this operator cancels a localized charge only by transporting the identical charge to the outer boundary; a globally-constant gauge parameter leaves this bulk term's variation exactly zero — PROVED-BY-SEAT (within the stated Stokes/CS5 setup).
4. An incoming SM-seat claim ("B1351": whole-cusp-torus acyclicity forces zero index for every Morse partition) is refuted on explicit relative cochains for a disc partition (H*=(0,k,0,0), χ=−k) — COMPUTED, explicitly scoped as "not a physically selected disc boundary."

## CONFLICTS WITH MAIN
Searched main's `docs`/`frontier` for "B1351" and "acyclicity." Main's own current B1351 (frontier/B1411_the_sm_seats_v10_arcs_harvested/FINDINGS.md) is a *different* statement — about vector-like Wilson-line pairs on a *closed* three-manifold (h¹(Yₙ;ψ)=h¹(Yₙ;ψ̄), Poincaré duality) — not the "whole-cusp-torus acyclicity forces zero index" claim this round attributes to "SM B1351 at ce5ca412." The "acyclicity" hits found in `docs/RELAY_LEDGER.md` and `frontier/B1157_dynamics_null/` concern an unrelated Sym-power/Ruelle-zeta torsion refutation. This looks like a cross-seat B-number collision (memory already flags "three collisions" in the harvest queue) rather than a same-claim conflict; main's own record does not currently carry the specific "acyclicity forces zero index for every Morse partition" statement this round rebuts, so no direct contradiction was found either way. CONFLICT: none located, but the B1351 label itself is ambiguous across seats — flag for reconciliation.

## WHAT MAIN WOULD HAVE TO VERIFY
Reproduce the U-matrix/Clifford identification and the K/Chern-form integral independently; recheck the CS5 descent's boundary bookkeeping (outer + source-tube + corner terms); and resolve which seat's "B1351" is meant before treating the acyclicity refutation as bearing on any specific main claim.
