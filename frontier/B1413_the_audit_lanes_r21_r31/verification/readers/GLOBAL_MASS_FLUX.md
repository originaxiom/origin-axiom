# R24 — the actual sourced field has nonzero total mass-eigenline flux

## VERDICT AS THE SEAT STATES IT
"The global boundary charge is computed, not inferred from three assumed Morse points. In R15's specified positive-source class, with every cusp incident to a source, the actual field obeys integral_(whole rounded boundary C) K = sign(q) * k... the existing three-arc construction has total flux +3 at positive charge. This is the same signed net chirality as R18/R19's conditional relative spectrum. The source selection, singular-domain law and quantum boundary completion are NOT consequences of this integer." Explicitly: "not an independently reviewed physical TOE."

## DECLARED INPUTS AND HYPOTHESES
- Banked identity: "R15's global commuting sourced field; R18's strong maximal charged complex; R19's relative spectrum; R23's faithful Clifford map and covariant positive-mass eigenline. These inputs are not inferred from numerical Chern–Simons values or selected here."
- Sourced: Nie, arXiv:0909.4754v2, eqs. (1.4),(1.5),(2.2)–(2.12), Remark 1.12, "the complete paper was read," for the index/secondary-Euler identity.
- Scope (P0): "orientable finite-volume hyperbolic three-manifolds with a finite specified family of disjoint proper geodesic source arcs, positive constant densities and at least one endpoint on every cusp... Mixed-sign sources and empty-end cusps are outside the positive-boundary-sign statement."
- Assumed/expected (P6): "expect a positive identification K=-Phi with the secondary Euler form, and total flux sign(q)*k for k prescribed arcs... expect no physical selection of k=3 and no automatic cancellation of the resulting gauge anomaly."
- Seals: original **d304e2b0**; source-informed equality control **833b939b**.

## CONTROLS
- Bundle-map controls: "Missing the second spin factor, reversing the sign, and exchanging two connection components each fail exactly."
- Sign/orientation controls: "Controls independently integrate K to -1 on the outward unit sphere... mass reversal gives +1."
- Curved-frame cancellation control: "On a horosphere with n vertical, the two terms are +1/(4*pi*z^2) and -1/(4*pi*z^2): K=0. Dropping either term produces a false nonzero answer."
- Corner/seam controls distinguishing incoming region by charge sign, and "a constant field on a ball has a disc incoming region and zero flux, while outward/inward radial fields give -1/+1; these controls reject dropping a genuine disc's Euler contribution."
- Cap-sign exhaustion control: "the failure of the cap-sign inference when b=0. A cusp without a source endpoint is outside the stated positive-sign theorem."
- **Retained instrument failure**: "The first routine compared an expanded matrix with an unexpanded one using structural equality. It returned false even though every entry of their difference is identically zero... The separately sealed control proves the exact polynomial equality... no sign, unitary or mathematical target was fitted after the failure."

## TESTS ON THIS BENCH
```
1 failed, 17 passed in 12.14s
```
(`tests/test_physical_bridge_global_mass_flux*.py`, from `<audit worktree @ 5e063851>`). Failure: `test_actual_twisted_connection_transports_both_spin_factors` (`assert (False)` on `connection_matches`) — this reproduces exactly the seat's own documented "retained instrument failure" (raw structural/expression-tree matrix comparison), which the report says is deliberately preserved and separately shown mathematically vacuous by a control module. No other failures.

## CLAIMS FOR MAIN
1. On R15's positive-source class, the total boundary flux of R23's mass-eigenline Chern form equals sign(q)·k, k = number of prescribed source arcs — PROVED-BY-SEAT (topological/Stokes argument plus exhaustion, "not only three: it is NOT a three-family selector").
2. The mass-eigenline curvature form equals minus Nie's secondary Euler form under matched conventions, verified symbolically on two charts — COMPUTED (input theorem from Nie cited, not reproved).
3. For k proper source arcs, χ(core)=−k, χ(source-tube)=0, χ(exterior cusp)=−2k, giving the stated per-sign incoming-region index — COMPUTED.
4. A corollary: for k>0 the actual gradient must vanish somewhere in every admissible core (else Stokes is contradicted) — PROVED-BY-SEAT, with the explicit caveat "Neither Morseness nor exactly k points is proved."

## CONFLICTS WITH MAIN
Searched main's `docs`/`frontier` for "mass-eigenline," "secondary Euler," "GLOBAL_MASS_FLUX" — no hits. This path-local round is not referenced anywhere in main's current record. NONE.

## WHAT MAIN WOULD HAVE TO VERIFY
Independently reconstruct U's action on the natural Levi-Civita connection (Γ⊗1+1⊗Γ) and confirm the K=−Φ identity against Nie's stated conventions; recheck the corner-rounding homotopy argument (frozen vs. variable field) and the cusp-asymptotic exhaustion order (high caps → small tubes → corners) before citing k=3 as anything beyond a topological identity in this fixed source class.
