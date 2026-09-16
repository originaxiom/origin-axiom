# xB004 — B6's RECIPE AT THE OBJECT'S POINT: it transports, and there is NO VACUUM there — the object's own point is a saddle, because its monodromy is pseudo-Anosov

**Status: banked (frontier, seat branch `sep16-branch`). Verdict PROVED.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any cell ran** — `PREREGISTRATION.md`, sha256
`90b65bf0fda9ecc4c5cb41fa3aac9cbd8904aa46aed6a11a47d17662a6c4e945`, committed `2f39b91` and
pushed to the remote before this file or any result existed. **The order is checkable from this
branch's history**, which is the property xB001 found the record's other seals cannot support.
Gate 5 untouched. Lock: `verification/reproduce.sh`, four cells, each asserting its mathematics.

## The result against the sealed criteria

| cell | sealed criterion | outcome |
|---|---|---|
| **C1** | does B6's recipe transport to the object's point? | **PASS** — `D` has multipliers `(5±√21)/2`, both **positive real**, so the principal `log D` exists |
| **C2** | is the leading potential quadratic there, where B6's is cubic? | **PASS** — and the reason is exact (below) |
| **C3** | the mass² analogue | **no vacuum, no mass²** — the point is a **saddle** |
| **C4** | does B9's cubic vertex have an analogue? | **yes** — a resonant cubic survives |

The declared prior (C2 pass, C4 non-zero) is confirmed. **C3 went further than the prior
anticipated and is the finding.**

## C2 — why B6's cubic is a boundary artefact

B6 builds its potential from a **Möbius** vector field, which is *quadratic* in `τ`, and integrates
it to a **cubic** `V`. That shape is a property of the *boundary* location: at an ideal point the
acting object is a Möbius map on `H`.

At the object's own point the field **vanishes at the fixed point**, so its leading term is
*linear*, and the potential is **quadratic**. Verified: the order-0 part of the induced map's
expansion is zero, the order-1 part is `D`.

**So B7/B8/B9's cubic vertex and its `κ/3` coefficient are artefacts of standing on `∂H`.**

## C3 — the finding: there is no vacuum at the object's point

`D = exp(J·Hess)`, so `Hess = J⁻¹ log D`. `log D` is traceless with eigenvalues `±μ`,
`μ = log((5+√21)/2) = 1.566799237`. Verified symbolically: `J⁻¹ log D` is **symmetric** and

> **`det(Hess) = −μ² = −2.454859849 < 0`** — the quadratic form is **indefinite**.

The object's point is a **saddle**. B8's `mass² = V''(φ) = κ√5 = 1.924847 > 0` is a **minimum**.

> **There is no vacuum, and no single mass², at the object's own point.**

### And this is forced, not accidental

The monodromy is **pseudo-Anosov** (`|tr| = 3 > 2`). A pseudo-Anosov's fixed point on the character
variety is **hyperbolic by definition** — its multipliers are off the unit circle. A stable minimum
would require multipliers on the unit circle, i.e. an elliptic mapping class.

> **The stability of B6's vacuum and the hyperbolicity of the object's monodromy are incompatible.**
> One may have either, not both. B6 obtained stability by standing at the boundary, where the
> dynamics is not the leaf dynamics.

That is the structural statement this arc was for, and it was not anticipated in the sealed prior.

## C4 — a vertex does survive, one order up

The induced map's order-2 **and** order-3 terms are both non-zero (computed exactly), and
`λ²·λ⁻¹ = λ`, so the monomial `u²v` is **resonant**: the cubic cannot be removed by a normal-form
change of variables. A vertex exists at the object's point — at the next order, not at leading
order, and around a saddle rather than a vacuum.

This is also the precise content of xB003's fence 1 ("leading quadratic part, not a global
linearisation"): the obstruction to linearising is exactly this resonance.

## What this does to the B6 → B9 tower

* **B6's potential**: cubic because of the boundary; at the object's point it is quadratic.
* **B7's Fisher–KPP front** to the golden vacuum: there is no vacuum at the object's point to
  travel to. The front is a feature of the boundary minimum.
* **B8's `mass² = κ√5`**: no analogue. The quadratic form is indefinite; `det = −μ²`.
* **B9's fusion vertex**: has an analogue, but at cubic order around a saddle.

**Nothing is withdrawn.** B6 states its own inserted reading ("τ as a field rather than a
coordinate on `H`"), and B6–B9 are each correct under it. This arc says only what the same recipe
gives at the point the object occupies, and the answer is that the tower's stability is not
available there.

## Scope

Dynamics layer, on the fibre's character variety. **Not** a 4d Lorentzian field action; TOE row 4
is untouched. No value, no generation count, no physics reading. `μ = log((5+√21)/2)` is reported
as computed and is **not** interpreted.
