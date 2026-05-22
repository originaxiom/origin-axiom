# Probe B2 — Monodromy action on the moduli space

> **Speculative frontier work.** Logged observations, not claims
> (`../../GOVERNANCE.md` §5). Nothing here is promoted to `CLAIMS.md`.

## The question

`ROADMAP.md` probe B2, from the handoff document's "Step 4B":

> How does the monodromy `A` act on the moduli space of the figure-eight knot
> complement, and what is the continuum limit of that discrete evolution?

The handoff document asserts specifically that *"A acts on the A-polynomial curve
as `(M, L) → (M²L, ML)`."* This probe tests that claim.

## Findings (`probe.py`)

**[1] Action on log-coordinates — solid.**
On the logarithmic boundary coordinates `(log M, log L)` the monodromy acts, by
construction, as the linear map `A` itself. Hence the moduli dynamics are
hyperbolic with multipliers `φ²` and `φ⁻²`; the unique fixed point is the origin
(the complete hyperbolic structure). This is exact and unsurprising — it is
claim P1's eigenstructure expressed in moduli coordinates.

**[2] The handoff's `(M,L) → (M²L, ML)` claim — FALSIFIED.**
Substituting `(M,L) → (M²L, ML)` into the figure-eight A-polynomial does **not**
leave the curve invariant: the image polynomial (degree 9 in `L`) is not
divisible by the A-polynomial — the remainder is nonzero. So that map does **not**
preserve the figure-eight A-polynomial curve.

The likely cause: the handoff conflated two different moduli spaces — the
monodromy acts on the character variety of the *fiber* (the punctured torus),
not on the meridian/longitude `(M, L)` coordinates of the *knot exterior's*
boundary torus. The `(M,L) → (M²L, ML)` formula is not a symmetry of the knot
A-polynomial.

**[3] Continuum limit — solid.**
The continuum limit of iterating the (well-defined, log-coordinate) evolution is
the flow `exp(t · log A)`, with generator the frame + spin-connection element
`log A` from probe B1. At `t = 1` it returns `A` exactly.

## Honest verdict

B2 splits cleanly:

- The **well-defined** moduli evolution — the linear action on `(log M, log L)` —
  is exactly `A`'s own hyperbolic dynamics (`φ±²`). Structurally sound, but it is
  not a gravitational equation of motion; it is a linear flow.
- The handoff's **more ambitious** claim — a specific nonlinear action on the
  knot A-polynomial curve — is **false** as stated. This is a clean negative
  result: it removes an over-reach the 2026-05-22 audit had flagged as likely.

No claim promoted; O1–O5 remain `open`. The genuine open question — the action on
the *fiber* character variety (the Markov-surface trace map) and whether *its*
continuum limit is gravitational — is not addressed here and remains open.
