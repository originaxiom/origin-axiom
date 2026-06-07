# S006 — Bell / CHSH on the Fricke surface

**Status: `HELD(value-matching)`.** Firewalled; **explicitly not support.** See the HELD rule in `GOVERNANCE.md`.

**The proposed calculation.** The Fricke relation `x²+y²+z²−xyz−2 = κ` constrains `z` given `(x,y)`. Treat two
parties sharing a representation and measuring trace functions; compute the CHSH combination of "correlators" on a
fixed-κ slice and ask whether it exceeds the classical bound 2. This is **pure algebra** on objects we already have.

**Why it is HELD, not testable-as-support.** The blocker is **not tractability** — it is the **arbitrary
`trace-coordinate ↔ measurement-correlator` identification**. Nothing derives that a trace function *is* a quantum
measurement correlator; without that, a CHSH number has no physical meaning. *(Do not write "depends: none / pure
algebra" — that reads as ready; the algebra is ready, the* meaning *is not.)*

**Rule for promotion.** Run the algebra if useful, but the result stays a "number in search of a meaning" until a
derivation of the trace↔correlator identification AND a null test exist. **Do not bank a CHSH value as evidence of
anything physical.**

Related: `S014`/`S015` (the killed identifications this discipline descends from), `PHYSICS_EXERCISE.md` Tier 4.
