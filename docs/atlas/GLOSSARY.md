# Glossary

Status: reader aid. Formal definitions should be checked against the cited
math files and source cards as those are added.

## Claim Labels

Proven: an exact theorem or computation accepted by the project gate.

Conditional: exact once named assumptions are granted.

Frontier: bounded exploration with a verdict, not promoted.

Dead: falsified, circular, or killed by controls.

## Core Terms

Record: a minimal state variable used by the L/R update system.

L/R update: primitive one-channel integer shears used in the record model.

Residue: what remains when cancellation is not perfectly commutative.

Commutative: operations can swap order without changing the result.

Noncommutative: operation order matters. This is where a residue can survive.

Selector: a rule that chooses one branch, basis, contour, sector, or
representative from several valid options.

S1: the trace-map selector rule that the primitive projective return
linearization reproduce the original `A` sector `t²−3t+1`.

T1: the tangent-filter inheritance assumption: the primitive projective tangent
return inherits the original arithmetic persistence filters. In the current
repo, T1 implies S1 but is not derived.

Projective tangent return: the linearized return map after quotienting by the
central-sign ambiguity of the trace-lift data. It is the object used by
`docs/TRACE_SELECTOR_THEOREM.md`.

Observable: a quantity or effect that can distinguish the proposal from
alternatives or be compared to measurement.

## Representation-Program Terms (the current center of gravity)

Character variety: the space of representations `F₂ → SL(n,ℂ)` up to conjugacy; for `n=2` it is the affine 3-space
of Fricke traces `(x,y,z)`. The project's arena (`knowledge/K001`).

Trace map: the polynomial automorphism of the character variety induced by a mapping class / `GL(2,ℤ)` word; the
project's recurring one is `T(x,y,z) = (z, x, xz − y)`.

κ (kappa): the commutator trace coordinate `tr[A,B] = x²+y²+z²−xyz−2`; conserved by the trace map (= the Sütő
quasicrystal invariant). The void sits at `κ=+2`, the geometric cusp at `κ=−2`.

Metallic family / metallic mean: the matrices `M_m=[[m,1],[1,0]]` (`det=−1`) and their eigenvalues `λ_m=(m+√(m²+4))/2`
(`m=1` golden, `m=2` silver, …); each a once-punctured-torus mapping class (`knowledge/K002`).

Tower / `ρ_n`: the linearization of the `SL(n)` trace map at the trivial fixed point — an `(n²−1)`-dimensional
`GL(2,ℤ)`-representation. The project's central object (`knowledge/K003`, `K008`).

Dickson tower / catalog: the decomposition `ρ_n = ⊕_d Sym^d(M)^{μ_d}`, equivalently `char(ρ_n) = ∏_k char(±M^k)`;
the `char(−M^k)` sectors are the `det=−1` twist.

Two-sequence `μ_d`: the multiplicities `μ_d = [2≤d≤n] + [0≤d≤n−3]` of the symmetric powers in the tower.

`W = V⊕1`: the 3-dimensional external monodromy fundamental (`det W = −1`); the tower is `Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖
W)` (B122). Distinct from the Fricke 3-space `Sym²(V)` (`det=+1`, internal/principal).

Opposition involution `θ = −w₀`: the contragredient/diagram symmetry of `A_{n−1}`; its `±1` eigenspaces give the
catalog's sign multiplicities `⌈/⌊(n−h)/2⌋` (`knowledge/K005`).

Degree = rank: the peripheral relation `L = (−1)^{n−1} M^n` (longitude eigenvalue = meridian eigenvalue to the rank);
a spectral law for all `n` and a geometric state only for `n∈{3,4}` (`knowledge/K004`, P005).

The wall / functorial `Sym(W) → trace-ring`: the standing open prize — a functorial construction realizing the tower
as `Sym^n(W)` (the module identity alone is not a construction).

Two-headed time: a labeled, firewalled *interpretation* of the spectrum's reciprocal/time-reversal symmetry
(`λ↔1/λ`); generic-symplectic, not metallic; no arrow (`philosophy/P006`, B124).

## Topology And Geometry

Puncture: a removed point or opening. In this project it marks the difference
between a closed object and an open one with boundary or cusp behavior.

Cusp: the geometric end associated with a puncture in a hyperbolic setting.

Monodromy: the transformation produced by going once around a loop or through
one period of a fibration.

Holonomy: the transformation accumulated by transporting data around a path.

Figure-eight knot: the knot whose complement appears as the hyperbolic host for
the `A = LR` punctured-torus monodromy.

A-polynomial: a relation between boundary holonomy variables for a knot
complement. In this project it is useful but convention-sensitive.

State integral: an integral expression, often involving quantum dilogarithms,
used to encode topological quantum data. The main obstruction is usually the
choice of contour or thimble.

Thimble: a steepest-descent integration cycle. Selecting the right one is a
selector problem.

## Physics Bridge Terms

Gauge dictionary: a proposed mapping from project math to gauge fields,
charges, and transformations.

Particle dictionary: a proposed mapping from spectra or representations to
physical particles, masses, and couplings.

Spectral triple: a noncommutative-geometry package involving an algebra, a
Hilbert space, and a Dirac operator.

Anomaly cancellation: a consistency condition in quantum field theory where
problematic quantum contributions cancel.

BPS kink: a stable domain-wall-like solution saturating a first-order bound in
some field theories.

Brane: a lower-dimensional surface or domain wall embedded in a higher-
dimensional model.

Unit bridge: a rule that converts dimensionless project numbers into physical
units. Without it, numerical matches to measurements are not meaningful.

`lambda/h`: the dimensionless Fibonacci-Hamiltonian coupling ratio used by the
trace-map spectrum probes. It is not an absolute physical coupling.
