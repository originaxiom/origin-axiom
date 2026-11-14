# S006 — Bell / CHSH on the Fricke surface

**Status: `TESTED-NEGATIVE`** (was `HELD(value-matching)`; resolved this round by a structural argument).
Firewalled; not a claim.

**The proposed calculation.** The Fricke relation `x²+y²+z²−xyz−2 = κ` constrains `z` given `(x,y)`. Treat two
parties sharing a representation and measuring trace functions; compute the CHSH combination on a fixed-κ slice and
ask whether it exceeds the classical bound 2.

**The clean negative (why it cannot violate Bell).** On the **classical** Fricke surface, `z = f(x,y)`
**deterministically** (given the branch). A deterministic functional relationship between the measured quantities
is, by definition, reproducible by **classical hidden variables** — and such correlations satisfy **CHSH ≤ 2
always**. So the *classical character variety cannot violate a Bell inequality*, full stop; there is no number to
hold. This converts the old HELD item into a structural `TESTED-NEGATIVE`: the blocker was not the
trace↔correlator identification but the determinism itself.

**Where a real test would live (not this computation).** Bell violation requires the **quantized** character
variety — Chern–Simons at **finite level `k`**, where `SU(2)_k` (a finite fusion category) replaces the
continuous Fricke surface and genuine non-commuting observables exist. That is a *different* computation (quantum,
finite-`k`), not the classical algebra here.

Related: `S014`/`S015` (the killed identifications), `S021` (the entanglement TESTED-NEGATIVE),
`PHYSICS_EXERCISE.md` Tier 4.
