# Physics resonances — the six paths, computed and adjudicated (+ the Hitchin addendum, Path 7)

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
*Reinforced* (B101, R2 — the spacetime-tower kill): the natural follow-on hope — that Lorentzian signature
**climbs the ranks** (a "tower of spacetimes," 3+1D appearing at `SL(3)` or higher) — is **dead by
computation**. The principal `SL(2)` (the `Symᵏ` ladder) lands in **split real forms** — `Sp(k+1,ℝ)` (odd
`k`), `SO(p,p±1)` (even `k`) — whose maximally-balanced signatures are the structural *opposite* of
Lorentzian. Lorentzian (one timelike) occurs at **exactly `k=2` (`SO(2,1)`) and does not climb** (k=4→SO(3,2),
k=6→SO(4,3), …). `Sp(4,ℝ)=Spin(3,2)` / `SO(3,2)` genuinely appear (k=3,4 = the real AdS₄ / 2+1-conformal
groups) but their symmetric spaces are higher-rank (dim 6), not the rank-1 spacetimes a universe needs. The
single Lorentzian rung is the toy-2+1 one already located; there is no spacetime tower. (Recorded as `dead`:
`docs/atlas/FAILURE_ATLAS.md`.)

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

## Path 7 — Hitchin / higher-Teichmüller → geometric Langlands → N=4 SYM → **CITED CONTEXT ONLY, ceiling stated**
*The mathematics* (B101, banked as higher-Teichmüller geometry — *not* physics): the geometric component
**V0 is the Fuchsian locus of the `SL(3,ℝ)` Hitchin component**, whose cubic-differential directions are
genuinely-`SL(3)` convex-projective deformations. *The cited chain* (published, **not ours**): the Hitchin
component carries a **Higgs-bundle / nonabelian-Hodge** structure, which feeds **geometric Langlands**, which
**Kapustin–Witten** realize as the **S-duality of `N=4` super-Yang–Mills**. This is a real and beautiful
mathematical bridge — but the **ceiling is hard and must be stated**: *even total success along this chain
reaches `N=4` super-Yang–Mills — **one specific, maximally-supersymmetric superconformal gauge theory** —
**NOT** the Standard Model, **NOT** gravity, **NOT** "the universe."* `N=4` SYM has no chiral matter, no
mass scale, exact conformal symmetry; it is a toy/laboratory theory, not observed physics. So this path is
**cited context, never a claim, never a ledger result, never promoted**; it points at where the *mathematics*
of V0 sits in the broader literature, and it does **not** reopen the physics chapter. (The "spacetime climbs
the ranks" sub-hope is separately `dead` — Path 1, B101 R2.)

## Path 8 — the quasicrystal anchor + the single-scale negative → **CITED CONTEXT, headline NEGATIVE (B107)**
*The mathematics* (B107, banked as trace-map dynamics — *not* physics): the SL(2) metallic trace map
`φ_m: a→aᵐb, b→a` **is** the Kohmoto–Kadanoff–Tang / Fibonacci-Hamiltonian trace map (`tr[A,B]` = Sütő's
spectral invariant `x²+y²+z²−xyz−2`, conserved for all `m`; `φ_1=(z,x,xz−y)`). So the tower sits on a **known
quasicrystal object** — cite Sütő (1989), Damanik–Gorodetski–Yessen (Invent. Math. 206, 2016), Roberts
(Physica A 228, 1996). *The decisive negative:* every SL(3) Fibonacci tower eigenvalue is `±φᵏ` — a **single
geometric scale `log φ`** dressed by signs/powers. A mass spectrum is the **Hessian of an action**, generically
not one ratio; a "spectrum" that collapses to one number is **re-presented moduli-space monodromy, not new
physics**. *The corrected overclaims* (withdrawn category errors, like the V90/V91 downgrades): *tower
eigenvalues = anomalous-dimensions/masses* and *torsion = masses* are **NOT** the 3d-3d dictionary — the
tower/torsion are linearized monodromy on the moduli-space tangent, masses are the fluctuation Hessian
(operator content), which the monodromy does not determine. **What is real and citable** is *moduli-space
level only*: `M_SUSY(T[M]) ≅ M_flat(M;G_C)` (vacua = flat connections; GKLP `1305.0937`, DGG `1108.4389`,
`1112.5179`), with the **three flat-connection types ↔ three vacuum branches** (trivial↔unbroken,
geometric↔Higgs, Dehn-filling↔Coulomb) = the three trace-map fixed-point classes (B106). *The one open fork:*
the genuinely irreducible **off-principal** SL(n) reps (multichannel quasiperiodic, not one Fibonacci chain)
are untouched by the tower; B106's D1 root-of-unity data (`±i,−1`; `ω,ω²`, independent of `φ`) confirms the
single-scale pattern **breaks** there — the only place any independent content could live. **All of this is
cited context, never a claim, never promoted; the physics chapter stays CLOSED.** See
`frontier/B107_physics_connection_audit/`.

## Overall verdict (honest)
The disciplined experiment — *compute the numbers, interpret after* — **answers the physics question
cleanly and negatively**: the one decisive, leveraged computation (the Hessian signature) is `(0,2)`
**definite**, closing the Lorentzian door; the selection ordering merely restates `m=1`-is-simplest
(already a theorem); the `n∈{3,4}=SM` map breaks on `n=2`; the det parity is an algebra fact, not a
manifold invariant; the Langlands route has no bounded test. **No new path to physics emerges. The physics
chapter stays closed — now reinforced by a decisive computation rather than only the prior sweep.** The
later Hitchin addendum (Path 7) does not change this: it *cites* where the mathematics of V0 sits (Hitchin /
Langlands / `N=4` SYM) with the ceiling stated, and its "spacetime climbs the ranks" sub-hope is `dead`
(B101 R2). The genuine value of these computations is *mathematical* (the volume ordering, the
systole/volume coherence, the NZ Hessian, and V0 = the Fuchsian locus of the `SL(3,ℝ)` Hitchin component
with its new cubic directions) — see `frontier/B96_geometry_invariants/`, `frontier/B101_hitchin_reframing/`.
Related: [[METALLIC_FOUNDATIONS]], the dead-sweep rows V28/V29/V34/V56/V58/V65.
