# Physics resonances — the six paths, computed and adjudicated

> **SPECULATION — interpretation only.** Nothing here is a claim. No content promotes to `../../CLAIMS.md`
> (GOVERNANCE §5), and none of it may appear as a premise/step in any proof, `frontier/` FINDINGS,
> `papers/` note, ledger row, or commit message. This file *may* cite the mathematics; the mathematics
> never cites it. The **physics chapter stays CLOSED** (V65/B82): this is a logged interpretation of
> bounded topology computations, not a reopening. GOVERNANCE §8 wording binds (a Lorentzian signature is
> "a Lorentzian form in phase space / a Hessian," never "spacetime").

After Paper 0, CC-web proposed six "paths to physics," each framed as *compute a number, interpret after*.
We did exactly that. The **discipline held and the answer is clean**: the single most-leveraged
computation returns negative, and the rest are structural coincidences or break under scrutiny. Below,
each path with the computed number (in `frontier/`) and my honest adjudication.

## Path 1 — the Hessian signature (CC-web's "single most leveraged") → **COMPUTED; located + deflated**
*Hoped*: signature `(3,1)` ⇒ "Lorentzian emergence"; `(4,0)` ⇒ the door closes.
*Computed* (B96): on the **SL(2,ℂ) geometric** (hyperbolic-3-manifold) component the volume Hessian at the
complete structure is **negative definite — `(0,2)` Euclidean** (Mostow max: 155/156 fillings below `vol₀`,
0 above; and the A-variety boundary is 1-complex-dim `L=(−1)ⁿ⁻¹Mⁿ`, so no canonical 4×4 Hessian exists).
**No Lorentzian on the geometric side.**
*Computed* (B97, the honest follow-up): on the **SL(2,ℝ)/Teichmüller** component (the 2+1-gravity phase
space) the Lorentzian form **is** present — it is the `sl(2,ℝ)=so(2,1)` gauge-algebra Killing form, signature
**`(2,1)`** = the 2+1 Minkowski metric, preserved by the holonomy (SO(2,1) local Lorentz). The fiber has an
explicit SL(2,ℝ) Fuchsian rep.
**Verdict (deflated, honest): Lorentzian structure is *located* — on the real/Teichmüller side, as the
gauge algebra of 2+1 gravity (Witten 1988), present *by construction, not emergent*.** It is not on the
geometric side, and it is the well-known structural feature of 2+1 Chern–Simons gravity — **a solvable toy
model with no local gravitons, not 3+1 fundamental physics.** So "Lorentzian emergence" resolves to "the
real component carries the so(2,1) gauge structure of a toy 2+1 gravity" — a precise, deflated *yes-and-no*,
not the emergent spacetime that was hoped for. The 3+1 wall is untouched.

## Path 2 / Path 5 — the volume/torsion ordering (selection) → **COMPUTED (volume), partial**
*Computed* (B96): the metallic volumes are **strictly monotone** `2.030 < 3.664 < 4.814` (`m=1` smallest).
The torsion `|τ₃|` is branch-ambiguous (needs Sage). *Interpretation (logged)*: a "simplest manifold
dominates the path integral" (Turok-type) reading would pick `m=1`. **Honest note**: `m=1` being the
extremum is the same `m=1`-is-simplest fact already proven *mathematically* (the systole, B92/MyCalc-5);
the "path integral selects the universe" reading adds **no new computation** beyond the monotone ordering.

## Path 3 — `n∈{3,4}` = Standard Model gauge groups → **LOGGED, BREAKS on `n=2`**
*Observation*: degree=rank's `Mⁿ=L` is forced to live at `n∈{3,4}` (B95). *The break*: the Standard Model
is `SU(3)×SU(2)×U(1)`; its `SU(2)` factor is the **`n=2`** case, which is **exactly where degree=rank is
degenerate** (B73 A0: SL(2) has *no* Dehn-filling component). So the framework gives structure at `n=3,4`
and **nothing at `n=2`**, while the SM *requires* `n=2`. The window and the SM **do not match** (the SM
would need `n∈{2,3}`, not `{3,4}`). Also: "rank" vs "size" — `SU(3)` has *rank 2*, not 3. **A precise
coincidence that fails on inspection; logged, not pursued.**

## Path 4 — det=−1 as a matter/antimatter (CPT) prerequisite → **LOGGED, it's an algebra fact**
*Observation*: det=−1 simultaneously selects the metallic family and generates the tower's parity sectors
(B93/B94). *Honest note*: this is a **trace-map / character-variety** fact (the `char(−Nᵏ)` sectors), not a
3-manifold invariant — and the metallic *manifolds* are all the det=+1 squares `M_m²`, so there is no
"det=−1 manifold" in the family to carry a distinct volume/torsion. The "CPT prerequisite" reading lives
at the **algebraic (B94)** level, already characterized; **no new manifold invariant distinguishes parity.**

## Path 6 — automorphic forms / Langlands / Kapustin–Witten → **LOGGED, no bounded test**
The objects (the modular surface `H/GL(2,ℤ)`, the `j`-invariant, geodesic spectra) are the right ones, but
"does the tower spectrum form an automorphic function" is **not yet a bounded computation**. Recorded as a
genuine-but-unspecified future direction; no number to compute today.

## Overall verdict (honest)
The disciplined experiment — *compute the numbers, interpret after* — **answers the physics question
cleanly and negatively**: the one decisive, leveraged computation (the Hessian signature) is `(0,2)`
**definite**, closing the Lorentzian door; the selection ordering merely restates `m=1`-is-simplest
(already a theorem); the `n∈{3,4}=SM` map breaks on `n=2`; the det parity is an algebra fact, not a
manifold invariant; the Langlands route has no bounded test. **No new path to physics emerges. The physics
chapter stays closed — now reinforced by a decisive computation rather than only the prior sweep.** The
genuine value of these computations is *mathematical* (the volume ordering, the systole/volume coherence,
the NZ Hessian) — see `frontier/B96_geometry_invariants/`. Related: [[METALLIC_FOUNDATIONS]],
the dead-sweep rows V28/V29/V34/V56/V58/V65.
