# R31: the global normalized Poisson source and its logarithmic wells

Pre-execution design, 2026-09-15. Path-local continuation of PB-BOUNDARY;
no B allocation or empirical premise. Source, proof, tests and this
design must be committed and pushed before first scientific execution.

BANKED IDENTITY: R15 supplies singular global existence in a prescribed
commuting ansatz; R29 supplies finite-width compact stationary sources
and their exact normalized radial comparator. R30 supplies the compact
absolute fermion realization and a conditional light-pair min-max bound.
None of these is claimed as newly discovered here.

PRIOR ART: [prior and retrieval](GLOBAL_POISSON_PRIOR.md),
[source receipts](GLOBAL_POISSON_SOURCES.json), R15/R29/R30.
Singularity subtraction and the hyperbolic fundamental solution are
published prior art. The candidate transfer argument is
[the proof](GLOBAL_POISSON_PROOF.md).

## P0--P6: scope before tests

P0: for EVERY fixed smooth compact connected hyperbolic domain with
nonempty boundary, fixed finitely many disjoint neat proper geodesic
arcs with contractible neighborhoods, fixed positive strengths and
fixed smooth Dirichlet data, test the normalized UNIFORM tube family
in the proof as epsilon tends to zero. Prove bounded potential off
the arcs and a bounded logarithmic remainder on interior subsegments.
The metric/truncation/source data are not varied in this quantifier.
This is one subfamily of the larger R29 weighted model; it is not a
census of all sources, all physics, or all complete cusp limits.

P1: this is exactly the global-estimate sub-duty recorded in R30 and
X33, on the same sourced path. P2: the atlas context card was consulted;
its epoch-limited general card is not a topic-specific novelty check.
P3: law/lead entries, R15/R29/R30 arguments and relevant implementations,
all-head and deleted-content retrieval were consulted; see the prior.
P4: retain R19's distinct singular domain, R26's fixed-domain stability
and the boundary/curved-cone hatches. A compact bulk-pair result is not
a no-go for those different theories. P5: seal before execution, retain
all runs and use separately sealed follow-ons for any repair. P6:
the honest prior is POSITIVE for the compact normalized-source well
estimate; if it holds, R30 predicts light paired, not unpaired, fermions.
Expected success is not an executed result or an empirical prediction.

## A. The analytic work and what finite tests cannot certify

Derive the compact Green remainder by a fixed local cutoff parametrix
and the bounded Dirichlet inverse. For source poles near the boundary,
compare to a fixed larger compact domain. Bounded total L1 source mass
then gives the off-source bound including boundary portions. Compare
the interior tube to the infinite H3 tube using the same kernel near
the diagonal and a uniformly integrable axial tail. No quotient image
series, unsupported global H2 subtraction or uniform cusp gap is assumed.

Follow the proof through all endpoint and measure factors. The finite
controls below test necessary identities and distinct comparators.
They do not certify the proof by enumeration, compute the actual m202
Green function, give numerical constants in its bound, or constitute
independent proof review. The result must state this distinction.

## B. Exact kernel, metric, source and rejecting controls

1. From the hyperboloid Fermi embedding reconstruct its metric and
   two-point distance. Check g=(coth d-1)/(4pi), its radial equation,
   unit negative flux and small-distance coefficient. Replacing it by
   1/(4pi d) must fail the H3 radial equation at d=1.
2. Check R29's radial field with normalized density 2beta/sinh(epsilon)^2:
   inside/outside equations, value and derivative joins, regular axis,
   and source mass 2pi beta per axis length. The normal-disc-only measure
   must return the DIFFERENT ratio 2/(1+cosh epsilon).
3. Check the hyperbolic ball-volume derivative and endpoint source mass
   tending to zero. A fixed-height tube instead has beta_epsilon of order
   epsilon^2. Check the sign reversal of the radial field explicitly.
4. Check the line-kernel primitive and its hyperbolic distance identity.
   Test the Dirichlet reflected finite line in H3 half-space; at z=0
   it must vanish, so a uniform log formula up to that boundary is rejected.

## C. Numerics fixed before execution

Use float64 SciPy adaptive integration, abs/rel tolerances 2e-11 and
limit 300, with a separately bounded axial tail at Z=14. These error
estimates are NOT interval certification.

* Point-kernel integration along an infinite axis: r=.001,.03,.4,1.2.
  Compare twice the integral on [0,14] with -log(tanh r)/(2pi); allow
  absolute 8e-10 plus the explicit positive tail bound.
* Finite-width three-dimensional convolution: epsilon=.2,.04,.005,
  r=2epsilon and 4epsilon, beta=1.7. Transform transverse radius by
  t=sinh(s)^2/sinh(epsilon)^2. Use Gauss--Legendre order 12 and 24 in t,
  periodic angle grids 24 and 48, respectively. Compare each integral
  and their difference with -beta log(tanh r), tolerance
  5e-8*max(1,abs(expected)), retaining the explicit tail and estimated
  quadrature error. The computation does not use the radial ODE solver.
* Reflected finite line: L=1.3, beta=1, z=.4, r=.1,.01,.001; compare
  direct Green quadrature and the primitive at absolute 8e-10. At
  z=0 and the same radii require zero to 1e-13. Its interior log slope
  from r=.001 and .0001 must differ from beta by less than 2e-5.
* Fixed-height-one tubes: epsilon=.1,.01,.001,.0001. The exact finite
  radial central value must tend toward zero and decrease in absolute
  value at each step; smallest <1e-6, largest >100*smallest. This is
  a different normalization, not a refutation of the fixed-beta result.

Reject invalid radii, widths, quadrature grids and negative source
strength in the positive convolution routine. Zero strength is a
separate exact control. Preserve all numerical rows, not just pass flags.

## D. Spectral implication and reporting

Use the unchanged R30 min-max/domain argument, now with the global
source estimates if the proof survives. Keep q beta>=1 and nontrivial
extending unitary L for at least k POSITIVE light pairs. Keep the
whole-proper-arc cutoffs, H1 scalar form domain, ordinary bulk norm
and absolute outer data. No axial core cutoff or singular-domain swap.
Report upper mass bounds, not exact masses or an exactly-k spectrum.

Run the native producer, new tests, focused R15/R29/R30/C3 tests, then
R30's exact 52-file broad population plus the C3 follow-on and this new
test (54 files). Compare failed/error IDs against R30, retaining its
original failed assertions. Keep the repository read-only during runs;
put exclusive raw captures outside it. Then run reporting gates and
hash/receipt checks without hiding inherited failures. Commit and push
only this seat's branch. Main banking, nonauthor proof review, physical
source/end selection, complete limits and the TOE remain distinct duties.
