# R31: actual compact Poisson wells and their light fermion partners

2026-09-15. Path-local result on the existing sourced route; no shared
B number, main banking, independent proof acceptance or completed TOE.
Scientific design, proof, source, tests and prior were committed and
pushed at `bd5009c4e5037513fd139ecc23e6302e526c863f` before execution.
They are unchanged. The [design](GLOBAL_POISSON_DESIGN.md) and
[analytic proof](GLOBAL_POISSON_PROOF.md) distinguish an all-width
argument from finite identity and numerical checks.

## Result and exact scope

The missing R30 estimate is supplied for one actual global source
family, not just its radial comparator. Fix a smooth compact connected
domain Q in a complete hyperbolic three-manifold, with nonempty boundary,
fixed smooth Dirichlet data, finitely many disjoint neat proper geodesic
arcs with contractible neighborhoods, and fixed positive strengths beta_j.
The metric, truncation, source locations and strengths are not varied.
For the R29 normalized uniform tubes, including their clipped end caps,

    Delta F_epsilon = sum_j 2 beta_j/sinh(epsilon)^2 * 1_(U_j,epsilon),
    F_epsilon|boundary Q = f,       Delta = div grad.

The solution is uniformly bounded off all the arcs, including at the
outer boundary. On any fixed small interior observation cylinder around
one arc, its difference from the matched infinite hyperbolic tube
potential is bounded uniformly in epsilon. In particular,

    |F_epsilon - beta_j log r| <= C,    2 epsilon <= r <= R0,

on a positive-length interior subsegment. Constants may depend on the
fixed compact data. This is not uniform in cusp truncation length, not
a theorem for every R29 weight, and not a logarithmic estimate at an
active Dirichlet endpoint. The indicator source is finite-width and
bounded, but is not a smooth density: F is W^(2,p) for finite p.

**Closing sentence:** For the fixed compact normalized uniform-source
family and R30's declared absolute extending-flat fermion realization,
the global potential has the required interior logarithmic wells and
off-source bounds; k strong arcs with q beta_j >= 1 and nontrivial L
therefore give at least k positive light Dirac pairs as width tends to
zero, not k unpaired Weyl generations.

This is an authored analytic result with supporting controls. The
controls do not independently certify the proof or solve a numerical
compact m202 Green function. Its application to the three-source model
retains that model's proper-arc and regulator hypotheses.

## Why the global matching works

The correctly normalized positive kernel of -Delta on H3 is

    g(d) = (coth d - 1)/(4 pi).

A local cutoff of g gives a point-source parametrix. Its residual lies
on a fixed annulus and is uniformly bounded; the compact Dirichlet
inverse bounds the correction by a fixed Poisson barrier. Poles near
the original boundary are handled by domain monotonicity in a fixed
larger compact domain, not by pretending the injectivity collar is
uniform there. Source mass is bounded: a tube contributes 2 pi beta_j
times arc length plus O(beta_j epsilon) from caps.

Near an interior arc segment, subtract the genuine infinite-tube
convolution. The local Green remainder, separated finite pieces and
integrable infinite axial tails all remain bounded. The convolution
has the already known radial value beta log(tanh r) outside its tube,
with its regular matched interior value. The proof checks the tail and
the uniqueness conditions; it does not sum an unsupported quotient
image series or borrow an endpoint theorem from Euclidean line sources.

For R30's whole-arc scalar trials exp(-qF_epsilon) chi_j s_j, cutoff
derivatives stay away from every source. The numerator is bounded by
the off-source estimate and the norm diverges by the interior logarithm.
Min-max gives, for equal a=q beta >=1,

    lambda <= C epsilon^(2a-2)    when a>1,
    lambda <= C/log(1/epsilon)   when a=1.

These are upper bounds on squared Dirac masses. For unequal strengths
use the largest individual bound on the disjoint trial span. Nontrivial
extending flat L has H0=0, making these scalar eigenvalues positive at
each width; their exact odd partners are supplied by the same Hilbert
complex. For trivial L one must account for H0 before claiming a
positive-pair count. An axial cutoff through a core would spoil the
vanishing quotient and is not used.

## Executed checks, including failures

| First run | Observed result |
|---|---|
| Native producer | 12/12 checks pass; exact identities and all numerical rows retained |
| New test file | 47 passed in 2.75 s |
| Focused R15/R29/R30/C3/R31 files | 115 passed, one inherited GUI warning, in 23.09 s |
| R30 ordered 52 files plus C3 correction and R31 | 508 passed, 16 failed, 8 errors, one warning, in 384.37 s |

All 24 broad failed/error IDs exactly equal R30's: none added, removed
or repaired. The original failures remain scientific evidence, not a
baseline exemption. The repository was read-only throughout these runs.

[Reporting gates and custody](GLOBAL_POISSON_FINAL_CHECKS.txt) record
26 passed and four failed gates. Attribution has one additional flagged
historical-ref token in the sealed retrieval metadata; the other old
failures remain. No full-green or independent banking claim is made.

Independent three-dimensional tube convolutions use two transverse
resolutions and a separately bounded axial tail. The largest
high-resolution discrepancy from the radial solution is
1.1759482276829658e-12. An independent reflected finite-line control
vanishes on its Dirichlet plane and has interior log slope
0.9999991762719147 for unit strength. It explicitly rejects extending
the log formula to the endpoint. Wrong Euclidean kernel, wrong transverse
measure, opposite sign, fixed-height shrinking source and invalid inputs
are separate rejecting controls. Quadrature is not interval-certified.

[Raw-output receipts](GLOBAL_POISSON_RUN_RECEIPTS.json),
[native output](GLOBAL_POISSON_NATIVE_FIRST.json),
[new tests](GLOBAL_POISSON_TESTS_FIRST.txt),
[focused output](GLOBAL_POISSON_FOCUSED_FIRST.txt), and
[broad output](GLOBAL_POISSON_REGRESSION.txt) retain the actual runs.
The [prior/history intake](GLOBAL_POISSON_PRIOR.md) preserves the initial
incorrect literal-search invocation as well as the corrected regex
search. No absence or novelty is inferred from that invocation error.

## Mission effect and next decision

This joins a previously conditional spectral statement to an actual
compact solution of the declared source equations. In this strong-source
regime, merely resolving and narrowing the cores does not make their
compensating fermions heavy. R19's singular three/zero kernel remains
on its different domain; it is not retracted by this calculation.

Next resolve the complete end/domain limit and its normalized currents
without interchanging cusp and width limits by assertion. A proposed
source/end interaction must then show what happens to the partners in
one action, with the full anomaly and allowed gauge transformations.
Finite physical width, enlarged or renormalized defect kinetic spaces,
nontrivial gauge/Higgs topology, and the separate curved-cone route are
not excluded. No physical source strength or width, exactly-three light
spectrum, full-parent lift, empirical mass, gravitational dynamics or
cosmological constant is derived here. PB-BOUNDARY stays OPEN.

The literature supplies the hyperbolic point kernel and the idea of
singularity subtraction; neither is claimed as new. Both complete
papers were personally read, with exact transfer boundaries and source
digests in [the proof](GLOBAL_POISSON_PROOF.md) and
[source custody](GLOBAL_POISSON_SOURCES.json).
